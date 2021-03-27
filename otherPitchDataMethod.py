import statsapi
import operator

def getPitcherData(playername, pitcherTeamAbbrev):
    with open("Teams2/" + pitcherTeamAbbrev + "/" + "2020" + "/" + playername + ".txt", "r") as FILE:
        content = FILE.read()
        try:
            content_dict = eval(content)
        except Exception as e:
            print("We got an error ", e)
            print("Database Error ")
    return content_dict

def allPitchData():
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}
    problem = []

    def vsEveryone():
        noSpinRate = False
        pitchData = pitch['pitchData']
        if 'type' in pitch['details']:
            pitchType = pitch['details']['type']['description']
            speed = pitchData['startSpeed']
            try:
                spinRate = pitchData['breaks']['spinRate']
            except KeyError as e:
                print(pitch)
                print("Suspected that there is no spin rate:", e)
                print(pitchType + " from " + pitcherName + " on " + game_date + " to " + hitterName + " in the " + inning)
                try:
                    spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                except KeyError:
                    spinRate = teamAverages(pitchType)
                print("1. This will be the spinRate for the pitch: " + str(spinRate))
                noSpinRate = True
            if noSpinRate == False:
                print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning, "to", hitterName, "("+str(testPitches[pitcherName]['pitches'])+")")
        else:
            pitchType = 'Unknown'
            speed = 0
            spinRate = 0

        if pitchType not in everyone:

            everyone[pitchType] = {}
            everyone[pitchType]['amount'] = 1
            everyone['All Pitches']['amount'] += 1
            everyone[pitchType]['allSpin'] = spinRate
            everyone[pitchType]['allSpeed'] = speed
            everyone[pitchType]['spin'] = spinRate
            everyone[pitchType]['speed'] = speed
            everyone['All Pitches']['allSpin'] += spinRate
            everyone['All Pitches']['allSpeed'] = round(everyone['All Pitches']['allSpeed'] + speed, 1)
            everyone['All Pitches']['spin'] = round((everyone['All Pitches']['allSpin']) / (everyone['All Pitches']['amount']), 2)
            everyone['All Pitches']['speed'] = round((everyone['All Pitches']['allSpeed']) / (everyone['All Pitches']['amount']), 2)

            if speed > everyone['All Pitches']['fastest']:
                everyone['All Pitches']['fastest'] = speed
            everyone[pitchType]['fastest'] = speed

            if everyone['All Pitches']['slowest'] != 0:
                if speed < everyone['All Pitches']['slowest']:
                    everyone['All Pitches']['slowest'] = speed
            else:
                everyone['All Pitches']['slowest'] = speed
            everyone[pitchType]['slowest'] = speed

            # everything below until the end of the if statement calculates swings and whiffs
            callDescription = pitch['details']['description']
            ballIsInPlay = pitch['details']['isInPlay']
            if 'Swinging Strike' in callDescription:
                everyone[pitchType]['swings'] = 1
                everyone[pitchType]['whiffs'] = 1
                everyone['All Pitches']['swings'] += 1
                everyone['All Pitches']['whiffs'] += 1
                # print("1. Swing and a miss by", hitterName)
            elif 'Foul' in callDescription or ballIsInPlay:
                everyone[pitchType]['swings'] = 1
                everyone[pitchType]['whiffs'] = 0
                everyone['All Pitches']['swings'] += 1
                everyone['All Pitches']['whiffs'] += 0
                # print("2. Some kind of contact by", hitterName)
                if ballIsInPlay:
                    hitData = pitch['hitData']
                    if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                        everyone[pitchType]['at bats'] = 1
                        everyone[pitchType]['hits'] = 1
                        everyone['All Pitches']['at bats'] += 1
                        everyone['All Pitches']['hits'] += 1
                    else:
                        everyone[pitchType]['at bats'] = 1
                        everyone[pitchType]['hits'] = 0
                        everyone['All Pitches']['at bats'] += 1
                        everyone['All Pitches']['hits'] += 0
        else:
            everyone[pitchType]['amount'] += 1
            everyone['All Pitches']['amount'] += 1

            everyone[pitchType]['allSpin'] += spinRate
            everyone[pitchType]['allSpeed'] = round(everyone[pitchType]['allSpeed'] + speed, 1)
            everyone[pitchType]['spin'] = round((everyone[pitchType]['allSpin']) / (everyone[pitchType]['amount']), 2)
            everyone[pitchType]['speed'] = round((everyone[pitchType]['allSpeed']) / (everyone[pitchType]['amount']),
                                                2)
            everyone['All Pitches']['allSpin'] += spinRate
            everyone['All Pitches']['allSpeed'] = round(everyone['All Pitches']['allSpeed'] + speed, 1)
            everyone['All Pitches']['spin'] = round(
                (everyone['All Pitches']['allSpin']) / (everyone['All Pitches']['amount']), 2)
            everyone['All Pitches']['speed'] = round(
                (everyone['All Pitches']['allSpeed']) / (everyone['All Pitches']['amount']), 2)

            if speed > everyone['All Pitches']['fastest']:
                everyone['All Pitches']['fastest'] = speed
            if speed > everyone[pitchType]['fastest']:
                everyone[pitchType]['fastest'] = speed
            if everyone['All Pitches']['slowest'] != 0:
                if speed < everyone['All Pitches']['slowest']:
                    everyone['All Pitches']['slowest'] = speed
            else:
                everyone['All Pitches']['slowest'] = speed
            if everyone[pitchType]['slowest'] != 0:
                if speed < everyone[pitchType]['slowest']:
                    everyone[pitchType]['slowest'] = speed


            try: # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the key is never actually created, so the except creates the keys)
                # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    everyone[pitchType]['swings'] += 1
                    everyone[pitchType]['whiffs'] += 1
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 1
                    # print("3. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    everyone[pitchType]['swings'] += 1
                    everyone[pitchType]['whiffs'] += 0
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 0
                    # print("4. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                everyone[pitchType]['at bats'] += 1
                                everyone[pitchType]['hits'] += 1
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 1
                            else:
                                everyone[pitchType]['at bats'] += 1
                                everyone[pitchType]['hits'] += 0
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 0
                        except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                everyone[pitchType]['at bats'] = 1
                                everyone[pitchType]['hits'] = 1
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 0
                            else:
                                everyone[pitchType]['at bats'] = 1
                                everyone[pitchType]['hits'] = 0
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 0
            except KeyError:
                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    everyone[pitchType]['swings'] = 1
                    everyone[pitchType]['whiffs'] = 1
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 1
                    # print("5. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    everyone[pitchType]['swings'] = 1
                    everyone[pitchType]['whiffs'] = 0
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 0
                    # print("6. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            everyone[pitchType]['at bats'] = 1
                            everyone[pitchType]['hits'] = 1
                            everyone['All Pitches']['at bats'] += 1
                            everyone['All Pitches']['hits'] += 1
                        else:
                            everyone[pitchType]['at bats'] = 1
                            everyone[pitchType]['hits'] = 0
                            everyone['All Pitches']['at bats'] += 1
                            everyone['All Pitches']['hits'] += 0

    def vsLeft():
        noSpinRate = False
        pitchData = pitch['pitchData']
        if 'type' in pitch['details']:
            speed = pitchData['startSpeed']
            pitchType = pitch['details']['type']['description']
            try:
                spinRate = pitchData['breaks']['spinRate']
            except KeyError as e:
                try:
                    spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                except KeyError:
                    spinRate = teamAverages(pitchType)
                print("2. This will be the spinRate for the pitch: " + str(spinRate))
                noSpinRate = True
        else:
            pitchType = 'Unknown'
            speed = 0
            spinRate = 0

        if pitchType not in lefties:

            lefties[pitchType] = {}
            lefties[pitchType]['amount'] = 1
            lefties['All Pitches']['amount'] += 1
            lefties[pitchType]['allSpin'] = spinRate
            lefties[pitchType]['allSpeed'] = speed
            lefties[pitchType]['spin'] = spinRate
            lefties[pitchType]['speed'] = speed
            lefties['All Pitches']['allSpin'] += spinRate
            lefties['All Pitches']['allSpeed'] = round(lefties['All Pitches']['allSpeed'] + speed, 1)
            lefties['All Pitches']['spin'] = round(
                (lefties['All Pitches']['allSpin']) / (lefties['All Pitches']['amount']), 2)
            lefties['All Pitches']['speed'] = round(
                (lefties['All Pitches']['allSpeed']) / (lefties['All Pitches']['amount']), 2)

            if speed > lefties['All Pitches']['fastest']:
                lefties['All Pitches']['fastest'] = speed
            lefties[pitchType]['fastest'] = speed

            if lefties['All Pitches']['slowest'] != 0:
                if speed < lefties['All Pitches']['slowest']:
                    lefties['All Pitches']['slowest'] = speed
            else:
                lefties['All Pitches']['slowest'] = speed
            lefties[pitchType]['slowest'] = speed

            # everything below until the end of the if statement calculates swings and whiffs
            callDescription = pitch['details']['description']
            ballIsInPlay = pitch['details']['isInPlay']
            if 'Swinging Strike' in callDescription:
                lefties[pitchType]['swings'] = 1
                lefties[pitchType]['whiffs'] = 1
                lefties['All Pitches']['swings'] += 1
                lefties['All Pitches']['whiffs'] += 1
                # print("1. Swing and a miss by", hitterName)
            elif 'Foul' in callDescription or ballIsInPlay:
                lefties[pitchType]['swings'] = 1
                lefties[pitchType]['whiffs'] = 0
                lefties['All Pitches']['swings'] += 1
                lefties['All Pitches']['whiffs'] += 0
                # print("2. Some kind of contact by", hitterName)
                if ballIsInPlay:
                    hitData = pitch['hitData']
                    if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                        lefties[pitchType]['at bats'] = 1
                        lefties[pitchType]['hits'] = 1
                        lefties['All Pitches']['at bats'] += 1
                        lefties['All Pitches']['hits'] += 1
                    else:
                        lefties[pitchType]['at bats'] = 1
                        lefties[pitchType]['hits'] = 0
                        lefties['All Pitches']['at bats'] += 1
                        lefties['All Pitches']['hits'] += 0
        else:
            lefties[pitchType]['amount'] += 1
            lefties['All Pitches']['amount'] += 1

            lefties[pitchType]['allSpin'] += spinRate
            lefties[pitchType]['allSpeed'] = round(lefties[pitchType]['allSpeed'] + speed, 1)
            lefties[pitchType]['spin'] = round((lefties[pitchType]['allSpin']) / (lefties[pitchType]['amount']), 2)
            lefties[pitchType]['speed'] = round((lefties[pitchType]['allSpeed']) / (lefties[pitchType]['amount']),
                                                2)
            lefties['All Pitches']['allSpin'] += spinRate
            lefties['All Pitches']['allSpeed'] = round(lefties['All Pitches']['allSpeed'] + speed, 1)
            lefties['All Pitches']['spin'] = round(
                (lefties['All Pitches']['allSpin']) / (lefties['All Pitches']['amount']), 2)
            lefties['All Pitches']['speed'] = round(
                (lefties['All Pitches']['allSpeed']) / (lefties['All Pitches']['amount']), 2)

            if speed > lefties['All Pitches']['fastest']:
                lefties['All Pitches']['fastest'] = speed
            if speed > lefties[pitchType]['fastest']:
                lefties[pitchType]['fastest'] = speed
            if lefties['All Pitches']['slowest'] != 0:
                if speed < lefties['All Pitches']['slowest']:
                    lefties['All Pitches']['slowest'] = speed
            else:
                lefties['All Pitches']['slowest'] = speed
            if lefties[pitchType]['slowest'] != 0:
                if speed < lefties[pitchType]['slowest']:
                    lefties[pitchType]['slowest'] = speed

            try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
                # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    lefties[pitchType]['swings'] += 1
                    lefties[pitchType]['whiffs'] += 1
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 1
                    # print("3. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    lefties[pitchType]['swings'] += 1
                    lefties[pitchType]['whiffs'] += 0
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 0
                    # print("4. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                lefties[pitchType]['at bats'] += 1
                                lefties[pitchType]['hits'] += 1
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 1
                            else:
                                lefties[pitchType]['at bats'] += 1
                                lefties[pitchType]['hits'] += 0
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 0
                        except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                lefties[pitchType]['at bats'] = 1
                                lefties[pitchType]['hits'] = 1
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 0
                            else:
                                lefties[pitchType]['at bats'] = 1
                                lefties[pitchType]['hits'] = 0
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 0

            except KeyError:
                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    lefties[pitchType]['swings'] = 1
                    lefties[pitchType]['whiffs'] = 1
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 1
                    # print("5. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    lefties[pitchType]['swings'] = 1
                    lefties[pitchType]['whiffs'] = 0
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 0

                    if ballIsInPlay:
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            lefties[pitchType]['at bats'] = 1
                            lefties[pitchType]['hits'] = 1
                            lefties['All Pitches']['at bats'] += 1
                            lefties['All Pitches']['hits'] += 1
                        else:
                            lefties[pitchType]['at bats'] = 1
                            lefties[pitchType]['hits'] = 0
                            lefties['All Pitches']['at bats'] += 1
                            lefties['All Pitches']['hits'] += 0

    def vsRight():
        noSpinRate = False
        pitchData = pitch['pitchData']
        if 'type' in pitch['details']:
            speed = pitchData['startSpeed']
            pitchType = pitch['details']['type']['description']
            try:
                spinRate = pitchData['breaks']['spinRate']
            except KeyError as e:
                try:
                    spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                except KeyError:
                    spinRate = teamAverages(pitchType)
                print("3. This will be the spinRate for the pitch: " + str(spinRate))
                noSpinRate = True
        else:
            pitchType = 'Unknown'
            speed = 0
            spinRate = 0

        if pitchType not in righties:

            righties[pitchType] = {}
            righties[pitchType]['amount'] = 1
            righties['All Pitches']['amount'] += 1
            righties[pitchType]['allSpin'] = spinRate
            righties[pitchType]['allSpeed'] = speed
            righties[pitchType]['spin'] = spinRate
            righties[pitchType]['speed'] = speed
            righties['All Pitches']['allSpin'] += spinRate
            righties['All Pitches']['allSpeed'] = round(righties['All Pitches']['allSpeed'] + speed, 1)
            righties['All Pitches']['spin'] = round(
                (righties['All Pitches']['allSpin']) / (righties['All Pitches']['amount']), 2)
            righties['All Pitches']['speed'] = round(
                (righties['All Pitches']['allSpeed']) / (righties['All Pitches']['amount']), 2)

            if speed > righties['All Pitches']['fastest']:
                righties['All Pitches']['fastest'] = speed
            righties[pitchType]['fastest'] = speed

            if righties['All Pitches']['slowest'] != 0:
                if speed < righties['All Pitches']['slowest']:
                    righties['All Pitches']['slowest'] = speed
            else:
                righties['All Pitches']['slowest'] = speed
            righties[pitchType]['slowest'] = speed

            # everything below until the end of the if statement calculates swings and whiffs
            callDescription = pitch['details']['description']
            ballIsInPlay = pitch['details']['isInPlay']
            if 'Swinging Strike' in callDescription:
                righties[pitchType]['swings'] = 1
                righties[pitchType]['whiffs'] = 1
                righties['All Pitches']['swings'] += 1
                righties['All Pitches']['whiffs'] += 1
                print("1. Swing and a miss by", hitterName)
            elif 'Foul' in callDescription or ballIsInPlay:
                righties[pitchType]['swings'] = 1
                righties[pitchType]['whiffs'] = 0
                righties['All Pitches']['swings'] += 1
                righties['All Pitches']['whiffs'] += 0
                # print("2. Some kind of contact by", hitterName)
                if ballIsInPlay:
                    hitData = pitch['hitData']
                    if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                        righties[pitchType]['at bats'] = 1
                        righties[pitchType]['hits'] = 1
                        righties['All Pitches']['at bats'] += 1
                        righties['All Pitches']['hits'] += 1
                    else:
                        righties[pitchType]['at bats'] = 1
                        righties[pitchType]['hits'] = 0
                        righties['All Pitches']['at bats'] += 1
                        righties['All Pitches']['hits'] += 0
        else:
            righties[pitchType]['amount'] += 1
            righties['All Pitches']['amount'] += 1

            righties[pitchType]['allSpin'] += spinRate
            righties[pitchType]['allSpeed'] = round(righties[pitchType]['allSpeed'] + speed, 1)
            righties[pitchType]['spin'] = round((righties[pitchType]['allSpin']) / (righties[pitchType]['amount']), 2)
            righties[pitchType]['speed'] = round((righties[pitchType]['allSpeed']) / (righties[pitchType]['amount']),
                                                2)
            righties['All Pitches']['allSpin'] += spinRate
            righties['All Pitches']['allSpeed'] = round(righties['All Pitches']['allSpeed'] + speed, 1)
            righties['All Pitches']['spin'] = round(
                (righties['All Pitches']['allSpin']) / (righties['All Pitches']['amount']), 2)
            righties['All Pitches']['speed'] = round(
                (righties['All Pitches']['allSpeed']) / (righties['All Pitches']['amount']), 2)

            if speed > righties['All Pitches']['fastest']:
                righties['All Pitches']['fastest'] = speed
            if speed > righties[pitchType]['fastest']:
                righties[pitchType]['fastest'] = speed
            if righties['All Pitches']['slowest'] != 0:
                if speed < righties['All Pitches']['slowest']:
                    righties['All Pitches']['slowest'] = speed
            else:
                righties['All Pitches']['slowest'] = speed
            if righties[pitchType]['slowest'] != 0:
                if speed < righties[pitchType]['slowest']:
                    righties[pitchType]['slowest'] = speed

            try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
                # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    righties[pitchType]['swings'] += 1
                    righties[pitchType]['whiffs'] += 1
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 1
                    # print("3. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    righties[pitchType]['swings'] += 1
                    righties[pitchType]['whiffs'] += 0
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 0
                    # print("4. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                righties[pitchType]['at bats'] += 1
                                righties[pitchType]['hits'] += 1
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 1
                            else:
                                righties[pitchType]['at bats'] += 1
                                righties[pitchType]['hits'] += 0
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 0
                        except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                righties[pitchType]['at bats'] = 1
                                righties[pitchType]['hits'] = 1
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 0
                            else:
                                righties[pitchType]['at bats'] = 1
                                righties[pitchType]['hits'] = 0
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 0

            except KeyError:
                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    righties[pitchType]['swings'] = 1
                    righties[pitchType]['whiffs'] = 1
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 1
                    # print("5. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    righties[pitchType]['swings'] = 1
                    righties[pitchType]['whiffs'] = 0
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 0
                    # print("6. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            righties[pitchType]['at bats'] = 1
                            righties[pitchType]['hits'] = 1
                            righties['All Pitches']['at bats'] += 1
                            righties['All Pitches']['hits'] += 1
                        else:
                            righties[pitchType]['at bats'] = 1
                            righties[pitchType]['hits'] = 0
                            righties['All Pitches']['at bats'] += 1
                            righties['All Pitches']['hits'] += 0

    sched = statsapi.schedule(start_date='08/14/2020', end_date='09/27/2020')
    # sched = statsapi.schedule(start_date = '07/23/2020', end_date='08/01/2020', team=137)
    for i in range(len(sched)):
        alreadyAdded = []
        testPitches = {} # this dictionary will be used to keep track of pitches thrown for each pitcher in the game and will log the pitcher's previous file just in case pitch counts don't match
        gameId = sched[i]["game_id"]
        game_date = sched[i]["game_date"]
        game_result = sched[i]["summary"]
        game_status = sched[i]["status"]
        game = statsapi.get('game', {'gamePk': gameId})

        allPlays = game['liveData']['plays']['allPlays']
        if game_status != 'Postponed':
            for pa in allPlays:
                inning = pa['about']['halfInning'] + " of the " + inningsName[pa['about']['inning']]
                pitcherName = pa['matchup']['pitcher']['fullName']
                if pa['about']['halfInning'] == 'top':
                    pitcherTeamAbbrev = game['gameData']['teams']['home']['abbreviation']
                else:
                    pitcherTeamAbbrev = game['gameData']['teams']['away']['abbreviation']
                hitterName = pa['matchup']['batter']['fullName']
                hitterBatSide = pa['matchup']['batSide']['description']
                playEvents = pa['playEvents']

                try:
                    if pitcherName not in alreadyAdded and pitcherName not in problem:
                        content_dict = getPitcherData(pitcherName, pitcherTeamAbbrev)  # get pitcher's whole database dictionary
                        pitchingDict = content_dict[pitcherName]['pitching']
                        if 'pitchData' not in pitchingDict:
                            pitchingDict['pitchData'] = {
                                'Dates': [],
                                'Everyone': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}},
                                'Lefties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}},
                                'Righties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}}}

                        if game_date not in pitchingDict['pitchData']['Dates']:
                            if pitcherName not in testPitches:
                                testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'ID': content_dict[pitcherName]['ID'], 'pitches': 0, 'pitchData': content_dict[pitcherName]['pitching']['pitchData']}
                            pDataDict = testPitches[pitcherName]['pitchData']
                            dates = pDataDict['Dates']
                            everyone = pDataDict['Everyone']
                            lefties = pDataDict['Lefties']
                            righties = pDataDict['Righties']
                            resultOfPlay = pa['result']['event']
                            for pitch in playEvents:
                                if pitch['isPitch'] == True and pitch['details']['description'] != 'Automatic Ball':
                                    testPitches[pitcherName]['pitches'] += 1
                                    vsEveryone()
                                    if hitterBatSide == 'Left':
                                        vsLeft()
                                    if hitterBatSide == 'Right':
                                        vsRight()
                                    editedData = editData(everyone, lefties, righties, dates)
                                    testPitches[pitcherName]['pitchData'] = editedData
                        else:
                            alreadyAdded.append(pitcherName)
                            print("Already added for", pitcherName, "on", game_date)
                except Exception as e:
                    print(pitcherName)
                    print(pitch)
                    problem.append(pitcherName)
                    testPitches.pop(pitcherName, None)
                    input(e)
            addData(testPitches, game_date, game, sched[i])

def addData(testPitches, game_date, game, schedule):
    listOfPitchers = list(testPitches.keys())
    for p in range(len(listOfPitchers)):
        pitcherName = listOfPitchers[p]
        pitcherTeam = testPitches[pitcherName]['team']
        pitcherId = testPitches[pitcherName]['ID']
        dates = testPitches[pitcherName]['pitchData']['Dates']
        pitcherData = getPitcherData(pitcherName, pitcherTeam)
        testNumberOfPitches = testPitches[pitcherName]['pitches']
        try:
            actualPitchesPerGame = game['liveData']['boxscore']['teams']['home']['players'][pitcherId]['stats']['pitching']['numberOfPitches']
        except KeyError:
            actualPitchesPerGame = game['liveData']['boxscore']['teams']['away']['players'][pitcherId]['stats']['pitching']['numberOfPitches']
        if testNumberOfPitches == actualPitchesPerGame:
            with open("Teams2/" + pitcherTeam + "/" + "2020" + "/" + pitcherName + ".txt", "w") as FILE:
                dates.append(game_date)
                pitcherData[pitcherName]['pitching']['pitchData'] = testPitches[pitcherName]['pitchData']
                FILE.write(str(pitcherData))
                print("Looks good for " + pitcherName + " with " + str(testNumberOfPitches) + " pitches")
        else:
            try:
                correctedTestPitches, firstPitcher, secondPitcher = checkNextPitcher(testPitches, listOfPitchers, p, game, actualPitchesPerGame, testNumberOfPitches, pitcherName, schedule)
            except Exception as e:
                print(listOfPitchers)
                print(testPitches[pitcherName])
                print(testPitches[listOfPitchers[p+1]])
                print(pitcherName)
                input(e)
            testPitches[firstPitcher] = correctedTestPitches[firstPitcher]
            testPitches[secondPitcher] = correctedTestPitches[secondPitcher]
            dates = testPitches[pitcherName]['pitchData']['Dates']
            testNumberOfPitches = testPitches[pitcherName]['pitches']
            if testNumberOfPitches == actualPitchesPerGame:
                with open("Teams2/" + pitcherTeam + "/" + "2020" + "/" + pitcherName + ".txt", "w") as FILE:
                    dates.append(game_date)
                    pitcherData[pitcherName]['pitching']['pitchData'] = testPitches[pitcherName]['pitchData']
                    FILE.write(str(pitcherData))
                    print("Looks good for " + pitcherName + " with " + str(testNumberOfPitches) + " pitches")
            else:
                input("\nWE HAVE A MASSIVE PROBLEM with " + firstPitcher + " and " + secondPitcher)
                break

def editData(everyone, lefties, righties, dates):
    temp = {}
    leftTemp = {}
    rightTemp = {}
    newNumbers = {}
    newLeftNumbers = {}
    newRightNumbers = {}

    everything = {'Dates': dates} # makes sure the dates list stays in the pitchData dictionary through the reordering of pitches (because the pitchData dictionary will end up this everything dictionary)

    # For everyone
    for pitch in everyone:
        temp[pitch] = everyone[pitch]['amount']
    sortedTemp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in sortedTemp:
        newNumbers[tuple[0]] = {}
        typeOfPitch = newNumbers[tuple[0]]
        for type in everyone[tuple[0]]:
            typeOfPitch[type] = everyone[tuple[0]][type]

    # For lefties
    for pitch in lefties:
        leftTemp[pitch] = lefties[pitch]['amount']
    leftSortedTemp = sorted(leftTemp.items(), key=operator.itemgetter(1), reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in leftSortedTemp:
        newLeftNumbers[tuple[0]] = {}
        typeOfPitch = newLeftNumbers[tuple[0]]
        for type in lefties[tuple[0]]:
            typeOfPitch[type] = lefties[tuple[0]][type]

    # For righties
    for pitch in righties:
        rightTemp[pitch] = righties[pitch]['amount']
    rightSortedTemp = sorted(rightTemp.items(), key=operator.itemgetter(1), reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in rightSortedTemp:
        newRightNumbers[tuple[0]] = {}
        typeOfPitch = newRightNumbers[tuple[0]]
        for type in righties[tuple[0]]:
            typeOfPitch[type] = righties[tuple[0]][type]

    everything['Everyone'] = newNumbers
    everything['Lefties'] = newLeftNumbers
    everything['Righties'] = newRightNumbers

    return everything

def checkNextPitcher(testPitches, listOfPitchers, p, game, actualPitchesPerGame, testNumberOfPitches, beforePitcherName, schedule):
    if testPitches[beforePitcherName]['team'] == testPitches[listOfPitchers[p+1]]['team']:
        nextPitcherName = listOfPitchers[p+1]
    else:
        next = 1
        while testPitches[beforePitcherName]['team'] != testPitches[listOfPitchers[p+next]]['team']:
            next+=1
            nextPitcherName = listOfPitchers[p+next]
    nextPitcherId = testPitches[nextPitcherName]['ID']
    nextPitcherTeam = testPitches[nextPitcherName]['team']
    nextTestNumberOfPitches = testPitches[nextPitcherName]['pitches']
    try:
        nextActualPitchesPerGame = game['liveData']['boxscore']['teams']['home']['players'][nextPitcherId]['stats']['pitching']['numberOfPitches']
    except KeyError:
        nextActualPitchesPerGame = game['liveData']['boxscore']['teams']['away']['players'][nextPitcherId]['stats']['pitching']['numberOfPitches']

    if nextActualPitchesPerGame != nextTestNumberOfPitches:
        if (nextTestNumberOfPitches-nextActualPitchesPerGame) == (actualPitchesPerGame-testNumberOfPitches):
            print("It looks like", nextPitcherName, "has", nextTestNumberOfPitches-nextActualPitchesPerGame, beforePitcherName, "pitches")
            print("Press Enter to Attempt to Fix The Issue \n==============================================\n")
            correctedTestPitches = fixData(beforePitcherName, nextPitcherName, actualPitchesPerGame, schedule)
            return correctedTestPitches, beforePitcherName, nextPitcherName

def fixData(firstPitcher, secondPitcher, actualPitchesPerGame, schedule):
    print("=========================================")
    print("Fixing...")
    print("=========================================")
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th",
                   10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th",
                   18: "18th"}

    def vsEveryone():
        noSpinRate = False
        pitchData = pitch['pitchData']
        if 'type' in pitch['details']:
            pitchType = pitch['details']['type']['description']
            speed = pitchData['startSpeed']
            try:
                spinRate = pitchData['breaks']['spinRate']
            except KeyError as e:
                print(pitch)
                print("Suspected that there is no spin rate:", e)
                print(pitchType + " from " + pitcherName + " on " + game_date + " to " + hitterName + " in the " + inning)
                try:
                    spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                except KeyError:
                    spinRate = teamAverages(pitchType)
                print("1. This will be the spinRate for the pitch: " + str(spinRate))
                noSpinRate = True
            if noSpinRate == False:
                print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning, "to", hitterName, "("+str(testPitches[pitcherName]['pitches'])+")")
        else:
            pitchType = 'Unknown'
            speed = 0
            spinRate = 0

        if pitchType not in everyone:

            everyone[pitchType] = {}
            everyone[pitchType]['amount'] = 1
            everyone['All Pitches']['amount'] += 1
            everyone[pitchType]['allSpin'] = spinRate
            everyone[pitchType]['allSpeed'] = speed
            everyone[pitchType]['spin'] = spinRate
            everyone[pitchType]['speed'] = speed
            everyone['All Pitches']['allSpin'] += spinRate
            everyone['All Pitches']['allSpeed'] = round(everyone['All Pitches']['allSpeed'] + speed, 1)
            everyone['All Pitches']['spin'] = round((everyone['All Pitches']['allSpin']) / (everyone['All Pitches']['amount']), 2)
            everyone['All Pitches']['speed'] = round((everyone['All Pitches']['allSpeed']) / (everyone['All Pitches']['amount']), 2)

            if speed > everyone['All Pitches']['fastest']:
                everyone['All Pitches']['fastest'] = speed
            everyone[pitchType]['fastest'] = speed

            if everyone['All Pitches']['slowest'] != 0:
                if speed < everyone['All Pitches']['slowest']:
                    everyone['All Pitches']['slowest'] = speed
            else:
                everyone['All Pitches']['slowest'] = speed
            everyone[pitchType]['slowest'] = speed

            # everything below until the end of the if statement calculates swings and whiffs
            callDescription = pitch['details']['description']
            ballIsInPlay = pitch['details']['isInPlay']
            if 'Swinging Strike' in callDescription:
                everyone[pitchType]['swings'] = 1
                everyone[pitchType]['whiffs'] = 1
                everyone['All Pitches']['swings'] += 1
                everyone['All Pitches']['whiffs'] += 1
                # print("1. Swing and a miss by", hitterName)
            elif 'Foul' in callDescription or ballIsInPlay:
                everyone[pitchType]['swings'] = 1
                everyone[pitchType]['whiffs'] = 0
                everyone['All Pitches']['swings'] += 1
                everyone['All Pitches']['whiffs'] += 0
                # print("2. Some kind of contact by", hitterName)
                if ballIsInPlay:
                    hitData = pitch['hitData']
                    if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                        everyone[pitchType]['at bats'] = 1
                        everyone[pitchType]['hits'] = 1
                        everyone['All Pitches']['at bats'] += 1
                        everyone['All Pitches']['hits'] += 1
                    else:
                        everyone[pitchType]['at bats'] = 1
                        everyone[pitchType]['hits'] = 0
                        everyone['All Pitches']['at bats'] += 1
                        everyone['All Pitches']['hits'] += 0
        else:
            everyone[pitchType]['amount'] += 1
            everyone['All Pitches']['amount'] += 1

            everyone[pitchType]['allSpin'] += spinRate
            everyone[pitchType]['allSpeed'] = round(everyone[pitchType]['allSpeed'] + speed, 1)
            everyone[pitchType]['spin'] = round((everyone[pitchType]['allSpin']) / (everyone[pitchType]['amount']), 2)
            everyone[pitchType]['speed'] = round((everyone[pitchType]['allSpeed']) / (everyone[pitchType]['amount']),
                                                2)
            everyone['All Pitches']['allSpin'] += spinRate
            everyone['All Pitches']['allSpeed'] = round(everyone['All Pitches']['allSpeed'] + speed, 1)
            everyone['All Pitches']['spin'] = round(
                (everyone['All Pitches']['allSpin']) / (everyone['All Pitches']['amount']), 2)
            everyone['All Pitches']['speed'] = round(
                (everyone['All Pitches']['allSpeed']) / (everyone['All Pitches']['amount']), 2)

            if speed > everyone['All Pitches']['fastest']:
                everyone['All Pitches']['fastest'] = speed
            if speed > everyone[pitchType]['fastest']:
                everyone[pitchType]['fastest'] = speed
            if everyone['All Pitches']['slowest'] != 0:
                if speed < everyone['All Pitches']['slowest']:
                    everyone['All Pitches']['slowest'] = speed
            else:
                everyone['All Pitches']['slowest'] = speed
            if everyone[pitchType]['slowest'] != 0:
                if speed < everyone[pitchType]['slowest']:
                    everyone[pitchType]['slowest'] = speed


            try: # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the key is never actually created, so the except creates the keys)
                # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    everyone[pitchType]['swings'] += 1
                    everyone[pitchType]['whiffs'] += 1
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 1
                    # print("3. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    everyone[pitchType]['swings'] += 1
                    everyone[pitchType]['whiffs'] += 0
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 0
                    # print("4. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                everyone[pitchType]['at bats'] += 1
                                everyone[pitchType]['hits'] += 1
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 1
                            else:
                                everyone[pitchType]['at bats'] += 1
                                everyone[pitchType]['hits'] += 0
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 0
                        except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                everyone[pitchType]['at bats'] = 1
                                everyone[pitchType]['hits'] = 1
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 0
                            else:
                                everyone[pitchType]['at bats'] = 1
                                everyone[pitchType]['hits'] = 0
                                everyone['All Pitches']['at bats'] += 1
                                everyone['All Pitches']['hits'] += 0
            except KeyError:
                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    everyone[pitchType]['swings'] = 1
                    everyone[pitchType]['whiffs'] = 1
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 1
                    # print("5. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    everyone[pitchType]['swings'] = 1
                    everyone[pitchType]['whiffs'] = 0
                    everyone['All Pitches']['swings'] += 1
                    everyone['All Pitches']['whiffs'] += 0
                    # print("6. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            everyone[pitchType]['at bats'] = 1
                            everyone[pitchType]['hits'] = 1
                            everyone['All Pitches']['at bats'] += 1
                            everyone['All Pitches']['hits'] += 1
                        else:
                            everyone[pitchType]['at bats'] = 1
                            everyone[pitchType]['hits'] = 0
                            everyone['All Pitches']['at bats'] += 1
                            everyone['All Pitches']['hits'] += 0

    def vsLeft():
        noSpinRate = False
        pitchData = pitch['pitchData']
        if 'type' in pitch['details']:
            speed = pitchData['startSpeed']
            pitchType = pitch['details']['type']['description']
            try:
                spinRate = pitchData['breaks']['spinRate']
            except KeyError as e:
                try:
                    spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                except KeyError:
                    spinRate = teamAverages(pitchType)
                print("2. This will be the spinRate for the pitch: " + str(spinRate))
                noSpinRate = True
        else:
            pitchType = 'Unknown'
            speed = 0
            spinRate = 0

        if pitchType not in lefties:

            lefties[pitchType] = {}
            lefties[pitchType]['amount'] = 1
            lefties['All Pitches']['amount'] += 1
            lefties[pitchType]['allSpin'] = spinRate
            lefties[pitchType]['allSpeed'] = speed
            lefties[pitchType]['spin'] = spinRate
            lefties[pitchType]['speed'] = speed
            lefties['All Pitches']['allSpin'] += spinRate
            lefties['All Pitches']['allSpeed'] = round(lefties['All Pitches']['allSpeed'] + speed, 1)
            lefties['All Pitches']['spin'] = round(
                (lefties['All Pitches']['allSpin']) / (lefties['All Pitches']['amount']), 2)
            lefties['All Pitches']['speed'] = round(
                (lefties['All Pitches']['allSpeed']) / (lefties['All Pitches']['amount']), 2)

            if speed > lefties['All Pitches']['fastest']:
                lefties['All Pitches']['fastest'] = speed
            lefties[pitchType]['fastest'] = speed

            if lefties['All Pitches']['slowest'] != 0:
                if speed < lefties['All Pitches']['slowest']:
                    lefties['All Pitches']['slowest'] = speed
            else:
                lefties['All Pitches']['slowest'] = speed
            lefties[pitchType]['slowest'] = speed

            # everything below until the end of the if statement calculates swings and whiffs
            callDescription = pitch['details']['description']
            ballIsInPlay = pitch['details']['isInPlay']
            if 'Swinging Strike' in callDescription:
                lefties[pitchType]['swings'] = 1
                lefties[pitchType]['whiffs'] = 1
                lefties['All Pitches']['swings'] += 1
                lefties['All Pitches']['whiffs'] += 1
                # print("1. Swing and a miss by", hitterName)
            elif 'Foul' in callDescription or ballIsInPlay:
                lefties[pitchType]['swings'] = 1
                lefties[pitchType]['whiffs'] = 0
                lefties['All Pitches']['swings'] += 1
                lefties['All Pitches']['whiffs'] += 0
                # print("2. Some kind of contact by", hitterName)
                if ballIsInPlay:
                    hitData = pitch['hitData']
                    if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                        lefties[pitchType]['at bats'] = 1
                        lefties[pitchType]['hits'] = 1
                        lefties['All Pitches']['at bats'] += 1
                        lefties['All Pitches']['hits'] += 1
                    else:
                        lefties[pitchType]['at bats'] = 1
                        lefties[pitchType]['hits'] = 0
                        lefties['All Pitches']['at bats'] += 1
                        lefties['All Pitches']['hits'] += 0
        else:
            lefties[pitchType]['amount'] += 1
            lefties['All Pitches']['amount'] += 1

            lefties[pitchType]['allSpin'] += spinRate
            lefties[pitchType]['allSpeed'] = round(lefties[pitchType]['allSpeed'] + speed, 1)
            lefties[pitchType]['spin'] = round((lefties[pitchType]['allSpin']) / (lefties[pitchType]['amount']), 2)
            lefties[pitchType]['speed'] = round((lefties[pitchType]['allSpeed']) / (lefties[pitchType]['amount']),
                                                2)
            lefties['All Pitches']['allSpin'] += spinRate
            lefties['All Pitches']['allSpeed'] = round(lefties['All Pitches']['allSpeed'] + speed, 1)
            lefties['All Pitches']['spin'] = round(
                (lefties['All Pitches']['allSpin']) / (lefties['All Pitches']['amount']), 2)
            lefties['All Pitches']['speed'] = round(
                (lefties['All Pitches']['allSpeed']) / (lefties['All Pitches']['amount']), 2)

            if speed > lefties['All Pitches']['fastest']:
                lefties['All Pitches']['fastest'] = speed
            if speed > lefties[pitchType]['fastest']:
                lefties[pitchType]['fastest'] = speed
            if lefties['All Pitches']['slowest'] != 0:
                if speed < lefties['All Pitches']['slowest']:
                    lefties['All Pitches']['slowest'] = speed
            else:
                lefties['All Pitches']['slowest'] = speed
            if lefties[pitchType]['slowest'] != 0:
                if speed < lefties[pitchType]['slowest']:
                    lefties[pitchType]['slowest'] = speed

            try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
                # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    lefties[pitchType]['swings'] += 1
                    lefties[pitchType]['whiffs'] += 1
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 1
                    # print("3. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    lefties[pitchType]['swings'] += 1
                    lefties[pitchType]['whiffs'] += 0
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 0
                    # print("4. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                lefties[pitchType]['at bats'] += 1
                                lefties[pitchType]['hits'] += 1
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 1
                            else:
                                lefties[pitchType]['at bats'] += 1
                                lefties[pitchType]['hits'] += 0
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 0
                        except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                lefties[pitchType]['at bats'] = 1
                                lefties[pitchType]['hits'] = 1
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 0
                            else:
                                lefties[pitchType]['at bats'] = 1
                                lefties[pitchType]['hits'] = 0
                                lefties['All Pitches']['at bats'] += 1
                                lefties['All Pitches']['hits'] += 0

            except KeyError:
                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    lefties[pitchType]['swings'] = 1
                    lefties[pitchType]['whiffs'] = 1
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 1
                    # print("5. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    lefties[pitchType]['swings'] = 1
                    lefties[pitchType]['whiffs'] = 0
                    lefties['All Pitches']['swings'] += 1
                    lefties['All Pitches']['whiffs'] += 0

                    if ballIsInPlay:
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            lefties[pitchType]['at bats'] = 1
                            lefties[pitchType]['hits'] = 1
                            lefties['All Pitches']['at bats'] += 1
                            lefties['All Pitches']['hits'] += 1
                        else:
                            lefties[pitchType]['at bats'] = 1
                            lefties[pitchType]['hits'] = 0
                            lefties['All Pitches']['at bats'] += 1
                            lefties['All Pitches']['hits'] += 0

    def vsRight():
        noSpinRate = False
        pitchData = pitch['pitchData']
        if 'type' in pitch['details']:
            speed = pitchData['startSpeed']
            pitchType = pitch['details']['type']['description']
            try:
                spinRate = pitchData['breaks']['spinRate']
            except KeyError as e:
                try:
                    spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                except KeyError:
                    spinRate = teamAverages(pitchType)
                print("3. This will be the spinRate for the pitch: " + str(spinRate))
                noSpinRate = True
        else:
            pitchType = 'Unknown'
            speed = 0
            spinRate = 0

        if pitchType not in righties:

            righties[pitchType] = {}
            righties[pitchType]['amount'] = 1
            righties['All Pitches']['amount'] += 1
            righties[pitchType]['allSpin'] = spinRate
            righties[pitchType]['allSpeed'] = speed
            righties[pitchType]['spin'] = spinRate
            righties[pitchType]['speed'] = speed
            righties['All Pitches']['allSpin'] += spinRate
            righties['All Pitches']['allSpeed'] = round(righties['All Pitches']['allSpeed'] + speed, 1)
            righties['All Pitches']['spin'] = round(
                (righties['All Pitches']['allSpin']) / (righties['All Pitches']['amount']), 2)
            righties['All Pitches']['speed'] = round(
                (righties['All Pitches']['allSpeed']) / (righties['All Pitches']['amount']), 2)

            if speed > righties['All Pitches']['fastest']:
                righties['All Pitches']['fastest'] = speed
            righties[pitchType]['fastest'] = speed

            if righties['All Pitches']['slowest'] != 0:
                if speed < righties['All Pitches']['slowest']:
                    righties['All Pitches']['slowest'] = speed
            else:
                righties['All Pitches']['slowest'] = speed
            righties[pitchType]['slowest'] = speed

            # everything below until the end of the if statement calculates swings and whiffs
            callDescription = pitch['details']['description']
            ballIsInPlay = pitch['details']['isInPlay']
            if 'Swinging Strike' in callDescription:
                righties[pitchType]['swings'] = 1
                righties[pitchType]['whiffs'] = 1
                righties['All Pitches']['swings'] += 1
                righties['All Pitches']['whiffs'] += 1
                print("1. Swing and a miss by", hitterName)
            elif 'Foul' in callDescription or ballIsInPlay:
                righties[pitchType]['swings'] = 1
                righties[pitchType]['whiffs'] = 0
                righties['All Pitches']['swings'] += 1
                righties['All Pitches']['whiffs'] += 0
                # print("2. Some kind of contact by", hitterName)
                if ballIsInPlay:
                    hitData = pitch['hitData']
                    if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                        righties[pitchType]['at bats'] = 1
                        righties[pitchType]['hits'] = 1
                        righties['All Pitches']['at bats'] += 1
                        righties['All Pitches']['hits'] += 1
                    else:
                        righties[pitchType]['at bats'] = 1
                        righties[pitchType]['hits'] = 0
                        righties['All Pitches']['at bats'] += 1
                        righties['All Pitches']['hits'] += 0
        else:
            righties[pitchType]['amount'] += 1
            righties['All Pitches']['amount'] += 1

            righties[pitchType]['allSpin'] += spinRate
            righties[pitchType]['allSpeed'] = round(righties[pitchType]['allSpeed'] + speed, 1)
            righties[pitchType]['spin'] = round((righties[pitchType]['allSpin']) / (righties[pitchType]['amount']), 2)
            righties[pitchType]['speed'] = round((righties[pitchType]['allSpeed']) / (righties[pitchType]['amount']),
                                                2)
            righties['All Pitches']['allSpin'] += spinRate
            righties['All Pitches']['allSpeed'] = round(righties['All Pitches']['allSpeed'] + speed, 1)
            righties['All Pitches']['spin'] = round(
                (righties['All Pitches']['allSpin']) / (righties['All Pitches']['amount']), 2)
            righties['All Pitches']['speed'] = round(
                (righties['All Pitches']['allSpeed']) / (righties['All Pitches']['amount']), 2)

            if speed > righties['All Pitches']['fastest']:
                righties['All Pitches']['fastest'] = speed
            if speed > righties[pitchType]['fastest']:
                righties[pitchType]['fastest'] = speed
            if righties['All Pitches']['slowest'] != 0:
                if speed < righties['All Pitches']['slowest']:
                    righties['All Pitches']['slowest'] = speed
            else:
                righties['All Pitches']['slowest'] = speed
            if righties[pitchType]['slowest'] != 0:
                if speed < righties[pitchType]['slowest']:
                    righties[pitchType]['slowest'] = speed

            try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
                # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    righties[pitchType]['swings'] += 1
                    righties[pitchType]['whiffs'] += 1
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 1
                    # print("3. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    righties[pitchType]['swings'] += 1
                    righties[pitchType]['whiffs'] += 0
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 0
                    # print("4. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                righties[pitchType]['at bats'] += 1
                                righties[pitchType]['hits'] += 1
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 1
                            else:
                                righties[pitchType]['at bats'] += 1
                                righties[pitchType]['hits'] += 0
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 0
                        except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                righties[pitchType]['at bats'] = 1
                                righties[pitchType]['hits'] = 1
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 0
                            else:
                                righties[pitchType]['at bats'] = 1
                                righties[pitchType]['hits'] = 0
                                righties['All Pitches']['at bats'] += 1
                                righties['All Pitches']['hits'] += 0

            except KeyError:
                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    righties[pitchType]['swings'] = 1
                    righties[pitchType]['whiffs'] = 1
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 1
                    # print("5. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    righties[pitchType]['swings'] = 1
                    righties[pitchType]['whiffs'] = 0
                    righties['All Pitches']['swings'] += 1
                    righties['All Pitches']['whiffs'] += 0
                    # print("6. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            righties[pitchType]['at bats'] = 1
                            righties[pitchType]['hits'] = 1
                            righties['All Pitches']['at bats'] += 1
                            righties['All Pitches']['hits'] += 1
                        else:
                            righties[pitchType]['at bats'] = 1
                            righties[pitchType]['hits'] = 0
                            righties['All Pitches']['at bats'] += 1
                            righties['All Pitches']['hits'] += 0

    testPitches = {}  # this dictionary will be used to keep track of pitches thrown for each pitcher in the game and will log the pitcher's previous file just in case pitch counts don't match
    gameId = schedule["game_id"]
    game_date = schedule["game_date"]
    game_result = schedule["summary"]
    game_status = schedule["status"]
    game = statsapi.get('game', {'gamePk': gameId})

    allPlays = game['liveData']['plays']['allPlays']
    if game_status != 'Postponed':
        for pa in allPlays:
            inning = pa['about']['halfInning'] + " of the " + inningsName[pa['about']['inning']]
            pitcherName = pa['matchup']['pitcher']['fullName']
            if pa['about']['halfInning'] == 'top':
                pitcherTeamAbbrev = game['gameData']['teams']['home']['abbreviation']
            else:
                pitcherTeamAbbrev = game['gameData']['teams']['away']['abbreviation']
            hitterName = pa['matchup']['batter']['fullName']
            hitterBatSide = pa['matchup']['batSide']['description']
            playEvents = pa['playEvents']

            if pitcherName == firstPitcher:
                content_dict = getPitcherData(pitcherName,pitcherTeamAbbrev)  # get pitcher's whole database dictionary
                pitchingDict = content_dict[pitcherName]['pitching']
                if 'pitchData' not in pitchingDict:
                    pitchingDict['pitchData'] = {
                        'Dates': [],
                        'Everyone': {
                            'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}},
                        'Lefties': {
                            'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}},
                        'Righties': {
                            'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}}}

                if game_date not in pitchingDict['pitchData']['Dates']:
                    if pitcherName not in testPitches:
                        testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'ID': content_dict[pitcherName]['ID'], 'pitches': 0, 'pitchData': content_dict[pitcherName]['pitching']['pitchData']}
                    pDataDict = testPitches[pitcherName]['pitchData']
                    dates = pDataDict['Dates']
                    everyone = pDataDict['Everyone']
                    lefties = pDataDict['Lefties']
                    righties = pDataDict['Righties']
                    resultOfPlay = pa['result']['event']
                    for pitch in playEvents:
                        if pitch['isPitch'] == True and pitch['details']['description'] != 'Automatic Ball':
                            testPitches[pitcherName]['pitches'] += 1
                            vsEveryone()
                            if hitterBatSide == 'Left':
                                vsLeft()
                            if hitterBatSide == 'Right':
                                vsRight()
                            editData(everyone, lefties, righties, dates)
                            # print(pitcherName, tested[pitcherName], testPitches[pitcherName]['pitchData']['Everyone']['All Pitches']['amount'])
            if pitcherName == secondPitcher:
                resultOfPlay = pa['result']['event']
                for pitch in playEvents:
                    if pitch['isPitch'] == True and pitch['details']['description'] != 'Automatic Ball':

                        if testPitches[firstPitcher]['pitches'] < actualPitchesPerGame:
                            pitcherName = firstPitcher
                        else:
                            pitcherName = secondPitcher

                        content_dict = getPitcherData(pitcherName, pitcherTeamAbbrev)  # get pitcher's whole database dictionary
                        pitchingDict = content_dict[pitcherName]['pitching']
                        if 'pitchData' not in pitchingDict:
                            pitchingDict['pitchData'] = {
                                'Dates': [],
                                'Everyone': {
                                    'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}},
                                'Lefties': {
                                    'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}},
                                'Righties': {
                                    'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}}}

                        if game_date not in pitchingDict['pitchData']['Dates']:
                            if pitcherName not in testPitches:
                                testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'ID': content_dict[pitcherName]['ID'], 'pitches': 0, 'pitchData': content_dict[pitcherName]['pitching']['pitchData']}

                            pDataDict = testPitches[pitcherName]['pitchData']
                            dates = pDataDict['Dates']
                            everyone = pDataDict['Everyone']
                            lefties = pDataDict['Lefties']
                            righties = pDataDict['Righties']

                            testPitches[pitcherName]['pitches'] += 1

                            vsEveryone()
                            if hitterBatSide == 'Left':
                                vsLeft()
                            if hitterBatSide == 'Right':
                                vsRight()
                            editedData = editData(everyone, lefties, righties, dates)
                            testPitches[pitcherName]['pitchData'] = editedData
                            # print(pitcherName, tested[pitcherName], testPitches[pitcherName]['pitchData']['Everyone']['All Pitches']['amount'])
        # addData(testPitches, game_date, game, schedule)
        return testPitches

def analyzePitchData():
    pitcherFile = getPitcherData('Drew Smyly', "SF")
    pitchData = pitcherFile['Drew Smyly']['pitching']['pitchData']
    dates = pitchData['Dates']
    everyone = pitchData['Everyone']
    lefties = pitchData['Lefties']
    righties = pitchData['Righties']
    pitchName = []
    pitchAmount = []
    for pitch in everyone:
        if pitch != 'All Pitches':
            pitchName.append(pitch+" ("+str(everyone[pitch]['speed'])+" MPH)")
            pitchAmount.append(everyone[pitch]['amount'])
            print(pitch, everyone[pitch]['amount'])
    print(pitchName)
    print(pitchAmount)

def pitchCharts(pitcherName, pitcherTeamAbbrev, againstWho):
    pitcherFile = getPitcherData(pitcherName, pitcherTeamAbbrev)
    pitchData = pitcherFile[pitcherName]['pitching']['pitchData']
    dates = pitchData['Dates']
    everyone = pitchData['Everyone']
    lefties = pitchData['Lefties']
    righties = pitchData['Righties']
    pitchName = []
    pitchAmount = []
    specificType = pitchData[againstWho]
    for pitch in pitchData[againstWho]:
        if pitch != 'All Pitches':
            pitchName.append(pitch+" ("+str(everyone[pitch]['speed'])+" MPH/"+str(everyone[pitch]['spin'])+" RPM)")
            pitchAmount.append(specificType[pitch]['amount'])

    return pitchName, pitchAmount

def teamAverages(pitch):
    teams = ['ARI', 'ATL','BAL','BOS','CHC','CIN','CLE','COL','CWS','DET','HOU','KC','LAA','LAD','MIA','MIL','MIN','NYM','NYY','OAK','PHI','PIT','SD','SEA','SF','STL','TB','TEX','TOR','WSH']
    numberOfPitchersWithPitch = 0
    spin = 0
    for team in teams:
        with open("Teams2/"+team+"/2020/pitchers.txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("We got an error ", e)
                print("Database Error ")
        pitcherList = content_dict['players']

        for pitcher in pitcherList:
            with open("Teams2/"+team+"/2020/"+pitcher+".txt", "r") as F:
                data = F.read()
                try:
                    dataDict = eval(data)
                except Exception as e:
                    print("We got an error ", e)
                    print("Database Error")
            if 'pitchData' in dataDict[pitcher]['pitching']:
                pitchData = dataDict[pitcher]['pitching']['pitchData']['Everyone']
                if pitch in pitchData:
                    spin += pitchData[pitch]['spin']
                    numberOfPitchersWithPitch += 1
    return spin/numberOfPitchersWithPitch



# averageSpin = teamAverages("Sinker")
# print(averageSpin)


allPitchData()
# analyzePitchData()