import statsapi
import os

def getplayerid():

  lastname = input("Player Last Name: ")
  
  sched = statsapi.schedule(start_date='02/22/2020',end_date='03/11/2020',team=137)
  for i in range(len(sched)):
    gameId = sched[i]["game_id"]
    scoredata = statsapi.boxscore_data(gameId)
    length_b_home = len(scoredata['homeBatters'])
    length_b_away = len(scoredata['awayBatters'])
    length_p_home = len(scoredata['homePitchers'])
    length_p_away = len(scoredata['awayPitchers'])
    if sched[i]['home_name']=='San Francisco Giants':
      for i in range(1,length_p_home):
        pitcher_name=scoredata['homePitchers'][i]['name']
        player_id='ID'+str(scoredata['homePitchers'][i]['personId'])
        fullname=scoredata['playerInfo'][player_id]['fullName']
        if lastname==pitcher_name:
          print(str(pitcher_name),": "+str(player_id))
          to_txtp(fullname,player_id)
          input()
      for i in range(1,length_b_home):
        batter_name=scoredata['homeBatters'][i]['name']
        player_id='ID'+str(scoredata['homeBatters'][i]['personId'])
        fullname=scoredata['playerInfo'][player_id]['fullName']
        if lastname==batter_name:
          print(str(batter_name),": "+str(player_id)) 
          to_txtb(fullname,player_id)
          input()
    else:
      for i in range(1,length_p_away):
        pitcher_name=scoredata['awayPitchers'][i]['name']
        player_id='ID'+str(scoredata['awayPitchers'][i]['personId'])
        fullname=scoredata['playerInfo'][player_id]['fullName']
        if lastname==pitcher_name:
          print(str(pitcher_name),": "+str(player_id))
          to_txtp(fullname,player_id)
          input()
      for i in range(1,length_b_away):
        batter_name=scoredata['awayBatters'][i]['name']
        player_id='ID'+str(scoredata['awayBatters'][i]['personId'])
        fullname=scoredata['playerInfo'][player_id]['fullName']
        if lastname==batter_name:
          print(str(batter_name),": "+str(player_id))
          to_txtb(fullname,player_id)
          input()
            
# def to_txt(fullname,player_id):
#   with open("2020/"+str(fullname)+".txt", "r") as FILE:
#     content = FILE.read()
#     try:
#       content_dict = eval( content )
#     except Exception as e:
#       print( "we got an error ", e) 
#       print("Read Error ")

#   with open("2020/"+str(fullname)+".txt", "w") as f:
#     try:
#       content_dict[fullname]['ID']=player_id
#       f.write(str(content_dict))
#       print(content_dict[fullname]['ID'])
#       print("Write success")
#     except Exception as e:
#       print( "we got an error ", e) 
#       print("Write Error ")

def to_txtb(fullname,player_id):
  with open("2020/"+str(fullname)+".txt", "w") as f:
    try:
      f.write("{'"+fullname+"': {'ID':'"+player_id+"', '2020': {'dates': [], 'progression': {'averages': [], 'obp': [], 'slg': [], 'ops': [], 'runs': [], 'doubles': [], 'triples': [], 'homeruns': [], 'strikeouts': [], 'walks': [], 'hits': [], 'ab': [], 'sb': [], 'rbi': [], 'lob': []}, 'per_game': {'ab': [], 'strikeouts': [], 'hits': [], 'walks': [], 'runs': [], 'rbi': [], 'sb': [], 'lob': [], 'doubles': [], 'triples': [], 'homeruns': []}}}}")
      print("Write success")
    except Exception as e:
      print( "we got an error ", e) 
      print("Write Error ")

def to_txtp(fullname,player_id):

  with open("2020/"+str(fullname)+".txt", "w") as f:
    try:
      f.write("{'"+fullname+"': {'ID':'"+player_id+"', '2020': {'dates': [], 'progression': {'era': [], 'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'doubles': [], 'triples': [], 'ab': [], 'obp': [], 'wins': [], 'losses': [], 'holds': [], 'blown_saves': []}, 'per_game': {'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'pitches': [], 'strikes': []}}}}")
      print("Write success")
    except Exception as e:
      print( "we got an error ", e) 
      print("Write Error ")