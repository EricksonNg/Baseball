import statsapi
import operator
import time

startTime = time.time()

def zoneExitVeloAndAverage():
    # On 7/29/2020, only Mike Yastrzemski (the last batter of the game) has the batterHotColdZoneStats key for his walk-off home run
    sched = statsapi.schedule(start_date='07/29/2020', team=137)
    for i in range(len(sched)):
        gameId = sched[i]["game_id"]
        game_date = sched[i]["game_date"]
        game_result = sched[i]["summary"]
        game_status = sched[i]["status"]
        game = statsapi.get('game', {'gamePk': gameId})

        allPlays = game['liveData']['plays']['allPlays']
        play = -1
        if game_status != 'Postponed':
            for thing in allPlays[play]:
                print(thing, allPlays[play][thing])
            hotCold = allPlays[play]['matchup']['batterHotColdZoneStats']['stats'][0]
            splits = hotCold['splits']
            exitVeloZones = splits[0]['stat']['zones']
            battingAverageZones = splits[0]['stat']['zones']
            for item in exitVeloZones:
                print(item)
            for item in battingAverageZones:
                print(item)

def spinAndSpeed():
    kind = []
    amount = {}
    spin = {}
    mph = {}
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th",
                   11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}

    sched = statsapi.schedule(start_date='07/29/2020', team=137)
    for i in range(len(sched)):
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
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                for pitch in playEvents:
                    print(pitch)
                    # if pitcherName == 'Kevin Gausman':
                    try:
                        pitchData = pitch['pitchData']
                        speed = pitchData['startSpeed']
                        pitchType = pitch['details']['type']['description']
                        spinRate = pitchData['breaks']['spinRate']
                        print(spinRate, speed, "MPH", pitchType, "by", pitcherName, "on", game_date, "in the", inning,
                              "to",
                              hitterName)
                        if pitchType not in kind:
                            kind.append(pitchType)
                            amount[pitchType] = 1
                            spin[pitchType] = spinRate
                            mph[pitchType] = speed
                        else:
                            amount[pitchType] += 1
                            spin[pitchType] += spinRate
                            mph[pitchType] += speed
                    except KeyError:
                        try:
                            print(pitch['details']['description'])
                        except KeyError:
                            if pitch['isPitch'] == False:
                                pass
                            else:
                                input("Something is off here: " + pitch)
    for type in kind:
        spinAVG = round(spin[type] / amount[type], 2)
        mphAVG = round(mph[type] / amount[type], 2)
        print(type, "averages", mphAVG, "MPH and", spinAVG, "RPM")

def pitchTypePerPitcher():
    kind = []
    amount = {}
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th",
                   11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}

    sched = statsapi.schedule(start_date='07/23/2020', end_date='09/27/2020', team=137)
    for i in range(len(sched)):
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
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                if pitcherName == 'Kevin Gausman':
                    for pitch in playEvents:
                        try:
                            pitchData = pitch['pitchData']
                            speed = pitchData['startSpeed']
                            pitchType = pitch['details']['type']['description']
                            spinRate = pitchData['breaks']['spinRate']
                            print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date,
                                  "in the", inning, "to", hitterName)
                            if pitchType not in kind:
                                kind.append(pitchType)
                                amount[pitchType] = 1
                            else:
                                amount[pitchType] += 1
                        except KeyError:
                            try:
                                print(pitch['details']['description'])
                            except KeyError:
                                if pitch['isPitch'] == False:
                                    pass
                                else:
                                    input("Something is off here: " + pitch)

    sortedAmount = sorted(amount.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedAmount)
    sortedDict = {pitch: amount for pitch, amount in sortedAmount}
    print(sortedDict)

def allPitchData():
    kind = []
    leftKind = []
    rightKind = []
    numbers = {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0, 'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}}
    leftNumbers = {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0,'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}}
    rightNumbers = {'All Pitches': {'amount': 0, 'allSpin': 0, 'allSpeed': 0,'spin': 0, 'speed': 0, 'fastest': 0, 'slowest': 0, 'swings': 0, 'whiffs': 0, 'at bats': 0, 'hits': 0}}
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th",
                   11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}

    def everyone(testPitchesPerGame):
        noSpinRate = False
        if pitch['isPitch'] == True:
            testPitchesPerGame += 1
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
            print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning,
                  "to", hitterName)

            if pitchType not in kind:

                kind.append(pitchType)
                numbers[pitchType] = {}
                numbers[pitchType]['amount'] = 1
                numbers['All Pitches']['amount'] += 1
                numbers[pitchType]['allSpin'] = spinRate
                numbers[pitchType]['allSpeed'] = speed
                numbers[pitchType]['spin'] = spinRate
                numbers[pitchType]['speed'] = speed
                numbers['All Pitches']['allSpin'] += spinRate
                numbers['All Pitches']['allSpeed'] = round(numbers['All Pitches']['allSpeed'] + speed, 1)
                numbers['All Pitches']['spin'] = round((numbers['All Pitches']['allSpin']) / (numbers['All Pitches']['amount']), 2)
                numbers['All Pitches']['speed'] = round((numbers['All Pitches']['allSpeed']) / (numbers['All Pitches']['amount']), 2)

                if speed > numbers['All Pitches']['fastest']:
                    numbers['All Pitches']['fastest'] = speed
                numbers[pitchType]['fastest'] = speed

                if numbers['All Pitches']['slowest'] != 0:
                    if speed < numbers['All Pitches']['slowest']:
                        numbers['All Pitches']['slowest'] = speed
                else:
                    numbers['All Pitches']['slowest'] = speed
                numbers[pitchType]['slowest'] = speed

                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    numbers[pitchType]['swings'] = 1
                    numbers[pitchType]['whiffs'] = 1
                    numbers['All Pitches']['swings'] += 1
                    numbers['All Pitches']['whiffs'] += 1
                    # print("1. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    numbers[pitchType]['swings'] = 1
                    numbers[pitchType]['whiffs'] = 0
                    numbers['All Pitches']['swings'] += 1
                    numbers['All Pitches']['whiffs'] += 0
                    # print("2. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        hitData = pitch['hitData']
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            numbers[pitchType]['at bats'] = 1
                            numbers[pitchType]['hits'] = 1
                            numbers['All Pitches']['at bats'] += 1
                            numbers['All Pitches']['hits'] += 1
                        else:
                            numbers[pitchType]['at bats'] = 1
                            numbers[pitchType]['hits'] = 0
                            numbers['All Pitches']['at bats'] += 1
                            numbers['All Pitches']['hits'] += 0

            else:  # If pitch has never been thrown yet
                numbers[pitchType]['amount'] += 1
                numbers['All Pitches']['amount'] += 1

                if noSpinRate == True:
                    spinRate = int(round(numbers[pitchType]['spin'],
                                         0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                    input("This will be the spinRate for the pitch: " + str(spinRate))
                numbers[pitchType]['allSpin'] += spinRate
                numbers[pitchType]['allSpeed'] = round(numbers[pitchType]['allSpeed'] + speed, 1)
                numbers[pitchType]['spin'] = round((numbers[pitchType]['allSpin']) / (numbers[pitchType]['amount']), 2)
                numbers[pitchType]['speed'] = round((numbers[pitchType]['allSpeed']) / (numbers[pitchType]['amount']),
                                                    2)
                numbers['All Pitches']['allSpin'] += spinRate
                numbers['All Pitches']['allSpeed'] = round(numbers['All Pitches']['allSpeed'] + speed, 1)
                numbers['All Pitches']['spin'] = round(
                    (numbers['All Pitches']['allSpin']) / (numbers['All Pitches']['amount']), 2)
                numbers['All Pitches']['speed'] = round(
                    (numbers['All Pitches']['allSpeed']) / (numbers['All Pitches']['amount']), 2)

                if speed > numbers['All Pitches']['fastest']:
                    numbers['All Pitches']['fastest'] = speed
                if speed > numbers[pitchType]['fastest']:
                    numbers[pitchType]['fastest'] = speed
                if numbers['All Pitches']['slowest'] != 0:
                    if speed < numbers['All Pitches']['slowest']:
                        numbers['All Pitches']['slowest'] = speed
                else:
                    numbers['All Pitches']['slowest'] = speed
                if numbers[pitchType]['slowest'] != 0:
                    if speed < numbers[pitchType]['slowest']:
                        numbers[pitchType]['slowest'] = speed


                try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
                    # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                    callDescription = pitch['details']['description']
                    ballIsInPlay = pitch['details']['isInPlay']
                    if 'Swinging Strike' in callDescription:
                        numbers[pitchType]['swings'] += 1
                        numbers[pitchType]['whiffs'] += 1
                        numbers['All Pitches']['swings'] += 1
                        numbers['All Pitches']['whiffs'] += 1
                        # print("3. Swing and a miss by", hitterName)
                    elif 'Foul' in callDescription or ballIsInPlay:
                        numbers[pitchType]['swings'] += 1
                        numbers[pitchType]['whiffs'] += 0
                        numbers['All Pitches']['swings'] += 1
                        numbers['All Pitches']['whiffs'] += 0
                        # print("4. Some kind of contact by", hitterName)
                        if ballIsInPlay:
                            try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                                if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                    numbers[pitchType]['at bats'] += 1
                                    numbers[pitchType]['hits'] += 1
                                    numbers['All Pitches']['at bats'] += 1
                                    numbers['All Pitches']['hits'] += 1
                                else:
                                    numbers[pitchType]['at bats'] += 1
                                    numbers[pitchType]['hits'] += 0
                                    numbers['All Pitches']['at bats'] += 1
                                    numbers['All Pitches']['hits'] += 0
                            except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                                if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                    numbers[pitchType]['at bats'] = 1
                                    numbers[pitchType]['hits'] = 1
                                    numbers['All Pitches']['at bats'] += 1
                                    numbers['All Pitches']['hits'] += 0
                                else:
                                    numbers[pitchType]['at bats'] = 1
                                    numbers[pitchType]['hits'] = 0
                                    numbers['All Pitches']['at bats'] += 1
                                    numbers['All Pitches']['hits'] += 0

                except KeyError:
                    # everything below until the end of the if statement calculates swings and whiffs
                    callDescription = pitch['details']['description']
                    ballIsInPlay = pitch['details']['isInPlay']
                    if 'Swinging Strike' in callDescription:
                        numbers[pitchType]['swings'] = 1
                        numbers[pitchType]['whiffs'] = 1
                        numbers['All Pitches']['swings'] += 1
                        numbers['All Pitches']['whiffs'] += 1
                        # print("5. Swing and a miss by", hitterName)
                    elif 'Foul' in callDescription or ballIsInPlay:
                        numbers[pitchType]['swings'] = 1
                        numbers[pitchType]['whiffs'] = 0
                        numbers['All Pitches']['swings'] += 1
                        numbers['All Pitches']['whiffs'] += 0
                        # print("6. Some kind of contact by", hitterName)
                        if ballIsInPlay:
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                numbers[pitchType]['at bats'] = 1
                                numbers[pitchType]['hits'] = 1
                                numbers['All Pitches']['at bats'] += 1
                                numbers['All Pitches']['hits'] += 1
                            else:
                                numbers[pitchType]['at bats'] = 1
                                numbers[pitchType]['hits'] = 0
                                numbers['All Pitches']['at bats'] += 1
                                numbers['All Pitches']['hits'] += 0

    def vsLeft(testPitchesPerGame):
        noSpinRate = False
        if pitch['isPitch'] == True:
            testPitchesPerGame += 1
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
            print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning,
                  "to", hitterName)

            if pitchType not in leftKind:

                leftKind.append(pitchType)
                leftNumbers[pitchType] = {}
                leftNumbers[pitchType]['amount'] = 1
                leftNumbers['All Pitches']['amount'] += 1
                leftNumbers[pitchType]['allSpin'] = spinRate
                leftNumbers[pitchType]['allSpeed'] = speed
                leftNumbers[pitchType]['spin'] = spinRate
                leftNumbers[pitchType]['speed'] = speed
                leftNumbers['All Pitches']['allSpin'] += spinRate
                leftNumbers['All Pitches']['allSpeed'] = round(leftNumbers['All Pitches']['allSpeed'] + speed, 1)
                leftNumbers['All Pitches']['spin'] = round(
                    (leftNumbers['All Pitches']['allSpin']) / (leftNumbers['All Pitches']['amount']), 2)
                leftNumbers['All Pitches']['speed'] = round(
                    (leftNumbers['All Pitches']['allSpeed']) / (leftNumbers['All Pitches']['amount']), 2)

                if speed > leftNumbers['All Pitches']['fastest']:
                    rightNumbers['All Pitches']['fastest'] = speed
                leftNumbers[pitchType]['fastest'] = speed

                if leftNumbers['All Pitches']['slowest'] != 0:
                    if speed < leftNumbers['All Pitches']['slowest']:
                        leftNumbers['All Pitches']['slowest'] = speed
                else:
                    leftNumbers['All Pitches']['slowest'] = speed
                leftNumbers[pitchType]['slowest'] = speed

                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    leftNumbers[pitchType]['swings'] = 1
                    leftNumbers[pitchType]['whiffs'] = 1
                    leftNumbers['All Pitches']['swings'] += 1
                    leftNumbers['All Pitches']['whiffs'] += 1
                    # print("1. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    leftNumbers[pitchType]['swings'] = 1
                    leftNumbers[pitchType]['whiffs'] = 0
                    leftNumbers['All Pitches']['swings'] += 1
                    leftNumbers['All Pitches']['whiffs'] += 0
                    # print("2. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        hitData = pitch['hitData']
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            leftNumbers[pitchType]['at bats'] = 1
                            leftNumbers[pitchType]['hits'] = 1
                            leftNumbers['All Pitches']['at bats'] += 1
                            leftNumbers['All Pitches']['hits'] += 1
                        else:
                            leftNumbers[pitchType]['at bats'] = 1
                            leftNumbers[pitchType]['hits'] = 0
                            leftNumbers['All Pitches']['at bats'] += 1
                            leftNumbers['All Pitches']['hits'] += 0

            else:  # If pitch has never been thrown yet
                leftNumbers[pitchType]['amount'] += 1
                leftNumbers['All Pitches']['amount'] += 1

                if noSpinRate == True:
                    spinRate = int(round(leftNumbers[pitchType]['spin'],
                                         0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                    input("This will be the spinRate for the pitch: " + str(spinRate))
                leftNumbers[pitchType]['allSpin'] += spinRate
                leftNumbers[pitchType]['allSpeed'] = round(leftNumbers[pitchType]['allSpeed'] + speed, 1)
                leftNumbers[pitchType]['spin'] = round((leftNumbers[pitchType]['allSpin']) / (leftNumbers[pitchType]['amount']), 2)
                leftNumbers[pitchType]['speed'] = round((leftNumbers[pitchType]['allSpeed']) / (leftNumbers[pitchType]['amount']),
                                                    2)
                leftNumbers['All Pitches']['allSpin'] += spinRate
                leftNumbers['All Pitches']['allSpeed'] = round(leftNumbers['All Pitches']['allSpeed'] + speed, 1)
                leftNumbers['All Pitches']['spin'] = round(
                    (leftNumbers['All Pitches']['allSpin']) / (leftNumbers['All Pitches']['amount']), 2)
                leftNumbers['All Pitches']['speed'] = round(
                    (leftNumbers['All Pitches']['allSpeed']) / (leftNumbers['All Pitches']['amount']), 2)

                if speed > leftNumbers['All Pitches']['fastest']:
                    leftNumbers['All Pitches']['fastest'] = speed
                if speed > leftNumbers[pitchType]['fastest']:
                    leftNumbers[pitchType]['fastest'] = speed
                if leftNumbers['All Pitches']['slowest'] != 0:
                    if speed < leftNumbers['All Pitches']['slowest']:
                        leftNumbers['All Pitches']['slowest'] = speed
                else:
                    leftNumbers['All Pitches']['slowest'] = speed
                if leftNumbers[pitchType]['slowest'] != 0:
                    if speed < leftNumbers[pitchType]['slowest']:
                        leftNumbers[pitchType]['slowest'] = speed

                try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
                    # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                    callDescription = pitch['details']['description']
                    ballIsInPlay = pitch['details']['isInPlay']
                    if 'Swinging Strike' in callDescription:
                        leftNumbers[pitchType]['swings'] += 1
                        leftNumbers[pitchType]['whiffs'] += 1
                        leftNumbers['All Pitches']['swings'] += 1
                        leftNumbers['All Pitches']['whiffs'] += 1
                        # print("3. Swing and a miss by", hitterName)
                    elif 'Foul' in callDescription or ballIsInPlay:
                        leftNumbers[pitchType]['swings'] += 1
                        leftNumbers[pitchType]['whiffs'] += 0
                        leftNumbers['All Pitches']['swings'] += 1
                        leftNumbers['All Pitches']['whiffs'] += 0
                        # print("4. Some kind of contact by", hitterName)
                        if ballIsInPlay:
                            try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                                if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                    leftNumbers[pitchType]['at bats'] += 1
                                    leftNumbers[pitchType]['hits'] += 1
                                    leftNumbers['All Pitches']['at bats'] += 1
                                    leftNumbers['All Pitches']['hits'] += 1
                                else:
                                    leftNumbers[pitchType]['at bats'] += 1
                                    leftNumbers[pitchType]['hits'] += 0
                                    leftNumbers['All Pitches']['at bats'] += 1
                                    leftNumbers['All Pitches']['hits'] += 0
                            except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                                if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                    leftNumbers[pitchType]['at bats'] = 1
                                    leftNumbers[pitchType]['hits'] = 1
                                    leftNumbers['All Pitches']['at bats'] += 1
                                    leftNumbers['All Pitches']['hits'] += 0
                                else:
                                    leftNumbers[pitchType]['at bats'] = 1
                                    leftNumbers[pitchType]['hits'] = 0
                                    leftNumbers['All Pitches']['at bats'] += 1
                                    leftNumbers['All Pitches']['hits'] += 0

                except KeyError:
                    # everything below until the end of the if statement calculates swings and whiffs
                    callDescription = pitch['details']['description']
                    ballIsInPlay = pitch['details']['isInPlay']
                    if 'Swinging Strike' in callDescription:
                        leftNumbers[pitchType]['swings'] = 1
                        leftNumbers[pitchType]['whiffs'] = 1
                        leftNumbers['All Pitches']['swings'] += 1
                        leftNumbers['All Pitches']['whiffs'] += 1
                        # print("5. Swing and a miss by", hitterName)
                    elif 'Foul' in callDescription or ballIsInPlay:
                        leftNumbers[pitchType]['swings'] = 1
                        leftNumbers[pitchType]['whiffs'] = 0
                        leftNumbers['All Pitches']['swings'] += 1
                        leftNumbers['All Pitches']['whiffs'] += 0

                        if ballIsInPlay:
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                leftNumbers[pitchType]['at bats'] = 1
                                leftNumbers[pitchType]['hits'] = 1
                                leftNumbers['All Pitches']['at bats'] += 1
                                leftNumbers['All Pitches']['hits'] += 1
                            else:
                                leftNumbers[pitchType]['at bats'] = 1
                                leftNumbers[pitchType]['hits'] = 0
                                leftNumbers['All Pitches']['at bats'] += 1
                                leftNumbers['All Pitches']['hits'] += 0

    def vsRight(testPitchesPerGame):
        noSpinRate = False
        if pitch['isPitch'] == True:
            testPitchesPerGame += 1
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
            print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning,
                  "to", hitterName)

            if pitchType not in rightKind:

                rightKind.append(pitchType)
                rightNumbers[pitchType] = {}
                rightNumbers[pitchType]['amount'] = 1
                rightNumbers['All Pitches']['amount'] += 1
                rightNumbers[pitchType]['allSpin'] = spinRate
                rightNumbers[pitchType]['allSpeed'] = speed
                rightNumbers[pitchType]['spin'] = spinRate
                rightNumbers[pitchType]['speed'] = speed
                rightNumbers['All Pitches']['allSpin'] += spinRate
                rightNumbers['All Pitches']['allSpeed'] = round(rightNumbers['All Pitches']['allSpeed'] + speed, 1)
                rightNumbers['All Pitches']['spin'] = round(
                    (rightNumbers['All Pitches']['allSpin']) / (rightNumbers['All Pitches']['amount']), 2)
                rightNumbers['All Pitches']['speed'] = round(
                    (rightNumbers['All Pitches']['allSpeed']) / (rightNumbers['All Pitches']['amount']), 2)

                if speed > rightNumbers['All Pitches']['fastest']:
                    rightNumbers['All Pitches']['fastest'] = speed
                rightNumbers[pitchType]['fastest'] = speed

                if rightNumbers['All Pitches']['slowest'] != 0:
                    if speed < rightNumbers['All Pitches']['slowest']:
                        rightNumbers['All Pitches']['slowest'] = speed
                else:
                    rightNumbers['All Pitches']['slowest'] = speed
                rightNumbers[pitchType]['slowest'] = speed

                # everything below until the end of the if statement calculates swings and whiffs
                callDescription = pitch['details']['description']
                ballIsInPlay = pitch['details']['isInPlay']
                if 'Swinging Strike' in callDescription:
                    rightNumbers[pitchType]['swings'] = 1
                    rightNumbers[pitchType]['whiffs'] = 1
                    rightNumbers['All Pitches']['swings'] += 1
                    rightNumbers['All Pitches']['whiffs'] += 1
                    print("1. Swing and a miss by", hitterName)
                elif 'Foul' in callDescription or ballIsInPlay:
                    rightNumbers[pitchType]['swings'] = 1
                    rightNumbers[pitchType]['whiffs'] = 0
                    rightNumbers['All Pitches']['swings'] += 1
                    rightNumbers['All Pitches']['whiffs'] += 0
                    # print("2. Some kind of contact by", hitterName)
                    if ballIsInPlay:
                        hitData = pitch['hitData']
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            rightNumbers[pitchType]['at bats'] = 1
                            rightNumbers[pitchType]['hits'] = 1
                            rightNumbers['All Pitches']['at bats'] += 1
                            rightNumbers['All Pitches']['hits'] += 1
                        else:
                            rightNumbers[pitchType]['at bats'] = 1
                            rightNumbers[pitchType]['hits'] = 0
                            rightNumbers['All Pitches']['at bats'] += 1
                            rightNumbers['All Pitches']['hits'] += 0

            else:  # If pitch has never been thrown yet
                rightNumbers[pitchType]['amount'] += 1
                rightNumbers['All Pitches']['amount'] += 1

                if noSpinRate == True:
                    spinRate = int(round(rightNumbers[pitchType]['spin'],
                                         0))  # If there's no spin rate data on a specific pitch (hopefully it's a rare occasion), then the spin rate for that pitch will be the previous average spin rate of that pitch
                    input("This will be the spinRate for the pitch: " + str(spinRate))
                rightNumbers[pitchType]['allSpin'] += spinRate
                rightNumbers[pitchType]['allSpeed'] = round(rightNumbers[pitchType]['allSpeed'] + speed, 1)
                rightNumbers[pitchType]['spin'] = round((rightNumbers[pitchType]['allSpin']) / (rightNumbers[pitchType]['amount']), 2)
                rightNumbers[pitchType]['speed'] = round((rightNumbers[pitchType]['allSpeed']) / (rightNumbers[pitchType]['amount']),
                                                    2)
                rightNumbers['All Pitches']['allSpin'] += spinRate
                rightNumbers['All Pitches']['allSpeed'] = round(rightNumbers['All Pitches']['allSpeed'] + speed, 1)
                rightNumbers['All Pitches']['spin'] = round(
                    (rightNumbers['All Pitches']['allSpin']) / (rightNumbers['All Pitches']['amount']), 2)
                rightNumbers['All Pitches']['speed'] = round(
                    (rightNumbers['All Pitches']['allSpeed']) / (rightNumbers['All Pitches']['amount']), 2)

                if speed > rightNumbers['All Pitches']['fastest']:
                    rightNumbers['All Pitches']['fastest'] = speed
                if speed > rightNumbers[pitchType]['fastest']:
                    rightNumbers[pitchType]['fastest'] = speed
                if rightNumbers['All Pitches']['slowest'] != 0:
                    if speed < rightNumbers['All Pitches']['slowest']:
                        rightNumbers['All Pitches']['slowest'] = speed
                else:
                    rightNumbers['All Pitches']['slowest'] = speed
                if rightNumbers[pitchType]['slowest'] != 0:
                    if speed < rightNumbers[pitchType]['slowest']:
                        rightNumbers[pitchType]['slowest'] = speed

                try:  # Key Error will happen because key is initially added only if the first pitch the pitcher threw of that kind is swung at (so if the first kind of that pitch isn't swung at, the keys is never actually created, so the except creates the keys)
                    # everything below until the end of the if statement calculates swings and whiffs (but this time it looks for the swing and whiff values already in the dictionary)
                    callDescription = pitch['details']['description']
                    ballIsInPlay = pitch['details']['isInPlay']
                    if 'Swinging Strike' in callDescription:
                        rightNumbers[pitchType]['swings'] += 1
                        rightNumbers[pitchType]['whiffs'] += 1
                        rightNumbers['All Pitches']['swings'] += 1
                        rightNumbers['All Pitches']['whiffs'] += 1
                        # print("3. Swing and a miss by", hitterName)
                    elif 'Foul' in callDescription or ballIsInPlay:
                        rightNumbers[pitchType]['swings'] += 1
                        rightNumbers[pitchType]['whiffs'] += 0
                        rightNumbers['All Pitches']['swings'] += 1
                        rightNumbers['All Pitches']['whiffs'] += 0
                        # print("4. Some kind of contact by", hitterName)
                        if ballIsInPlay:
                            try:  # If the try and except isn't here, it could result in an incorrect swings count because an unexcepted KeyError will add another swing after a swing was already added (see 2nd KeyError down)
                                if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                    rightNumbers[pitchType]['at bats'] += 1
                                    rightNumbers[pitchType]['hits'] += 1
                                    rightNumbers['All Pitches']['at bats'] += 1
                                    rightNumbers['All Pitches']['hits'] += 1
                                else:
                                    rightNumbers[pitchType]['at bats'] += 1
                                    rightNumbers[pitchType]['hits'] += 0
                                    rightNumbers['All Pitches']['at bats'] += 1
                                    rightNumbers['All Pitches']['hits'] += 0
                            except KeyError:  # For if the 'at bats' and 'hits' key aren't created yet (this situation is entirely possible if the pitch has already been thrown once before without a hit off of it and there's a foul or an out made on the pitch before a hit off the pitch is recorded)
                                if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                    rightNumbers[pitchType]['at bats'] = 1
                                    rightNumbers[pitchType]['hits'] = 1
                                    rightNumbers['All Pitches']['at bats'] += 1
                                    rightNumbers['All Pitches']['hits'] += 0
                                else:
                                    rightNumbers[pitchType]['at bats'] = 1
                                    rightNumbers[pitchType]['hits'] = 0
                                    rightNumbers['All Pitches']['at bats'] += 1
                                    rightNumbers['All Pitches']['hits'] += 0

                except KeyError:
                    # everything below until the end of the if statement calculates swings and whiffs
                    callDescription = pitch['details']['description']
                    ballIsInPlay = pitch['details']['isInPlay']
                    if 'Swinging Strike' in callDescription:
                        rightNumbers[pitchType]['swings'] = 1
                        rightNumbers[pitchType]['whiffs'] = 1
                        rightNumbers['All Pitches']['swings'] += 1
                        rightNumbers['All Pitches']['whiffs'] += 1
                        # print("5. Swing and a miss by", hitterName)
                    elif 'Foul' in callDescription or ballIsInPlay:
                        rightNumbers[pitchType]['swings'] = 1
                        rightNumbers[pitchType]['whiffs'] = 0
                        rightNumbers['All Pitches']['swings'] += 1
                        rightNumbers['All Pitches']['whiffs'] += 0
                        # print("6. Some kind of contact by", hitterName)
                        if ballIsInPlay:
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                rightNumbers[pitchType]['at bats'] = 1
                                rightNumbers[pitchType]['hits'] = 1
                                rightNumbers['All Pitches']['at bats'] += 1
                                rightNumbers['All Pitches']['hits'] += 1
                            else:
                                rightNumbers[pitchType]['at bats'] = 1
                                rightNumbers[pitchType]['hits'] = 0
                                rightNumbers['All Pitches']['at bats'] += 1
                                rightNumbers['All Pitches']['hits'] += 0

    sched = statsapi.schedule(start_date='07/23/2020', end_date = '09/27/2020',team=137)
    for i in range(len(sched)):
        testPitchesPerGame = 0
        didPitch = False
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
                hitterName = pa['matchup']['batter']['fullName']
                hitterBatSide = pa['matchup']['batSide']['description']
                playEvents = pa['playEvents']
                if pitcherName == 'Kevin Gausman':
                    resultOfPlay = pa['result']['event']
                    didPitch = True
                    for pitch in playEvents:
                        everyone(testPitchesPerGame)
                        if hitterBatSide == 'Left':
                            vsLeft(testPitchesPerGame)
                        if hitterBatSide == 'Right':
                            vsRight(testPitchesPerGame)


            # if didPitch:
            #     try:
            #         actualPitchesPerGame = game['liveData']['boxscore']['teams']['home']['players']['ID456501']['stats']['pitching']['numberOfPitches']
            #     except KeyError:
            #         actualPitchesPerGame = game['liveData']['boxscore']['teams']['away']['players']['ID456501']['stats']['pitching']['numberOfPitches']
            #     if actualPitchesPerGame != testPitchesPerGame:
            #         print("=============================")
            #         print("Actual", actualPitchesPerGame)
            #         print("Test", testPitchesPerGame)
            #         input("We have a pitch count problem \n=============================\n")

    temp = {}
    leftTemp = {}
    rightTemp = {}
    newNumbers = {}
    newLeftNumbers = {}
    newRightNumbers = {}

    everything = {}

    # For everyone
    for pitch in numbers:
        temp[pitch] = numbers[pitch]['amount']
    sortedTemp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in sortedTemp:
        newNumbers[tuple[0]] = {}
        typeOfPitch = newNumbers[tuple[0]]
        for type in numbers[tuple[0]]:
            typeOfPitch[type] = numbers[tuple[0]][type]

    # For lefties
    for pitch in leftNumbers:
        leftTemp[pitch] = leftNumbers[pitch]['amount']
    leftSortedTemp = sorted(leftTemp.items(), key=operator.itemgetter(1), reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in leftSortedTemp:
        newLeftNumbers[tuple[0]] = {}
        typeOfPitch = newLeftNumbers[tuple[0]]
        for type in leftNumbers[tuple[0]]:
            typeOfPitch[type] = leftNumbers[tuple[0]][type]

    # For righties
    for pitch in rightNumbers:
        rightTemp[pitch] = rightNumbers[pitch]['amount']
    rightSortedTemp = sorted(rightTemp.items(), key=operator.itemgetter(1), reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in rightSortedTemp:
        newRightNumbers[tuple[0]] = {}
        typeOfPitch = newRightNumbers[tuple[0]]
        for type in rightNumbers[tuple[0]]:
            typeOfPitch[type] = rightNumbers[tuple[0]][type]

    list = []
    list2 = []

    everything['Everyone'] = newNumbers
    everything['Lefties'] = newLeftNumbers
    everything['Righties'] = newRightNumbers

    with open("Teams/" + "SF" + "/" + "2020" + "/Kevin Gausman.txt", "r") as FILE:
        content = FILE.read()
        try:
            content_dict = eval(content)
        except Exception as e:
            print("We got an error ", e)
            print("Database Error ")
    with open("Teams/" + "SF" + "/" + "2020" + "/Kevin Gausman.txt", "w") as FILE:
        content_dict['Kevin Gausman']['pitching']['pitchData'] = everything
        FILE.write(str(content_dict))

# allPitchData()

def hitData():
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}
    groundBalls = 0
    flyBalls = 0
    popUps = 0
    lineDrives = 0

    optimal = 0

    cords = []

    def trajectoryCalculation(groundBalls, lineDrives, flyBalls, popUps):
        # all variables have to be declared outside of the loop
        if hitData['trajectory'] == 'ground_ball':
            groundBalls += 1
        if hitData['trajectory'] == 'line_drive':
            lineDrives += 1
        if hitData['trajectory'] == 'fly_ball':
            flyBalls += 1
        if hitData['trajectory'] == 'popup':
            popUps += 1

    def hardnessCalculation(soft, medium, hard):
        # all variables have to be declared outside of the loop
        if hitData['hardness'] == 'soft':
            soft += 1
        if hitData['hardness'] == 'medium':
            medium += 1
        if hitData['hardness'] == 'hard':
            hard += 1

    def optimalContact(hitData, optimal, pa):
        if hitData['launchSpeed'] > 95 and (hitData['launchAngle'] > 25 and hitData['launchAngle'] < 35):
            optimal += 1
            print(pa['result']['event'], hitData)

    sched = statsapi.schedule(start_date='07/23/2020', end_date='09/27/2020', team=137)
    for i in range(len(sched)):
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
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                if hitterName == 'Mike Yastrzemski':
                    for pitch in playEvents:
                        if 'In play' in pitch['details']['description']: # Using the 'isInPlay' boolean value in pitch is also an option, but game advisories don't have the key, so using ['details']['description'] is much simpler
                            hitData = pitch['hitData']
                            optimalContact(hitData, optimal, pa)
                            # cords.append((hitData['coordinates']['coordX'], hitData['coordinates']['coordY']))

# hitData()

def leftVsRight():
    leftKind = []
    rightKind = []
    leftNumbers = {}
    rightNumbers = {}
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}

    sched = statsapi.schedule(start_date='07/23/2020', end_date='09/27/2020', team=137)
    for i in range(len(sched)):
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
                hitterName = pa['matchup']['batter']['fullName']
                hitterBatSide = pa['matchup']['batSide']['description']
                playEvents = pa['playEvents']
                if pitcherName == 'Kevin Gausman':
                    if hitterBatSide == 'Left':
                        for pitch in playEvents:
                            try:
                                pitchData = pitch['pitchData']
                                speed = pitchData['startSpeed']
                                pitchType = pitch['details']['type']['description']
                                spinRate = pitchData['breaks']['spinRate']
                                print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date, "in the", inning, "to", hitterName)
                                if pitchType not in leftKind:
                                    leftKind.append(pitchType)
                                    leftNumbers[pitchType] = {}
                                    leftNumbers[pitchType]['amount'] = 1
                                    leftNumbers[pitchType]['spin'] = spinRate
                                    leftNumbers[pitchType]['speed'] = speed
                                else:
                                    totalSpin = round(
                                        (leftNumbers[pitchType]['spin'] * leftNumbers[pitchType]['amount']),
                                        2)  # before the thrown pitch's spin is added and analyzed
                                    totalSpeed = round(
                                        (leftNumbers[pitchType]['speed'] * leftNumbers[pitchType]['amount']),
                                        2)  # before the thrown pitch's speed is added and analyzed

                                    leftNumbers[pitchType]['amount'] += 1
                                    totalSpin += spinRate
                                    totalSpeed += speed

                                    leftNumbers[pitchType]['spin'] = round(totalSpin / leftNumbers[pitchType]['amount'],
                                                                           2)
                                    leftNumbers[pitchType]['speed'] = round(
                                        totalSpeed / leftNumbers[pitchType]['amount'], 2)
                            except KeyError:
                                try:
                                    print(pitch['details']['description'])
                                except KeyError:
                                    if pitch['isPitch'] == False:
                                        pass
                                    else:
                                        input("Something is off here: " + pitch)
                    if hitterBatSide == 'Right':
                        for pitch in playEvents:
                            try:
                                pitchData = pitch['pitchData']
                                speed = pitchData['startSpeed']
                                pitchType = pitch['details']['type']['description']
                                spinRate = pitchData['breaks']['spinRate']
                                print(speed, "MPH /", spinRate, "RPM", pitchType, "by", pitcherName, "on", game_date,
                                      "in the", inning, "to", hitterName)
                                if pitchType not in rightKind:
                                    rightKind.append(pitchType)
                                    rightNumbers[pitchType] = {}
                                    rightNumbers[pitchType]['amount'] = 1
                                    rightNumbers[pitchType]['spin'] = spinRate
                                    rightNumbers[pitchType]['speed'] = speed
                                else:
                                    totalSpin = round(
                                        (rightNumbers[pitchType]['spin'] * rightNumbers[pitchType]['amount']),
                                        2)  # before the thrown pitch's spin is added and analyzed
                                    totalSpeed = round(
                                        (rightNumbers[pitchType]['speed'] * rightNumbers[pitchType]['amount']),
                                        2)  # before the thrown pitch's speed is added and analyzed

                                    rightNumbers[pitchType]['amount'] += 1
                                    totalSpin += spinRate
                                    totalSpeed += speed

                                    rightNumbers[pitchType]['spin'] = round(
                                        totalSpin / rightNumbers[pitchType]['amount'],
                                        2)
                                    rightNumbers[pitchType]['speed'] = round(
                                        totalSpeed / rightNumbers[pitchType]['amount'],
                                        2)
                            except KeyError:
                                try:
                                    print(pitch['details']['description'])
                                except KeyError:
                                    if pitch['isPitch'] == False:
                                        pass
                                    else:
                                        input("Something is off here: " + pitch)

    leftTemp = {}
    rightTemp = {}
    newLeftNumbers = {}
    newRightNumbers = {}

    for pitch in leftNumbers:
        leftTemp[pitch] = leftNumbers[pitch]['amount']
    leftSortedTemp = sorted(leftTemp.items(), key=operator.itemgetter(1),
                            reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in leftSortedTemp:
        newLeftNumbers[tuple[0]] = {}
        typeOfPitch = newLeftNumbers[tuple[0]]
        for type in leftNumbers[tuple[0]]:
            typeOfPitch[type] = leftNumbers[tuple[0]][type]
        "Hard coded version of what the loop above does"
        # typeOfPitch['amount'] = leftNumbers[tuple[0]]['amount']
        # typeOfPitch['spin'] = leftNumbers[tuple[0]]['spin']
        # typeOfPitch['speed'] = leftNumbers[tuple[0]]['speed']

    for pitch in rightNumbers:
        rightTemp[pitch] = rightNumbers[pitch]['amount']
    sortedTemp = sorted(rightTemp.items(), key=operator.itemgetter(1),
                        reverse=True)  # list of tuples (first thing is the pitch name, second is the amount it was thrown
    for tuple in sortedTemp:
        newRightNumbers[tuple[0]] = {}
        typeOfPitch = newRightNumbers[tuple[0]]
        for type in rightNumbers[tuple[0]]:
            typeOfPitch[type] = rightNumbers[tuple[0]][type]
        "Hard coded version of what the loop above does"
        # typeOfPitch['amount'] = rightNumbers[tuple[0]]['amount']
        # typeOfPitch['spin'] = rightNumbers[tuple[0]]['spin']
        # typeOfPitch['speed'] = rightNumbers[tuple[0]]['speed']

    print("Left:", newLeftNumbers)
    print("Right:", newRightNumbers)

def hitOnWhatPitch():
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}
    hit = 0

    sched = statsapi.schedule(start_date='07/23/2020', end_date='09/27/2020', team=137)
    for i in range(len(sched)):
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
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                if hitterName == 'Mike Yastrzemski':
                    resultOfPlay = pa['result']['event']
                    resultOfPlayDescription = pa['result']['description']
                    if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                        try:
                            hitPitch = playEvents[-1]
                            strikesWhenHit = hitPitch['count']['strikes']
                            hitPitchType = hitPitch['details']['type']['description']
                            hitPitchData = hitPitch['pitchData']
                            hitPitchSpeed = hitPitchData['startSpeed']
                            hitPitchSpin = hitPitchData['breaks']['spinRate']
                            print(resultOfPlay, "by", hitterName, "on a", hitPitchSpeed, "MPH /", hitPitchSpin, "RPM", hitPitchType, "by", pitcherName, "with", strikesWhenHit, "strikes")
                        except KeyError:
                            print(resultOfPlay, "off", pitcherName)

def firstPitch():
    sched = statsapi.schedule(start_date='07/29/2020', team=137)
    for i in range(len(sched)):
        gameId = sched[i]["game_id"]
        game_date = sched[i]["game_date"]
        game_result = sched[i]["summary"]
        game_status = sched[i]["status"]
        game = statsapi.get('game', {'gamePk': gameId})

        allPlays = game['liveData']['plays']['allPlays']
        if game_status != 'Postponed':
            for pa in allPlays:
                pitcherName = pa['matchup']['pitcher']['fullName']
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                for pitch in playEvents:
                    try:
                        if pitch['pitchNumber'] == 1:
                            firstPitch = pitch['details']['type']['description']
                            print(firstPitch, "to", hitterName, "by", pitcherName, "for the first pitch")
                    except KeyError:
                        print("Maybe problem", pitch['details']['description'])

def firstPitchStrike():
    sched = statsapi.schedule(start_date='07/29/2020', team=137)
    for i in range(len(sched)):
        gameId = sched[i]["game_id"]
        game_date = sched[i]["game_date"]
        game_result = sched[i]["summary"]
        game_status = sched[i]["status"]
        game = statsapi.get('game', {'gamePk': gameId})

        allPlays = game['liveData']['plays']['allPlays']
        if game_status != 'Postponed':
            for pa in allPlays:
                pitcherName = pa['matchup']['pitcher']['fullName']
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                for pitch in playEvents:
                    try:
                        isStrike = pitch['details']['isStrike']
                        pitchNumber = pitch['pitchNumber']
                        if pitchNumber == 1 and isStrike:
                            print("First pitch strike for", pitcherName, "against", hitterName)
                    except KeyError:
                        print("Maybe problem:", pitch['details']['description'])

def twoStrikePitches():
    sched = statsapi.schedule(start_date='07/29/2020', team=137)
    for i in range(len(sched)):
        gameId = sched[i]["game_id"]
        game_date = sched[i]["game_date"]
        game_result = sched[i]["summary"]
        game_status = sched[i]["status"]
        game = statsapi.get('game', {'gamePk': gameId})

        allPlays = game['liveData']['plays']['allPlays']
        if game_status != 'Postponed':
            for pa in allPlays:
                atTwoStrikes = False
                pitcherName = pa['matchup']['pitcher']['fullName']
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                for pitch in playEvents:
                    # print(pitch, "\n")
                    try:
                        pitchNumber = pitch['pitchNumber']
                        strikesInCount = pitch['count']['strikes']
                        ballsInCount = pitch['count']['balls']
                        call = pitch['details']['call']['description']
                        if "no out" in call:
                            call = "ball in play (no out)"
                        elif "In play" in call:
                            call = "ball in play (out)"
                        if atTwoStrikes:
                            strikePitch = pitch['details']['type']['description']
                            print(strikePitch, "to", hitterName, "by", pitcherName, "with 2 strikes", "for a", call, "\n")
                        if strikesInCount == 2:  # This is for when there are two strikes AFTER the pitch is thrown (this is why atTwoStrikes is checked before strikesInCount (because when strikesInCount turns to 2, it doesn't necessarily mean that the batter had 2 strikes before the pitch))
                            atTwoStrikes = True  # No worries if atTwoStrikes is True when the ball is put in play because atTwoStrikes is reset to False when there's a new plate appearance
                    except KeyError:
                        print("Maybe problem", pitch['details']['description'])

def twoStrikeAverage():
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th",
                   11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}
    twoStrikeAtBats = 0
    twoStrikeHits = 0

    sched = statsapi.schedule(start_date='07/23/2020', end_date='09/27/2020', team=137)
    for i in range(len(sched)):
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
                hitterName = pa['matchup']['batter']['fullName']
                playEvents = pa['playEvents']
                if hitterName == 'Mike Yastrzemski':
                    input(pa)
                    resultOfPlay = pa['result']['event']
                    resultOfPlayDescription = pa['result']['description']
                    lastPitchStrikesInCount = playEvents[-1]['count']['strikes']
                    if lastPitchStrikesInCount == 2:
                        # No need for a work-around like with TwoStrikePitches()
                        # A ball put into play would mean the end of the at bat (if amount of strikes in the count was 1 at the time, then the strikes in count reads as 1 in the data), so if the last pitch of the at bat has 2 strikes, it definitely means that the ball was put into play when the count was at two strikes
                        if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                            twoStrikeAtBats += 1
                            twoStrikeHits += 1
                        elif resultOfPlay == 'Field Error':
                            twoStrikeAtBats += 1
                            twoStrikeHits += 0
                        elif resultOfPlay == 'Walk' or resultOfPlay == 'Intentional Walk':
                            twoStrikeAtBats += 0
                            twoStrikeHits += 0
                        else:
                            twoStrikeAtBats += 1
                            twoStrikeHits += 0
                    if lastPitchStrikesInCount == 3:  # This means that the batter struck out
                        twoStrikeAtBats += 1
                        twoStrikeHits += 0
    average = round(twoStrikeHits / twoStrikeAtBats, 3)
    print(average)

# twoStrikeAverage()

def liveGamePbp():
    # print(game['liveData']['boxscore']['teams']['away']['players'])
    # print(game['liveData']['linescore'])
    # print(play['allPlays'])
    sched = statsapi.schedule(start_date='07/29/2020', team=137)
    gameId = sched["game_id"]
    game_date = sched["game_date"]
    game_result = sched["summary"]
    game = statsapi.get('game', {'gamePk': gameId})
    analyzed = []
    while True:
        play = statsapi.get('game_playByPlay', {'gamePk': gameId})
        game = statsapi.get('game', {'gamePk': gameId})
        """if code is run during game, range must have a -1"""
        # for i in range(len(play['allPlays'])-1):
        #     if i not in analyzed:
        #         print(str(i + 1), play['allPlays'][i]['result']['description'])
        #         analyzed.append(int(i))
        for i in range(len(game['liveData']['plays']['allPlays']) - 1):
            if i not in analyzed:
                print(str(i + 1), game['liveData']['plays']['allPlays'][i]['result']['description'])
                analyzed.append(int(i))


executionTime = (time.time() - startTime)
print("==============")
print('Execution time in seconds: ' + str(executionTime))
print("==============")
