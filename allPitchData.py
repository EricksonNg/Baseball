import statsapi
import operator

def getPitcherData(playername, pitcherTeamAbbrev):
    with open("Teams/" + pitcherTeamAbbrev + "/" + "2020" + "/" + playername + ".txt", "r") as FILE:
        content = FILE.read()
        try:
            content_dict = eval(content)
        except Exception as e:
            print("We got an error ", e)
            print("Database Error ")
    return content_dict

def allPitchData():
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}

    def test():
        inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th",
                       10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th",
                       18: "18th"}

        actualNumberOfPitchers = 71

        sched = statsapi.schedule(start_date='08/01/2020', team=137)
        for i in range(len(sched)):
            testPitches = {}  # this dictionary will be used to keep track of pitches thrown for each pitcher in the game and will log the pitcher's previous file just in case pitch counts don't match
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

                    if pitcherName == 'Drew Smyly':
                        content_dict = getPitcherData(pitcherName, pitcherTeamAbbrev)  # get pitcher's whole database dictionary
                        pitchingDict = content_dict[pitcherName]['pitching']
                        if 'pitchData' not in pitchingDict:
                            pitchingDict['pitchData'] = {
                                'Dates': [],
                                'Everyone': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}},
                                'Lefties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}},
                                'Righties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}}}
                        pDataDict = pitchingDict['pitchData']
                        dates = pDataDict['Dates']
                        everyone = pDataDict['Everyone']
                        lefties = pDataDict['Lefties']
                        righties = pDataDict['Righties']

                        if game_date not in dates:
                            other = getPitcherData(pitcherName, pitcherTeamAbbrev)  # having a separate getPitcherData() call that'll be used by testPitches helps avoid a weird counting error (still don't know why it happens)
                            if pitcherName not in testPitches:
                                testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'pitches': 0, 'data': other}

                            resultOfPlay = pa['result']['event']
                            for pitch in playEvents:
                                if pitch['isPitch'] == True:
                                    testPitches[pitcherName]['pitches'] += 1
                                    vsEveryone()
                                    if hitterBatSide == 'Left':
                                        vsLeft()
                                    if hitterBatSide == 'Right':
                                        vsRight()
                                    addData(pitcherName, everyone, lefties, righties, pDataDict, content_dict, pitcherTeamAbbrev, dates)
                    if pitcherName == 'Shaun Anderson':
                            resultOfPlay = pa['result']['event']
                            for pitch in playEvents:
                                if pitch['isPitch'] == True:

                                    if testPitches['Drew Smyly']['pitches'] < actualNumberOfPitchers:
                                        pitcherName = 'Drew Smyly'
                                    else:
                                        pitcherName = 'Shaun Anderson'

                                    content_dict = getPitcherData(pitcherName, pitcherTeamAbbrev)  # get pitcher's whole database dictionary
                                    pitchingDict = content_dict[pitcherName]['pitching']
                                    if 'pitchData' not in pitchingDict:
                                        pitchingDict['pitchData'] = {
                                            'Dates': [],
                                            'Everyone': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0,'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0,'whiffs': 0, 'at bats': 0, 'hits': 0}},
                                            'Lefties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0,'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0,'whiffs': 0, 'at bats': 0, 'hits': 0}},
                                            'Righties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0,'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0,'whiffs': 0, 'at bats': 0, 'hits': 0}}}
                                    pDataDict = pitchingDict['pitchData']
                                    dates = pDataDict['Dates']
                                    everyone = pDataDict['Everyone']
                                    lefties = pDataDict['Lefties']
                                    righties = pDataDict['Righties']

                                    if game_date not in dates:
                                        other = getPitcherData(pitcherName,pitcherTeamAbbrev)  # having a separate getPitcherData() call that'll be used by testPitches helps avoid a weird counting error (still don't know why it happens)
                                        if pitcherName not in testPitches:
                                            testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'pitches': 0, 'data': other}

                                        testPitches[pitcherName]['pitches'] += 1
                                        vsEveryone()
                                        if hitterBatSide == 'Left':
                                            vsLeft()
                                        if hitterBatSide == 'Right':
                                            vsRight()
                                        addData(pitcherName, everyone, lefties, righties, pDataDict, content_dict, pitcherTeamAbbrev, dates)

    def vsEveryone():
        noSpinRate = False
        pitchData = pitch['pitchData']
        try:
            pitchType = pitch['details']['type']['description']
        except KeyError as e:
            print(pa)
            print(pitch)
            print("Suspected that there is no pitch type:", e)
            input("Unknown pitch type from " + pitcherName + " on " + game_date + " to " + hitterName + " in the " + inning)
        try:
            speed = pitchData['startSpeed']
        except KeyError as e:
            print(pitch)
            print("Suspected that there is no speed:", e)
            input(pitchType + " from " + pitcherName + " on " + game_date + " to " + hitterName + " in the " + inning)
        try:
            spinRate = pitchData['breaks']['spinRate']
        except KeyError as e:
            print(pitch)
            print("Suspected that there is no spin rate:", e)
            print(pitchType + " from " + pitcherName + " on " + game_date + " to " + hitterName + " in the " + inning)
            noSpinRate = True
        if noSpinRate == False:
            print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning, "to", hitterName, "("+str(testPitches[pitcherName]['pitches'])+")")

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

            if noSpinRate == True:
                spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                print("1. This will be the spinRate for the pitch: " + str(spinRate))
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
        speed = pitchData['startSpeed']
        pitchType = pitch['details']['type']['description']
        try:
            spinRate = pitchData['breaks']['spinRate']
        except KeyError as e:
            noSpinRate = True

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

            if noSpinRate == True:
                spinRate = int(round(lefties[pitchType]['spin'],
                                     0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                print("2. This will be the spinRate for the pitch: " + str(spinRate))
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
        speed = pitchData['startSpeed']
        pitchType = pitch['details']['type']['description']
        try:
            spinRate = pitchData['breaks']['spinRate']
        except KeyError as e:
            noSpinRate = True

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

            if noSpinRate == True:
                spinRate = int(round(righties[pitchType]['spin'],
                                     0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                print("3. This will be the spinRate for the pitch: " + str(spinRate))
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

    sched = statsapi.schedule(start_date='07/23/2020', end_date='09/27/2020',team=137)
    # sched = statsapi.schedule(start_date='07/24/2020',team=137)
    for i in range(len(sched)):
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

                if pitcherTeamAbbrev == 'SF':
                    content_dict = getPitcherData(pitcherName, pitcherTeamAbbrev)  # get pitcher's whole database dictionary
                    pitchingDict = content_dict[pitcherName]['pitching']
                    if 'pitchData' not in pitchingDict:
                        pitchingDict['pitchData'] = {
                            'Dates': [],
                            'Everyone': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}},
                            'Lefties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}},
                            'Righties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,'hits': 0}}}
                    pDataDict = pitchingDict['pitchData']
                    dates = pDataDict['Dates']
                    everyone = pDataDict['Everyone']
                    lefties = pDataDict['Lefties']
                    righties = pDataDict['Righties']

                    if game_date not in dates:
                        other = getPitcherData(pitcherName, pitcherTeamAbbrev)  # having a separate getPitcherData() call that'll be used by testPitches helps avoid a weird counting error (still don't know why it happens)
                        if pitcherName not in testPitches:
                            testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'pitches': 0, 'data': other}

                        resultOfPlay = pa['result']['event']
                        for pitch in playEvents:
                            if pitch['isPitch'] == True:
                                testPitches[pitcherName]['pitches'] += 1
                                vsEveryone()
                                if hitterBatSide == 'Left':
                                    vsLeft()
                                if hitterBatSide == 'Right':
                                    vsRight()
                                addData(pitcherName, everyone, lefties, righties, pitchingDict, content_dict, pitcherTeamAbbrev, dates)
                    else:
                        print("Already added for", pitcherName, "on", game_date)
            addDates(testPitches, game_date)
            checkPitchCount(testPitches, game)

def addDates(testPitches, game_date):
    listOfPitchers = list(testPitches.keys())
    for pitcher in listOfPitchers:
        pitcherTeam = testPitches[pitcher]['team']
        pitcherData = getPitcherData(pitcher, pitcherTeam)
        dates = pitcherData[pitcher]['pitching']['pitchData']['Dates']
        with open("Teams/" + pitcherTeam + "/" + "2020" + "/" + pitcher + ".txt", "w") as FILE:
            dates.append(game_date)
            FILE.write(str(pitcherData))

def addData(playername, everyone, lefties, righties, pitchingDict, content_dict, pitcherTeamAbbrev, dates):
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

    with open("Teams/" + pitcherTeamAbbrev + "/" + "2020" + "/" + playername + ".txt", "w") as FILE:
        pitchingDict['pitchData'] = everything # for some reason, trying to use pDataDict (the shortcut variable to get to the pitchData key) messes up the sorting of pitches by amount
        FILE.write(str(content_dict))

def checkPitchCount(testPitches, game):
    skip = False
    listOfPitchers = list(testPitches.keys())
    for p in range(len(listOfPitchers)):
        if not skip:
            pitcherName = listOfPitchers[p]
            pitcherId = testPitches[listOfPitchers[p]]['data'][listOfPitchers[p]]['ID']
            pitcherTeam = testPitches[listOfPitchers[p]]['team']
            testNumberOfPitches = testPitches[listOfPitchers[p]]['pitches']
            try:
                actualPitchesPerGame = game['liveData']['boxscore']['teams']['home']['players'][pitcherId]['stats']['pitching']['numberOfPitches']
            except KeyError:
                actualPitchesPerGame = game['liveData']['boxscore']['teams']['away']['players'][pitcherId]['stats']['pitching']['numberOfPitches']
            if actualPitchesPerGame != testNumberOfPitches:
                oldData = testPitches[pitcherName]['data']
                print("==============================================")
                pitchCountProblem(pitcherTeam, pitcherName, oldData)
                checkNextPitcher(testPitches, listOfPitchers, p, game, actualPitchesPerGame, testNumberOfPitches, pitcherName) # checks if the pitcher after also has incorrect pitch count (it would mean that he has a few of the previous pitcher's pitches) and restores his database if that's the case
                skip = True
            else:
                print("Looks good for " + listOfPitchers[p] + " with " + str(testNumberOfPitches) + " pitches")
        else:
            skip = False

def pitchCountProblem(pitcherTeamAbbrev, playername, oldData):
    with open("Teams/" + pitcherTeamAbbrev + "/" + "2020" + "/" + playername + ".txt", "w") as FILE:
        FILE.write(str(oldData))
    print("Restore for", playername,"should be succesful")

def checkNextPitcher(testPitches, listOfPitchers, p, game, actualPitchesPerGame, testNumberOfPitches, beforePitcherName):
    nextPitcherName = listOfPitchers[p+1]
    nextOldData = testPitches[listOfPitchers[p+1]]['data']
    nextPitcherId = testPitches[listOfPitchers[p+1]]['data'][listOfPitchers[p+1]]['ID']
    nextPitcherTeam = testPitches[listOfPitchers[p+1]]['team']
    nextTestNumberOfPitches = testPitches[listOfPitchers[p+1]]['pitches']
    try:
        nextActualPitchesPerGame = game['liveData']['boxscore']['teams']['home']['players'][nextPitcherId]['stats']['pitching']['numberOfPitches']
    except KeyError:
        nextActualPitchesPerGame = game['liveData']['boxscore']['teams']['away']['players'][nextPitcherId]['stats']['pitching']['numberOfPitches']

    if nextActualPitchesPerGame != nextTestNumberOfPitches:
        if (nextTestNumberOfPitches-nextActualPitchesPerGame) == (actualPitchesPerGame-testNumberOfPitches):
            pitchCountProblem(nextPitcherTeam, nextPitcherName, nextOldData)
            print("It looks like", nextPitcherName, "has", nextTestNumberOfPitches-nextActualPitchesPerGame, beforePitcherName, "pitches")
            input("Press Enter to Attempt to Fix The Issue \n==============================================\n")
            fixData(beforePitcherName, nextPitcherName, actualPitchesPerGame)

def fixData(firstPitcher, secondPitcher, actualPitchesPerGame):
    print("=========================================")
    print("Fixing...")
    print("=========================================")
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th",
                   10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th",
                   18: "18th"}

    def vsEveryone():
        noSpinRate = False
        pitchData = pitch['pitchData']
        speed = pitchData['startSpeed']
        pitchType = pitch['details']['type']['description']
        try:
            spinRate = pitchData['breaks']['spinRate']
        except KeyError as e:
            print(pitch)
            print("Suspected that there is no spin rate:", e)
            input(pitchType + " " + game_date + " " + hitterName + " " + inning)
            noSpinRate = True
        print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning, "to", hitterName, "("+str(testPitches[pitcherName]['pitches'])+")")

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

            if noSpinRate == True:
                spinRate = int(round(everyone[pitchType]['spin'],0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                input("This will be the spinRate for the pitch: " + str(spinRate))
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


            try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
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
        speed = pitchData['startSpeed']
        pitchType = pitch['details']['type']['description']
        try:
            spinRate = pitchData['breaks']['spinRate']
        except KeyError as e:
            print(pitch)
            print("Suspected that there is no spin rate:", e)
            input(pitchType + " " + game_date + " " + hitterName + " " + inning)
            noSpinRate = True

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

            if noSpinRate == True:
                spinRate = int(round(lefties[pitchType]['spin'],
                                     0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                input("This will be the spinRate for the pitch: " + str(spinRate))
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
        speed = pitchData['startSpeed']
        pitchType = pitch['details']['type']['description']
        try:
            spinRate = pitchData['breaks']['spinRate']
        except KeyError as e:
            print(pitch)
            # print("Suspected that there is no spin rate:", e)
            input(pitchType + " " + game_date + " " + hitterName + " " + inning)
            noSpinRate = True

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

            if noSpinRate == True:
                spinRate = int(round(righties[pitchType]['spin'],
                                     0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                input("This will be the spinRate for the pitch: " + str(spinRate))
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

    sched = statsapi.schedule(start_date='08/01/2020', team=137)
    for i in range(len(sched)):
        testPitches = {}  # this dictionary will be used to keep track of pitches thrown for each pitcher in the game and will log the pitcher's previous file just in case pitch counts don't match
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

                if pitcherName == firstPitcher:
                    content_dict = getPitcherData(pitcherName,pitcherTeamAbbrev)  # get pitcher's whole database dictionary
                    pitchingDict = content_dict[pitcherName]['pitching']
                    if 'pitchData' not in pitchingDict:
                        pitchingDict['pitchData'] = {
                            'Dates': [],
                            'Everyone': {
                                'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,
                                                'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,
                                                'hits': 0}},
                            'Lefties': {
                                'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,
                                                'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,
                                                'hits': 0}},
                            'Righties': {
                                'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0,
                                                'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0,
                                                'hits': 0}}}
                    pDataDict = pitchingDict['pitchData']
                    dates = pDataDict['Dates']
                    everyone = pDataDict['Everyone']
                    lefties = pDataDict['Lefties']
                    righties = pDataDict['Righties']

                    if game_date not in dates:
                        other = getPitcherData(pitcherName,
                                               pitcherTeamAbbrev)  # having a separate getPitcherData() call that'll be used by testPitches helps avoid a weird counting error (still don't know why it happens)
                        if pitcherName not in testPitches:
                            testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'pitches': 0, 'data': other}

                        resultOfPlay = pa['result']['event']
                        for pitch in playEvents:
                            if pitch['isPitch'] == True:
                                testPitches[pitcherName]['pitches'] += 1
                                vsEveryone()
                                if hitterBatSide == 'Left':
                                    vsLeft()
                                if hitterBatSide == 'Right':
                                    vsRight()
                                addData(pitcherName, everyone, lefties, righties, pDataDict, content_dict, pitcherTeamAbbrev, dates)
                if pitcherName == secondPitcher:
                    resultOfPlay = pa['result']['event']
                    for pitch in playEvents:
                        if pitch['isPitch'] == True:

                            if len(testPitches) > 0: # testPitches would be empty if date was already added for the first pitcher, so this prevents a KeyError
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
                                        'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0,
                                                        'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0,
                                                        'whiffs': 0, 'at bats': 0, 'hits': 0}},
                                    'Lefties': {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0,
                                                                'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0,
                                                                'whiffs': 0, 'at bats': 0, 'hits': 0}},
                                    'Righties': {
                                        'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0,
                                                        'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0,
                                                        'whiffs': 0, 'at bats': 0, 'hits': 0}}}
                            pDataDict = pitchingDict['pitchData']
                            dates = pDataDict['Dates']
                            everyone = pDataDict['Everyone']
                            lefties = pDataDict['Lefties']
                            righties = pDataDict['Righties']

                            if game_date not in dates:
                                other = getPitcherData(pitcherName, pitcherTeamAbbrev)  # having a separate getPitcherData() call that'll be used by testPitches helps avoid a weird counting error (still don't know why it happens)
                                if pitcherName not in testPitches:
                                    testPitches[pitcherName] = {'team': pitcherTeamAbbrev, 'pitches': 0,'data': other}

                                testPitches[pitcherName]['pitches'] += 1
                                vsEveryone()
                                if hitterBatSide == 'Left':
                                    vsLeft()
                                if hitterBatSide == 'Right':
                                    vsRight()
                                addData(pitcherName, everyone, lefties, righties, pDataDict, content_dict,pitcherTeamAbbrev, dates)
            addDates(testPitches, game_date)
            checkPitchCount(testPitches, game)

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

analyzePitchData()
# allPitchData()
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

