import statsapi

sched = statsapi.schedule(start_date= '07/23/2020', team=137)
gameId = sched[0]["game_id"]
boxscore = statsapi.boxscore_data(gameId)
# print(boxscore)
game = statsapi.get('game', {'gamePk': gameId})
players = game['gameData']['players']
liveData = game['liveData']
liveBox = liveData['boxscore']
awayPlayers = liveBox['teams']['away']['players']
homePlayers = liveBox['teams']['home']['players']

# for item in awayPlayers:
#     print(item, awayPlayers[item]['person']['fullName'], awayPlayers[item]['position'], awayPlayers[item]['stats'])
#     print("")

list = []

for item in awayPlayers['ID592767']['seasonStats']['pitching']:
    print(item, awayPlayers['ID592767']['seasonStats']['pitching'][item])
    list.append("p_" + item)

# for item in awayPlayers['ID573262']['seasonStats']['batting']:
#     print(item, awayPlayers['ID573262']['seasonStats']['batting'][item])
#     list.append("p_" + item)

print(list)

removed = ['p_inheritedRunners']

# p_pitchesPerInning goes with per game (not progressive)

