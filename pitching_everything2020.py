from os import path
import statsapi

def pitching_everything2020():
    sched = statsapi.schedule(start_date='07/23/2020', end_date='09/27/2020', team=137)
    for i in range(len(sched)):
        gameId = sched[i]["game_id"]
        game_date = sched[i]["game_date"]
        scoredata = statsapi.boxscore_data(gameId)
        if sched[i]["game_type"] == "R" and sched[i]['status']=="Final":
            for ID in scoredata['playerInfo']:
                if sched[i]['home_name'] == "San Francisco Giants":
                    if ID in scoredata['home']['players']:
                        if scoredata['home']['players'][ID]['stats']['pitching'] != {}:
                            if scoredata['home']['players'][ID]['position']['abbreviation'] == 'P':
                                h_add(game_date, scoredata, ID)
                else:
                    if ID in scoredata['away']['players']:
                        if scoredata['away']['players'][ID]['stats']['pitching'] != {}:
                            if scoredata['away']['players'][ID]['position']['abbreviation'] == 'P':
                                a_add(game_date, scoredata, ID)


def h_add(game_date, scoredata, ID):
    index = scoredata['home']['players'][ID]
    playername = scoredata['playerInfo'][ID]['fullName']
    # progressive
    p_era = float(index['seasonStats']['pitching']['era'])
    p_innings = float(index['seasonStats']['pitching']['inningsPitched'])
    p_hits = int(index['seasonStats']['pitching']['hits'])
    p_runs = int(index['seasonStats']['pitching']['runs'])
    p_earned_runs = int(index['seasonStats']['pitching']['earnedRuns'])
    p_walks = int(index['seasonStats']['pitching']['baseOnBalls'])
    p_strikeouts = int(index['seasonStats']['pitching']['strikeOuts'])
    p_homeruns = int(index['seasonStats']['pitching']['homeRuns'])
    p_doubles = int(index['seasonStats']['pitching']['doubles'])
    p_triples = int(index['seasonStats']['pitching']['triples'])
    p_ab = int(index['seasonStats']['pitching']['atBats'])
    p_obp = float(index['seasonStats']['pitching']['obp'])
    p_wins = int(index['seasonStats']['pitching']['wins'])
    p_losses = int(index['seasonStats']['pitching']['losses'])
    p_holds = int(index['seasonStats']['pitching']['holds'])
    p_blown_saves = int(index['seasonStats']['pitching']['blownSaves'])
    # per game
    pg_innings = float(index['stats']['pitching']['inningsPitched'])
    pg_hits = int(index['stats']['pitching']['hits'])
    pg_runs = int(index['stats']['pitching']['runs'])
    pg_earned_runs = int(index['stats']['pitching']['earnedRuns'])
    pg_walks = int(index['stats']['pitching']['baseOnBalls'])
    pg_strikeouts = int(index['stats']['pitching']['strikeOuts'])
    pg_homeruns = int(index['stats']['pitching']['homeRuns'])
    pg_pitches = int(index['stats']['pitching']['pitchesThrown'])
    pg_strikes = int(index['stats']['pitching']['strikes'])

    p_categories = [p_era, p_innings, p_hits, p_runs, p_earned_runs, p_walks, p_strikeouts, p_homeruns, p_doubles,
                    p_triples, p_ab, p_obp, p_wins, p_losses, p_holds, p_blown_saves]
    pg_categories = [pg_innings, pg_hits, pg_runs, pg_earned_runs, pg_walks, pg_strikeouts, pg_homeruns, pg_pitches,
                     pg_strikes]
    p_names = ['era', 'innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'doubles', 'triples',
               'ab', 'obp', 'wins', 'losses', 'holds', 'blown_saves']
    pg_names = ['innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'pitches', 'strikes']

    if path.exists("2020/" + playername + ".txt"):
        print("File Exists For", playername)
        with open("2020/" + str(playername) + ".txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
            else:
                print("read success for", playername)
    else:
        print("Creating File For Pitcher", playername)
        with open("2020/" + str(playername) + ".txt", "w") as f:
            f.write(
                "{'" + playername + "': {'ID':'" + ID + "', '2020': { 'pitching' : {'dates': [], 'progression': {'era': [], 'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'doubles': [], 'triples': [], 'ab': [], 'obp': [], 'wins': [], 'losses': [], 'holds': [], 'blown_saves': []}, 'per_game': {'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'pitches': [], 'strikes': []}}, 'hitting': {'dates': [], 'progression': {'averages': [], 'obp': [], 'slg': [], 'ops': [], 'runs': [], 'doubles': [], 'triples': [], 'homeruns': [], 'strikeouts': [], 'walks': [], 'hits': [], 'ab': [], 'sb': [], 'rbi': [], 'lob': []}, 'per_game': {'ab': [], 'strikeouts': [], 'hits': [], 'walks': [], 'runs': [], 'rbi': [], 'sb': [], 'lob': [], 'doubles': [], 'triples': [], 'homeruns': []}}}}}")
        with open("2020/" + str(playername) + ".txt", "r") as FILE:
            content = FILE.read()
            content_dict = eval(content)

    if game_date not in content_dict[playername]['2020']['pitching']['dates']:
        print("Yes")
        with open("2020/" + str(playername) + ".txt", "w") as f:
            try:
                content_dict[playername]['2020']['pitching']['dates'].append(game_date)
                for i in range(len(p_categories)):
                    content_dict[playername]['2020']['pitching']['progression'][p_names[i]].append(p_categories[i])
                for i in range(len(pg_categories)):
                    content_dict[playername]['2020']['pitching']['per_game'][pg_names[i]].append(pg_categories[i])
                f.write(str(content_dict))
                print("Write Success")
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")


def a_add(game_date, scoredata, ID):
    index = scoredata['away']['players'][ID]
    playername = scoredata['playerInfo'][ID]['fullName']
    # progressive
    p_era = float(index['seasonStats']['pitching']['era'])
    p_innings = float(index['seasonStats']['pitching']['inningsPitched'])
    p_hits = int(index['seasonStats']['pitching']['hits'])
    p_runs = int(index['seasonStats']['pitching']['runs'])
    p_earned_runs = int(index['seasonStats']['pitching']['earnedRuns'])
    p_walks = int(index['seasonStats']['pitching']['baseOnBalls'])
    p_strikeouts = int(index['seasonStats']['pitching']['strikeOuts'])
    p_homeruns = int(index['seasonStats']['pitching']['homeRuns'])
    p_doubles = int(index['seasonStats']['pitching']['doubles'])
    p_triples = int(index['seasonStats']['pitching']['triples'])
    p_ab = int(index['seasonStats']['pitching']['atBats'])
    p_obp = float(index['seasonStats']['pitching']['obp'])
    p_wins = int(index['seasonStats']['pitching']['wins'])
    p_losses = int(index['seasonStats']['pitching']['losses'])
    p_holds = int(index['seasonStats']['pitching']['holds'])
    p_blown_saves = int(index['seasonStats']['pitching']['blownSaves'])
    # per game
    pg_innings = float(index['stats']['pitching']['inningsPitched'])
    pg_hits = int(index['stats']['pitching']['hits'])
    pg_runs = int(index['stats']['pitching']['runs'])
    pg_earned_runs = int(index['stats']['pitching']['earnedRuns'])
    pg_walks = int(index['stats']['pitching']['baseOnBalls'])
    pg_strikeouts = int(index['stats']['pitching']['strikeOuts'])
    pg_homeruns = int(index['stats']['pitching']['homeRuns'])
    pg_pitches = int(index['stats']['pitching']['pitchesThrown'])
    pg_strikes = int(index['stats']['pitching']['strikes'])

    p_categories = [p_era, p_innings, p_hits, p_runs, p_earned_runs, p_walks, p_strikeouts, p_homeruns, p_doubles,
                    p_triples, p_ab, p_obp, p_wins, p_losses, p_holds, p_blown_saves]
    pg_categories = [pg_innings, pg_hits, pg_runs, pg_earned_runs, pg_walks, pg_strikeouts, pg_homeruns, pg_pitches,
                     pg_strikes]
    p_names = ['era', 'innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'doubles', 'triples',
               'ab', 'obp', 'wins', 'losses', 'holds', 'blown_saves']
    pg_names = ['innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'pitches', 'strikes']

    if path.exists("2020/" + playername + ".txt"):
        print("File Exists For", playername)
        with open("2020/" + str(playername) + ".txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
            else:
                print("read success for", playername)
    else:
        print("Creating File For Pitcher", playername)
        with open("2020/" + str(playername) + ".txt", "w") as f:
            f.write(
                "{'" + playername + "': {'ID':'" + ID + "', '2020': { 'pitching' : {'dates': [], 'progression': {'era': [], 'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'doubles': [], 'triples': [], 'ab': [], 'obp': [], 'wins': [], 'losses': [], 'holds': [], 'blown_saves': []}, 'per_game': {'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'pitches': [], 'strikes': []}}, 'hitting': {'dates': [], 'progression': {'averages': [], 'obp': [], 'slg': [], 'ops': [], 'runs': [], 'doubles': [], 'triples': [], 'homeruns': [], 'strikeouts': [], 'walks': [], 'hits': [], 'ab': [], 'sb': [], 'rbi': [], 'lob': []}, 'per_game': {'ab': [], 'strikeouts': [], 'hits': [], 'walks': [], 'runs': [], 'rbi': [], 'sb': [], 'lob': [], 'doubles': [], 'triples': [], 'homeruns': []}}}}}")
        with open("2020/" + str(playername) + ".txt", "r") as FILE:
            content = FILE.read()
            content_dict = eval(content)

    if game_date not in content_dict[playername]['2020']['pitching']['dates']:
        print("Yes")
        with open("2020/" + str(playername) + ".txt", "w") as f:
            try:
                content_dict[playername]['2020']['pitching']['dates'].append(game_date)
                for i in range(len(p_categories)):
                    content_dict[playername]['2020']['pitching']['progression'][p_names[i]].append(p_categories[i])
                for i in range(len(pg_categories)):
                    content_dict[playername]['2020']['pitching']['per_game'][pg_names[i]].append(pg_categories[i])
                f.write(str(content_dict))
                print("Write Success")
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
