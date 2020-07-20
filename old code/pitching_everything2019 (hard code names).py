import statsapi

def pitching_everything2019():

  players=[]

  for i in range(len(players)):
    playername = players[i]
  
    with open("2019/"+str(playername)+".txt", "r") as FILE:
      content = FILE.read()
      try:
        content_dict = eval( content )
      except Exception as e:
        print( "we got an error ", e ) 
        print("Database Error ")
      else:
        print("read succees for",playername)
      ID = content_dict[playername]["ID"]

    sched = statsapi.schedule(start_date='03/28/2019',end_date='09/29/2019',team=137)
    for i in range(len(sched)):
      gameId = sched[i]["game_id"]
      game_date = sched[i]["game_date"]
      scoredata = statsapi.boxscore_data(gameId)
      if sched[i]["game_type"] == "R":
        if sched[i]['home_name']=="San Francisco Giants":
          if ID in scoredata['home']['players']:
            if scoredata['home']['players'][ID]['stats']['pitching']!={}:
              #progressive
              p_era=scoredata['home']['players'][ID]['seasonStats']['pitching']['era']
              p_innings=(scoredata['home']['players'][ID]['seasonStats']['pitching']['inningsPitched'])
              p_hits=(scoredata['home']['players'][ID]['seasonStats']['pitching']['hits'])
              p_runs=scoredata['home']['players'][ID]['seasonStats']['pitching']['runs']
              p_earned_runs=scoredata['home']['players'][ID]['seasonStats']['pitching']['earnedRuns']
              p_walks=scoredata['home']['players'][ID]['seasonStats']['pitching']['baseOnBalls']
              p_strikeouts=scoredata['home']['players'][ID]['seasonStats']['pitching']['strikeOuts']
              p_homeruns=scoredata['home']['players'][ID]['seasonStats']['pitching']['homeRuns']
              p_doubles=scoredata['home']['players'][ID]['seasonStats']['pitching']['doubles']
              p_triples=scoredata['home']['players'][ID]['seasonStats']['pitching']['triples']
              p_ab=scoredata['home']['players'][ID]['seasonStats']['pitching']['atBats']
              p_obp=scoredata['home']['players'][ID]['seasonStats']['pitching']['obp']
              p_wins=scoredata['home']['players'][ID]['seasonStats']['pitching']['wins']
              p_losses=scoredata['home']['players'][ID]['seasonStats']['pitching']['losses']
              p_holds=scoredata['home']['players'][ID]['seasonStats']['pitching']['holds']
              p_blown_saves=scoredata['home']['players'][ID]['seasonStats']['pitching']['blownSaves']
              pg_innings=scoredata['home']['players'][ID]['stats']['pitching']['inningsPitched']
              pg_hits=scoredata['home']['players'][ID]['stats']['pitching']['hits']
              pg_runs=scoredata['home']['players'][ID]['stats']['pitching']['runs']
              pg_earned_runs=scoredata['home']['players'][ID]['stats']['pitching']['earnedRuns']
              pg_walks=scoredata['home']['players'][ID]['stats']['pitching']['baseOnBalls']
              pg_strikeouts=scoredata['home']['players'][ID]['stats']['pitching']['strikeOuts']
              pg_homeruns=scoredata['home']['players'][ID]['stats']['pitching']['homeRuns']
              pg_pitches=scoredata['home']['players'][ID]['stats']['pitching']['pitchesThrown']
              pg_strikes=scoredata['home']['players'][ID]['stats']['pitching']['strikes']

              p_categories = [p_era,p_innings,p_hits,p_runs,p_earned_runs,p_walks,p_strikeouts,p_homeruns,p_doubles,p_triples, p_ab, p_obp,p_wins,p_losses,p_holds,p_blown_saves]
              pg_categories = [pg_innings,pg_hits,pg_runs,pg_earned_runs,pg_walks,pg_strikeouts,pg_homeruns,pg_pitches,pg_strikes]
              p_names = ['era','innings','hits','runs','earned_runs','walks','strikeouts','homeruns','doubles','triples','ab','obp','wins','losses','holds','blown_saves']
              pg_names = ['innings','hits','runs','earned_runs','walks','strikeouts','homeruns','pitches','strikes']

              if game_date == '2019-07-15':
                print("Here I am")
                if content_dict[playername]['2019']['dates'].count('2019-07-15')<1:
                  print(content_dict[playername]['2019']['dates'].count('2019-07-15'))
                  with open("2019/"+str(playername)+".txt", "w") as f:
                    try:
                      content_dict[playername]['2019']['dates'].append(game_date)
                      for i in range(len(p_categories)):
                        content_dict[playername]['2019']['progression'][p_names[i]].append(p_categories[i])
                      for i in range(len(pg_categories)):
                        content_dict[playername]['2019']['per_game'][pg_names[i]].append(pg_categories[i])
                      f.write(str(content_dict))
                      print("Write Success")
                    except Exception as e:
                      print( "we got an error ", e ) 
              else:
                if game_date not in content_dict[playername]['2019']['dates']:
                  print("Yes")
                  with open("2019/"+str(playername)+".txt", "w") as f:
                    try:
                      content_dict[playername]['2019']['dates'].append(game_date)
                      for i in range(len(p_categories)):
                        content_dict[playername]['2019']['progression'][p_names[i]].append(p_categories[i])
                      for i in range(len(pg_categories)):
                        content_dict[playername]['2019']['per_game'][pg_names[i]].append(pg_categories[i])
                      f.write(str(content_dict))
                      print("Write Success")
                    except Exception as e:
                      print( "we got an error ", e ) 
                else:
                  pass
                  print("Already In")

        else:
          if ID in scoredata['away']['players']:
            if scoredata['away']['players'][ID]['stats']['pitching']!={}:
              #progressive
              p_era=scoredata['away']['players'][ID]['seasonStats']['pitching']['era']
              p_innings=(scoredata['away']['players'][ID]['seasonStats']['pitching']['inningsPitched'])
              p_hits=(scoredata['away']['players'][ID]['seasonStats']['pitching']['hits'])
              p_runs=scoredata['away']['players'][ID]['seasonStats']['pitching']['runs']
              p_earned_runs=scoredata['away']['players'][ID]['seasonStats']['pitching']['earnedRuns']
              p_walks=scoredata['away']['players'][ID]['seasonStats']['pitching']['baseOnBalls']
              p_strikeouts=scoredata['away']['players'][ID]['seasonStats']['pitching']['strikeOuts']
              p_homeruns=scoredata['away']['players'][ID]['seasonStats']['pitching']['homeRuns']
              p_doubles=scoredata['away']['players'][ID]['seasonStats']['pitching']['doubles']
              p_triples=scoredata['away']['players'][ID]['seasonStats']['pitching']['triples']
              p_ab=scoredata['away']['players'][ID]['seasonStats']['pitching']['atBats']
              p_obp=scoredata['away']['players'][ID]['seasonStats']['pitching']['obp']
              p_wins=scoredata['away']['players'][ID]['seasonStats']['pitching']['wins']
              p_losses=scoredata['away']['players'][ID]['seasonStats']['pitching']['losses']
              p_holds=scoredata['away']['players'][ID]['seasonStats']['pitching']['holds']
              p_blown_saves=scoredata['away']['players'][ID]['seasonStats']['pitching']['blownSaves']
              pg_innings=scoredata['away']['players'][ID]['stats']['pitching']['inningsPitched']
              pg_hits=scoredata['away']['players'][ID]['stats']['pitching']['hits']
              pg_runs=scoredata['away']['players'][ID]['stats']['pitching']['runs']
              pg_earned_runs=scoredata['away']['players'][ID]['stats']['pitching']['earnedRuns']
              pg_walks=scoredata['away']['players'][ID]['stats']['pitching']['baseOnBalls']
              pg_strikeouts=scoredata['away']['players'][ID]['stats']['pitching']['strikeOuts']
              pg_homeruns=scoredata['away']['players'][ID]['stats']['pitching']['homeRuns']
              pg_pitches=scoredata['away']['players'][ID]['stats']['pitching']['pitchesThrown']
              pg_strikes=scoredata['away']['players'][ID]['stats']['pitching']['strikes']

              p_categories = [p_era,p_innings,p_hits,p_runs,p_earned_runs,p_walks,p_strikeouts,p_homeruns,p_doubles,p_triples, p_ab, p_obp,p_wins,p_losses,p_holds,p_blown_saves]
              pg_categories = [pg_innings,pg_hits,pg_runs,pg_earned_runs,pg_walks,pg_strikeouts,pg_homeruns,pg_pitches,pg_strikes]
              p_names = ['era','innings','hits','runs','earned_runs','walks','strikeouts','homeruns','doubles','triples','ab','obp','wins','losses','holds','blown_saves']
              pg_names = ['innings','hits','runs','earned_runs','walks','strikeouts','homeruns','pitches','strikes']

              if game_date == '2019-07-15':
                print("Here I am")
                if content_dict[playername]['2019']['dates'].count('2019-07-15')<1:
                  print(content_dict[playername]['2019']['dates'].count('2019-07-15'))
                  with open("2019/"+str(playername)+".txt", "w") as f:
                    try:
                      content_dict[playername]['2019']['dates'].append(game_date)
                      for i in range(len(p_categories)):
                        content_dict[playername]['2019']['progression'][p_names[i]].append(p_categories[i])
                      for i in range(len(pg_categories)):
                        content_dict[playername]['2019']['per_game'][pg_names[i]].append(pg_categories[i])
                      f.write(str(content_dict))
                      print("Write Success")
                    except Exception as e:
                      print( "we got an error ", e ) 
              else:
                if game_date not in content_dict[playername]['2019']['dates']:
                  print("Yes")
                  with open("2019/"+str(playername)+".txt", "w") as f:
                    try:
                      content_dict[playername]['2019']['dates'].append(game_date)
                      for i in range(len(p_categories)):
                        content_dict[playername]['2019']['progression'][p_names[i]].append(p_categories[i])
                      for i in range(len(pg_categories)):
                        content_dict[playername]['2019']['per_game'][pg_names[i]].append(pg_categories[i])
                      f.write(str(content_dict))
                      print("Write Success")
                    except Exception as e:
                      print( "we got an error ", e )
                else:
                  pass
                  print("Already In")


          