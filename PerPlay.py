import statsapi

sched = statsapi.schedule(date='08/11/2020', team =137)
gameId = sched[0]["game_id"]
game_date = sched[0]["game_date"]
game_result = sched[0]["summary"]
game = statsapi.get('game', {'gamePk': gameId})
play = statsapi.get('game_playByPlay', {'gamePk': gameId})
line = statsapi.get('game_linescore', {'gamePk': gameId})
win = statsapi.get('game_winProbability', {'gamePk': gameId})
highlights = statsapi.game_highlight_data(gameId)

print(highlights)

# for i in play['allPlays']:
#     # print(i['result']['description'])
#     print(i)
#     print("")

# for i in range(len(play['allPlays'])):
#     if 'hitData' in play['allPlays'][i]['playEvents'][-1]:
#         print(i, play['allPlays'][i]['playEvents'][-1]['hitData'])

# for i in range(len(game['liveData']['plays']['allPlays'])):
#     if 'hitData' in game['liveData']['plays']['allPlays'][i]['playEvents'][-1]:
#         for e in game['liveData']['plays']['allPlays'][i]['playEvents'][-1]['hitData']:
#             print(i+1,e+":", game['liveData']['plays']['allPlays'][i]['playEvents'][-1]['hitData'][e])