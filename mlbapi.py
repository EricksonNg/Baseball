import statsapi
import os 

def lookupid(teamname):
  team_id = statsapi.lookup_team(teamname)[0]["id"]
  return team_id

def getTeam(team_id):
  stat = statsapi.get("team",{"teamId":team_id}) # identify team throught teamId
  return stat

def search_sched(start_date, end_date):
  game_info = statsapi.schedule(start_date= start_date, end_date = end_date, team=137)
  return game_info

def get_gameid(sched):
  game_id = sched[0]["game_id"]
  return game_id

def fboxscore(game_id):
  formatted = statsapi.boxscore(game_id)
  return formatted

def linescore(game_id):
  linescore = statsapi.linescore(game_id)
  return linescore

def win_prob():
  sched = statsapi.schedule(start_date='09/01/2019',team=137)
  gameId = sched[0]["game_id"]
  game_date = sched[0]["game_date"]
  game_result = sched[0]["summary"]
  test=[]
  play = statsapi.get('game_playByPlay',{'gamePk':gameId})
  for i in range(len(play['allPlays'])):
    test.append(play['allPlays'][i]['result']['description'])
  return play['allPlays'][8]


def avgobp():
  """Print out averages and on base percentage for players that showed up in the box scores of the games played within the start and end date specified in sched"""
  sched = statsapi.schedule(start_date='09/01/2019', team=137)
  for i in range(len(sched)):
    gameId = sched[i]["game_id"]
    game_date = sched[i]["game_date"]
    game_result = sched[i]["summary"]
    scoredata = statsapi.boxscore_data(gameId)
    length_home = len(scoredata['homeBatters'])
    length_away = len(scoredata['awayBatters'])
    title= game_result,"/",gameId
    title_length = len(str(title))-8

    #check if regular season
    if sched[i]["game_type"] == "R":
      print("")
      print((title_length)*"=")
      print(game_result,"/",gameId)
      print((title_length)*"=")
      print("")
      if sched[i]['home_name']=="San Francisco Giants":
        for i in range(1,length_home):
          average=(scoredata['homeBatters'][i]['avg'])
          on_base_percentage=(scoredata['homeBatters'][i]['obp'])
          player_name=(scoredata['homeBatters'][i]['name'])
          print(player_name+":","AVG -",average,"/","OBP -", on_base_percentage)
      else:
        for i in range(1,length_away):
          average=(scoredata['awayBatters'][i]['avg'])
          on_base_percentage=(scoredata['awayBatters'][i]['obp'])
          player_name=(scoredata['awayBatters'][i]['name'])
          print(player_name+":","AVG -",average,"/","OBP -", on_base_percentage)
  print("")
  print((title_length)*"=")
  
  
# sched = statsapi.schedule(start_date= '09/01/2019',team=137)
# gameId = sched[0]["game_id"]
# scoredata = statsapi.boxscore_data(gameId)
# game_date = sched[0]["game_date"]
# game_result = sched[0]["summary"]


  

# def json_explorer(json,level = 0):
#   if json == None:
#     print("null")
#     return

#   if type(json) == list and len(json) >= 1:
#     print(level*"  "+"[")
#     for item in json:
#       json_explorer(item,level+1)
#     print(level*"  "+"]")

#   if type(json) == dict:
#     print(level*"  "+"{")

#     if level < 2:
#       for key in json:
#         if type(json[key]) == str or type(json[key])==int:
#           print((level*"  ")+"-",key, ":", json[key])

#         elif type(json[key])==list or type(json[key])==dict:
#             print((level*"  ")+"-",key)
#             json_explorer(json[key],level+1)

#     print(level*"  "+"}")

# print("====JSOON====") 
# json_explorer(scoredata['away'])
