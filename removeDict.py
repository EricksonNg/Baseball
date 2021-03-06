from os import path

teams = ['ARI','ATL','BAL','BOS','CHC','CIN','CLE','COL','CWS','DET','HOU','KC','LAA','LAD','MIA','MIL','MIN','NYM','NYY','OAK','PHI','PIT','SD','SEA','SF','STL','TB','TEX','TOR','WSH']
abbrevs = {'ARI': 109, 'ATL': 144,'BAL': 110,'BOS': 111,'CHC': 112,'CIN': 113,'CLE': 114,'COL': 115,'CWS': 145,'DET': 116,'HOU': 117,'KC': 118,'LAA': 108,'LAD': 119,'MIA': 146,'MIL': 158,'MIN': 142,'NYM': 121,'NYY': 147,'OAK': 133,'PHI': 143,'PIT': 134,'SD': 135,'SEA': 136,'SF': 137,'STL': 138,'TB': 139,'TEX': 140,'TOR': 141,'WSH': 120}
year = '2020'
type = 'fielders'

def file(teamAbbrev, year, type):
    if path.exists("Teams/" + teamAbbrev + "/" + year):
        with open("Teams/" + teamAbbrev + "/" + year + "/" + type + ".txt", "r") as FILE:
            content = FILE.read()
            try:
                players = eval(content)
            except Exception as e:
                print("1. We got an error ", e)
    return players

def removeHittingDict(teamAbbrev, year, playername):
    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "r") as f:
        content = f.read()
        try:
            data = eval(content)
        except Exception as e:
            print("2. We got an error", e)

    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "w") as f:
        data[playername]['hitting']['dates'] = [] # dates list
        data[playername]['hitting']['progression'] = {} # progression dict
        data[playername]['hitting']['per_game'] = {} # per game dict
        f.write(str(data))

def removeFieldingDict(teamAbbrev, year, playername):
    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "r") as f:
        content = f.read()
        try:
            data = eval(content)
        except Exception as e:
            print("2. We got an error", e)

    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "w") as f:
        data[playername]['fielding'] = {"dates": [], "positions": [], "progression": {}, "per_game": {}}
        f.write(str(data))

def removeSpecificCategory(teamAbbrev, year, playername):
    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "r") as f:
        content = f.read()
        try:
            data = eval(content) # accesses the dictionary in the file (basically what the whole file is)
        except Exception as e:
            print("2. We got an error", e)

    with open("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt", "w") as f:
        # Example(between the {} is needed info to remove key): {index dictionary to where key is located}.pop({key}, None)
        data[playername]['hitting']['per_game'].pop('ab per hr', None) # data[playername]['hitting']['per_game'] is where 'ab per hr' is located, so that's what goes before the .pop
        f.write(str(data)) # rewrite the file to officially remove the key

for teamAbbrev in teams:
    players = file(teamAbbrev, year, type)
    for playername in players['players']:
        # removeFieldingDict(teamAbbrev, year, playername)
        print(playername)

