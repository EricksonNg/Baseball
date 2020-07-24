import statsapi

sched = statsapi.schedule(start_date='07/23/2020', team=137)
# print(sched)
gameId = sched[0]["game_id"]
game_date = sched[0]["game_date"]
game_result = sched[0]["summary"]
# print(game['liveData']['boxscore']['teams']['away']['players'])
# print(play['allPlays'])
analyzed = []
while True:
    play = statsapi.get('game_playByPlay', {'gamePk': gameId})
    game = statsapi.get('game', {'gamePk': gameId})
    """if code is run during game, range must have a -1"""
    for i in range(len(play['allPlays'])):
        if i not in analyzed:
            print(str(i + 1), play['allPlays'][i]['result']['description'])
            analyzed.append(int(i))
#     # for i in range(len(game['liveData']['plays']['allPlays'])-1):
#     #     if i not in analyzed:
#     #         print(str(i+1), game['liveData']['plays']['allPlays'][i]['result']['description'])
#     #         analyzed.append(int(i))
