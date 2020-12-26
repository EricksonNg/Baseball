from os import path
import statsapi

new = []
teams = ['ARI', 'ATL','BAL','BOS','CHC','CIN','CLE','COL','CWS','DET','HOU','KC','LAA','LAD','MIA','MIL','MIN','NYM','NYY','OAK','PHI','PIT','SD','SEA','SF','STL','TB','TEX','TOR','WSH']
abbrevs = {'ARI': 109, 'ATL': 144,'BAL': 110,'BOS': 111,'CHC': 112,'CIN': 113,'CLE': 114,'COL': 115,'CWS': 145,'DET': 116,'HOU': 117,'KC': 118,'LAA': 108,'LAD': 119,'MIA': 146,'MIL': 158,'MIN': 142,'NYM': 121,'NYY': 147,'OAK': 133,'PHI': 143,'PIT': 134,'SD': 135,'SEA': 136,'SF': 137,'STL': 138,'TB': 139,'TEX': 140,'TOR': 141,'WSH': 120}
year = '2023'
type = 'hitters'

def file(teamAbbrev, year, type):
    if path.exists("Teams/" + teamAbbrev + "/" + year):
        with open("Teams/" + teamAbbrev + "/" + year + "/" + type + ".txt", "r") as FILE:
            content = FILE.read()
            try:
                players = eval(content)
            except Exception as e:
                print("1. We got an error ", e)
    return players

def read(teamAbbrev, year, playername):
    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "r") as f:
        content = f.read()
        try:
            data = eval(content)
        except Exception as e:
            print("2. We got an error", e)
    return data

def readDateList(teamAbbrev, year, playername):
    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "r") as f:
        content = f.read()
        try:
            data = eval(content)
            dates = data[playername]['pitching']['dates']
        except Exception as e:
            print("2. We got an error", e)
    return dates

def addCategoryToDict(teamAbbrev, year, playername, data, gameDate, category):
    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "w") as f:
        try:
            try:
                data[playername]['pitching']['per_game']['inherited runners'].append(category)
                print(str(category) + " added to " + playername + " on " + gameDate)
            except KeyError:
                data[playername]['pitching']['per_game']['inherited runners'] = []
                data[playername]['pitching']['per_game']['inherited runners'].append(category)
                print(str(category) + " added to " + playername + " on " + gameDate)
            f.write(str(data))
        except Exception as e:
            print("3. We got an error", e)

# for teamAbbrev in teams:
#     players = file(teamAbbrev, year, type)
#     for playername in players['players']:
#         data = read(teamAbbrev, year, playername)
#         addCategoryToDict(teamAbbrev, year, playername, data)
#         print(data)

# def add(homeOrAway, boxscore, ID, category):
#     index = boxscore['teams'][homeOrAway]['players'][ID]
#     if index['stats']['pitching']['numberOfPitches'] != 0:
#         pg_inheritedRunners = index['stats']['pitching']['inheritedRunners']
#         category.append(pg_inheritedRunners)


for teamAbbrev in teams:
    players = file(teamAbbrev, year, type)
    for playername in players['players']:
        data = read(teamAbbrev, year, playername)
        dates = readDateList(teamAbbrev, year, playername)
        playerID = data[playername]['ID']
        sched = statsapi.schedule(start_date= '07/23/2020', end_date = '07/26/2020', team = abbrevs[teamAbbrev])
        for game in sched:
            gameId = game["game_id"]
            gameDate = game["game_date"]
            gameData = statsapi.get('game', {'gamePk': gameId})
            boxscore = gameData['liveData']['boxscore']
            homeId = game["home_id"]
            awayId = game["away_id"]
            homeAbbrev = statsapi.get('team', {'teamId': homeId})['teams'][0]['abbreviation']
            awayAbbrev = statsapi.get('team', {'teamId': awayId})['teams'][0]['abbreviation']

            if game['game_type'] == "R":
                awayPlayers = boxscore['teams']['away']['players']
                homePlayers = boxscore['teams']['home']['players']
                for ID in homePlayers:
                    if ID == playerID:
                        if homePlayers[ID]['stats']['pitching'] != {}:
                            pg_inheritedRunners = boxscore['teams']['home']['players'][ID]['stats']['pitching']['inheritedRunners']
                            addCategoryToDict(teamAbbrev, year, playername, data, gameDate, pg_inheritedRunners)
                for ID in awayPlayers:
                    if ID == playerID:
                        if awayPlayers[ID]['stats']['pitching'] != {}:
                            pg_inheritedRunners = boxscore['teams']['away']['players'][ID]['stats']['pitching']['inheritedRunners']
                            addCategoryToDict(teamAbbrev, year, playername, data, gameDate,pg_inheritedRunners)


