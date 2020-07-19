import statsapi

def hitting(search_player):

  dates=[]
  averages=[]
  on_base_percentage=[]
  slugging=[]
  on_plus_slugging=[]
  at_bats=[]
  strikeouts=[]
  hits=[]
  walks=[]
  runs=[]
  runs_batted_in=[]
  stolen_bases=[]
  left_on_base=[]
  doubles=[]
  triples=[]
  homers=[]

  sched = statsapi.schedule(start_date='03/28/2019', end_date = '09/29/2019', team=137)
  for i in range(len(sched)):
    gameId = sched[i]["game_id"]
    game_date = sched[i]["game_date"]
    game_result = sched[i]["summary"]
    scoredata = statsapi.boxscore_data(gameId)
    length_home = len(scoredata['homeBatters'])
    length_away = len(scoredata['awayBatters'])
    if sched[i]["game_type"] == "R":
      #all home games
      if sched[i]['home_name']=="San Francisco Giants":
        for i in range(1,length_home):
          player_name=(scoredata['homeBatters'][i]['name'])
          avg=(scoredata['homeBatters'][i]['avg'])
          obp=(scoredata['homeBatters'][i]['obp'])
          ops = scoredata['homeBatters'][i]['ops']
          slg = scoredata['homeBatters'][i]['slg']
          k = scoredata['homeBatters'][i]['k']
          ab = scoredata['homeBatters'][i]['ab']
          h = scoredata['homeBatters'][i]['h']
          bb = scoredata['homeBatters'][i]['bb']
          r = scoredata['homeBatters'][i]["r"]
          rbi = scoredata['homeBatters'][i]["rbi"]
          sb = scoredata['homeBatters'][i]['sb']
          lob = scoredata['homeBatters'][i]['lob']
          double = scoredata['homeBatters'][i]['doubles']
          triple = scoredata['homeBatters'][i]['triples']
          hr = scoredata['homeBatters'][i]['hr']
          if player_name == search_player:
            dates.append(game_date)
            averages.append(float(avg))
            on_base_percentage.append(float(obp))
            slugging.append(float(slg))
            strikeouts.append(float(k))
            at_bats.append(int(ab))
            hits.append(int(h))
            walks.append(int(bb))
            runs.append(int(r))
            runs_batted_in.append(int(rbi))
            stolen_bases.append(int(sb))
            left_on_base.append(int(lob))
            doubles.append(int(double))
            triples.append(int(triple))
            homers.append(int(hr))

      #all_away games
      else:
        for i in range(1,length_away):
          player_name=(scoredata['awayBatters'][i]['name'])
          avg=(scoredata['awayBatters'][i]['avg'])
          obp=(scoredata['awayBatters'][i]['obp'])
          ops = scoredata['awayBatters'][i]['ops']
          slg = scoredata['awayBatters'][i]['slg']
          k = scoredata['awayBatters'][i]['k']
          ab = scoredata['awayBatters'][i]['ab']
          h = scoredata['awayBatters'][i]['h']
          bb = scoredata['awayBatters'][i]['bb']
          r = scoredata['awayBatters'][i]["r"]
          rbi = scoredata['awayBatters'][i]["rbi"]
          sb = scoredata['awayBatters'][i]['sb']
          lob = scoredata['awayBatters'][i]['lob']
          lob = scoredata['awayBatters'][i]['lob']
          double = scoredata['awayBatters'][i]['doubles']
          triple = scoredata['awayBatters'][i]['triples']
          hr = scoredata['awayBatters'][i]['hr']
          if player_name == search_player:
            dates.append(game_date)
            averages.append(float(avg))
            on_base_percentage.append(float(obp))
            slugging.append(float(slg))
            strikeouts.append(float(k))
            at_bats.append(int(ab))
            hits.append(int(h))
            walks.append(int(bb))
            runs.append(int(r))
            runs_batted_in.append(int(rbi))
            stolen_bases.append(int(sb))
            left_on_base.append(int(lob))
            doubles.append(int(double))
            triples.append(int(triple))
            homers.append(int(hr))
  return dates, on_base_percentage

