import statsapi

def hitOnWhatPitch():
    inningsName = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th", 10: "10th", 11: "11th", 12: "12th", 13: "13th", 14: "14th", 15: "15th", 16: "16th", 17: "17th", 18: "18th"}
    hit = 0
    totalHitEV = 0

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
                    # input(pa)
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
                            hitData = hitPitch['hitData']
                            hitPitchEV = hitData['launchSpeed']
                            print(hitPitchEV, "MPH", resultOfPlay, "by", hitterName, "on a", hitPitchSpeed, "MPH /", hitPitchSpin, "RPM", hitPitchType, "by", pitcherName, "with", strikesWhenHit, "strikes")
                            hit += 1
                            totalHitEV += hitPitchEV
                        except KeyError:
                            print(resultOfPlay, "off", pitcherName)
    print(totalHitEV/hit)

def twoStrikeStats():
    sched = statsapi.schedule(start_date='07/23/2020', end_date = '09/27/2020', team=137)
    twoStrikeHits = 0
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
                if hitterName == 'Mike Yastrzemski':
                    resultOfPlay = pa['result']['event']
                    resultOfPlayDescription = pa['result']['description']
                    lastPitch = playEvents[-1]
                    lastPitchStrikesInCount = lastPitch['count']['strikes']
                    if 'Caught' not in resultOfPlay and 'Pickoff' not in resultOfPlay:
                        if lastPitchStrikesInCount >= 2:
                            if resultOfPlay == 'Single' or resultOfPlay == 'Double' or resultOfPlay == 'Triple' or resultOfPlay == 'Home Run':
                                print(resultOfPlayDescription)
                                twoStrikeHits += 1
                    else:
                        input(pa)
    print(twoStrikeHits)


# hitOnWhatPitch()

twoStrikeStats()