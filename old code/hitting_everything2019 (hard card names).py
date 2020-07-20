import statsapi

def hitting_everything2019():

  players = ['Alex Dickerson','Aramis Garcia','Austin Slater','Brandon Belt','Brandon Crawford','Buster Posey','Chris Shaw','Donovan Solano','Evan Longoria','Hunter Pence','Jaylin Davis','Joey Rickard','Mauricio Dubon','Mike Yastrzemski','Pablo Sandoval','Wilmer Flores']
  
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
        print("read success for",playername)
      ID = content_dict[playername]["ID"]

    #progressive
    sched = statsapi.schedule(start_date='03/28/2019',end_date='09/29/2019',team=137)
    for i in range(len(sched)):
      gameId = sched[i]["game_id"]
      game_date = sched[i]["game_date"]
      scoredata = statsapi.boxscore_data(gameId)
      if sched[i]["game_type"] == "R":
        if game_date!='2019-05-08':
          if sched[i]['home_name']=="San Francisco Giants":
            if ID in scoredata['home']['players']:
              if scoredata['home']['players'][ID]['stats']['batting']!={}:
                #progressive
                p_averages=float(scoredata['home']['players'][ID]['seasonStats']['batting']['avg'])
                p_obp=float(scoredata['home']['players'][ID]['seasonStats']['batting']['obp'])
                p_slg=float(scoredata['home']['players'][ID]['seasonStats']['batting']['slg'])
                p_ops=float(scoredata['home']['players'][ID]['seasonStats']['batting']['ops'])
                p_runs=int(scoredata['home']['players'][ID]['seasonStats']['batting']['runs'])
                p_doubles=int(scoredata['home']['players'][ID]['seasonStats']['batting']['doubles'])
                p_triples=int(scoredata['home']['players'][ID]['seasonStats']['batting']['triples'])
                p_homeruns=int(scoredata['home']['players'][ID]['seasonStats']['batting']['homeRuns'])
                p_strikeouts=int(scoredata['home']['players'][ID]['seasonStats']['batting']['strikeOuts'])
                p_walks=int(scoredata['home']['players'][ID]['seasonStats']['batting']['baseOnBalls'])
                p_hits=int(scoredata['home']['players'][ID]['seasonStats']['batting']['hits'])
                p_ab=int(scoredata['home']['players'][ID]['seasonStats']['batting']['atBats'])
                p_sb=int(scoredata['home']['players'][ID]['seasonStats']['batting']['stolenBases'])
                p_rbi=int(scoredata['home']['players'][ID]['seasonStats']['batting']['rbi'])
                p_lob=int(scoredata['home']['players'][ID]['seasonStats']['batting']['leftOnBase'])
                #per game
                pg_ab = int(scoredata['home']['players'][ID]['stats']['batting']['atBats'])
                pg_strikeouts = int(scoredata['home']['players'][ID]['stats']['batting']['strikeOuts'])
                pg_hits = int(scoredata['home']['players'][ID]['stats']['batting']['hits'])
                pg_walks = int(scoredata['home']['players'][ID]['stats']['batting']['baseOnBalls'])
                pg_runs = int(scoredata['home']['players'][ID]['stats']['batting']['runs'])
                pg_rbi = int(scoredata['home']['players'][ID]['stats']['batting']['rbi'])
                pg_sb = int(scoredata['home']['players'][ID]['stats']['batting']['stolenBases'])
                pg_lob = int(scoredata['home']['players'][ID]['stats']['batting']['leftOnBase'])
                pg_doubles = int(scoredata['home']['players'][ID]['stats']['batting']['doubles'])
                pg_triples = int(scoredata['home']['players'][ID]['stats']['batting']['triples'])
                pg_homeruns = int(scoredata['home']['players'][ID]['stats']['batting']['homeRuns'])

                p_categories = [p_averages, p_obp, p_slg, p_ops, p_runs, p_doubles, p_triples, p_homeruns, p_strikeouts, p_walks,p_hits, p_ab, p_sb, p_rbi, p_lob]
                pg_categories = [pg_ab, pg_strikeouts, pg_hits, pg_walks, pg_runs, pg_rbi, pg_sb, pg_lob, pg_doubles, pg_triples, pg_homeruns]
                p_names = ['averages', 'obp', 'slg', 'ops', 'runs', 'doubles', 'triples', 'homeruns', 'strikeouts','walks','hits','ab','sb','rbi','lob']
                pg_names= ['ab','strikeouts','hits','walks','runs','rbi','sb','lob','doubles','triples','homeruns']

                if game_date == '2019-07-15':
                  print("Here I am")
                  if content_dict[playername]['2019']['dates'].count('2019-07-15')<2:
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
                        print("Database Error ")
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
                        print("Database Error ")
                  else:
                    pass
                    print("Already in for", playername)
                  
          else:
            if ID in scoredata['away']['players']:
              if scoredata['away']['players'][ID]['stats']['batting']!={}:
                #progressive
                p_averages=float(scoredata['away']['players'][ID]['seasonStats']['batting']['avg'])
                p_obp=float(scoredata['away']['players'][ID]['seasonStats']['batting']['obp'])
                p_slg=float(scoredata['away']['players'][ID]['seasonStats']['batting']['slg'])
                p_ops=float(scoredata['away']['players'][ID]['seasonStats']['batting']['ops'])
                p_runs=int(scoredata['away']['players'][ID]['seasonStats']['batting']['runs'])
                p_doubles=int(scoredata['away']['players'][ID]['seasonStats']['batting']['doubles'])
                p_triples=int(scoredata['away']['players'][ID]['seasonStats']['batting']['triples'])
                p_homeruns=int(scoredata['away']['players'][ID]['seasonStats']['batting']['homeRuns'])
                p_strikeouts=int(scoredata['away']['players'][ID]['seasonStats']['batting']['strikeOuts'])
                p_walks=int(scoredata['away']['players'][ID]['seasonStats']['batting']['baseOnBalls'])
                p_hits=int(scoredata['away']['players'][ID]['seasonStats']['batting']['hits'])
                p_ab=int(scoredata['away']['players'][ID]['seasonStats']['batting']['atBats'])
                p_sb=int(scoredata['away']['players'][ID]['seasonStats']['batting']['stolenBases'])
                p_rbi=int(scoredata['away']['players'][ID]['seasonStats']['batting']['rbi'])
                p_lob=int(scoredata['away']['players'][ID]['seasonStats']['batting']['leftOnBase'])
                #per game
                pg_ab = scoredata['away']['players'][ID]['stats']['batting']['atBats']
                pg_strikeouts = scoredata['away']['players'][ID]['stats']['batting']['strikeOuts']
                pg_hits = scoredata['away']['players'][ID]['stats']['batting']['hits']
                pg_walks = scoredata['away']['players'][ID]['stats']['batting']['baseOnBalls']
                pg_runs = scoredata['away']['players'][ID]['stats']['batting']['runs']
                pg_rbi = scoredata['away']['players'][ID]['stats']['batting']['rbi']
                pg_sb = scoredata['away']['players'][ID]['stats']['batting']['stolenBases']
                pg_lob = scoredata['away']['players'][ID]['stats']['batting']['leftOnBase']
                pg_doubles = scoredata['away']['players'][ID]['stats']['batting']['doubles']
                pg_triples = scoredata['away']['players'][ID]['stats']['batting']['triples']
                pg_homeruns = scoredata['away']['players'][ID]['stats']['batting']['homeRuns']

                p_categories = [p_averages, p_obp, p_slg, p_ops, p_runs, p_doubles, p_triples, p_homeruns, p_strikeouts, p_walks,p_hits, p_ab, p_sb, p_rbi, p_lob]
                pg_categories = [pg_ab, pg_strikeouts, pg_hits, pg_walks, pg_runs, pg_rbi, pg_sb, pg_lob, pg_doubles, pg_triples, pg_homeruns]
                p_names = ['averages', 'obp', 'slg', 'ops', 'runs', 'doubles', 'triples', 'homeruns', 'strikeouts','walks','hits','ab','sb','rbi','lob']
                pg_names= ['ab','strikeouts','hits','walks','runs','rbi','sb','lob','doubles','triples','homeruns']

                if game_date == '2019-07-15':
                  print("Here I am")
                  if content_dict[playername]['2019']['dates'].count('2019-07-15')<2:
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
                        print("Database Error ")
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
                        print("Database Error ")
                  else:
                    pass
                    print("Already in for", playername)
