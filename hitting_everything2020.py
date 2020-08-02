from os import path
import statsapi
import datetime

def hitting_everything2020():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    sched = statsapi.schedule(start_date= yesterday, end_date = tomorrow, team=137)
    for i in range(len(sched)):
        gameId = sched[i]["game_id"]
        game_date = sched[i]["game_date"]
        scoredata = statsapi.boxscore_data(gameId)
        if path.exists("2020/h_dates.txt"):
            with open("2020/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
        else:
            with open("2020/h_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open("2020/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
        if game_date not in content_dict['dates'] and (sched[i]['status'] == "Final" or sched[i]['status'] == "Game Over"):
            if sched[i]["game_type"] == "R":
                for ID in scoredata['playerInfo']:
                    if sched[i]['home_name'] == "San Francisco Giants":
                        if ID in scoredata['home']['players']:
                            if scoredata['home']['players'][ID]['stats']['batting'] != {}:
                                h_add(game_date, scoredata, ID)
                    else:
                        if ID in scoredata['away']['players']:
                            if scoredata['away']['players'][ID]['stats']['batting'] != {}:
                                a_add(game_date, scoredata, ID)
                with open("2020/h_dates.txt", "w") as f:
                    try:
                        content_dict['dates'].append(game_date)
                        f.write(str(content_dict))
                    except Exception as e:
                        print("we got an error ", e)
                        print("Database Error ")

def h_add(game_date, scoredata, ID):
    index = scoredata['home']['players'][ID]
    playername = scoredata['playerInfo'][ID]['fullName']
    if playername == 'Michael Yastrzemski':
        playername = 'Mike Yastrzemski'
    # progressive
    p_averages = float(index['seasonStats']['batting']['avg'])
    p_obp = float(index['seasonStats']['batting']['obp'])
    p_slg = float(index['seasonStats']['batting']['slg'])
    p_ops = float(index['seasonStats']['batting']['ops'])
    p_runs = int(index['seasonStats']['batting']['runs'])
    p_doubles = int(index['seasonStats']['batting']['doubles'])
    p_triples = int(index['seasonStats']['batting']['triples'])
    p_homeruns = int(index['seasonStats']['batting']['homeRuns'])
    p_strikeouts = int(index['seasonStats']['batting']['strikeOuts'])
    p_walks = int(index['seasonStats']['batting']['baseOnBalls'])
    p_hits = int(index['seasonStats']['batting']['hits'])
    p_ab = int(index['seasonStats']['batting']['atBats'])
    p_sb = int(index['seasonStats']['batting']['stolenBases'])
    p_rbi = int(index['seasonStats']['batting']['rbi'])
    p_lob = int(index['seasonStats']['batting']['leftOnBase'])
    # per game
    pg_ab = index['stats']['batting']['atBats']
    pg_strikeouts = index['stats']['batting']['strikeOuts']
    pg_hits = index['stats']['batting']['hits']
    pg_walks = index['stats']['batting']['baseOnBalls']
    pg_runs = index['stats']['batting']['runs']
    pg_rbi = index['stats']['batting']['rbi']
    pg_sb = index['stats']['batting']['stolenBases']
    pg_lob = index['stats']['batting']['leftOnBase']
    pg_doubles = index['stats']['batting']['doubles']
    pg_triples = index['stats']['batting']['triples']
    pg_homeruns = index['stats']['batting']['homeRuns']

    p_categories = [p_averages, p_obp, p_slg, p_ops, p_runs, p_doubles, p_triples, p_homeruns, p_strikeouts, p_walks,
                    p_hits, p_ab, p_sb, p_rbi, p_lob]
    pg_categories = [pg_ab, pg_strikeouts, pg_hits, pg_walks, pg_runs, pg_rbi, pg_sb, pg_lob, pg_doubles, pg_triples,
                     pg_homeruns]
    p_names = ['averages', 'obp', 'slg', 'ops', 'runs', 'doubles', 'triples', 'homeruns', 'strikeouts', 'walks', 'hits',
               'ab', 'sb', 'rbi', 'lob']
    pg_names = ['ab', 'strikeouts', 'hits', 'walks', 'runs', 'rbi', 'sb', 'lob', 'doubles', 'triples', 'homeruns']

    if path.exists("2020/" + playername + ".txt"):
        print("============================================")
        print("File Exists For", playername)
        with open("2020/" + str(playername) + ".txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
            else:
                print("Read success for", playername)
    else:
        if scoredata['home']['players'][ID]['position']['abbreviation'] == 'P':
            print("============================================")
            print("Creating File For Pitcher", playername)
            with open("2020/" + str(playername) + ".txt", "w") as f:
                f.write(
                    "{'" + playername + "': {'ID':'" + ID + "', '2020': { 'pitching' : {'dates': [], 'progression': {'era': [], 'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'doubles': [], 'triples': [], 'ab': [], 'obp': [], 'wins': [], 'losses': [], 'holds': [], 'blown_saves': []}, 'per_game': {'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'pitches': [], 'strikes': []}}, 'hitting': {'dates': [], 'progression': {'averages': [], 'obp': [], 'slg': [], 'ops': [], 'runs': [], 'doubles': [], 'triples': [], 'homeruns': [], 'strikeouts': [], 'walks': [], 'hits': [], 'ab': [], 'sb': [], 'rbi': [], 'lob': []}, 'per_game': {'ab': [], 'strikeouts': [], 'hits': [], 'walks': [], 'runs': [], 'rbi': [], 'sb': [], 'lob': [], 'doubles': [], 'triples': [], 'homeruns': []}}}}}")
            with open("2020/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)
        else:
            print("============================================")
            print("Creating File For Hitter", playername)
            with open("2020/" + str(playername) + ".txt", "w") as f:
                f.write(
                    "{'" + playername + "': {'ID':'" + ID + "', '2020': { 'hitting' : {'dates': [], 'progression': {'averages': [], 'obp': [], 'slg': [], 'ops': [], 'runs': [], 'doubles': [], 'triples': [], 'homeruns': [], 'strikeouts': [], 'walks': [], 'hits': [], 'ab': [], 'sb': [], 'rbi': [], 'lob': []}, 'per_game': {'ab': [], 'strikeouts': [], 'hits': [], 'walks': [], 'runs': [], 'rbi': [], 'sb': [], 'lob': [], 'doubles': [], 'triples': [], 'homeruns': []}}, 'pitching': {'dates': [], 'progression': {'era': [], 'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'doubles': [], 'triples': [], 'ab': [], 'obp': [], 'wins': [], 'losses': [], 'holds': [], 'blown_saves': []}, 'per_game': {'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'pitches': [], 'strikes': []}}}}}")
            with open("2020/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)

    if game_date not in content_dict[playername]['2020']['hitting']['dates']:
        print("-----Stats not added yet for", game_date + "-----")
        with open("2020/" + str(playername) + ".txt", "w") as f:
            try:
                content_dict[playername]['2020']['hitting']['dates'].append(game_date)
                for i in range(len(p_categories)):
                    content_dict[playername]['2020']['hitting']['progression'][p_names[i]].append(p_categories[i])
                    print(p_names[i], "(p) added to " + playername)
                for i in range(len(pg_categories)):
                    content_dict[playername]['2020']['hitting']['per_game'][pg_names[i]].append(pg_categories[i])
                    print(pg_names[i], "(pg) added to " + playername)
                f.write(str(content_dict))
                print("============================================")
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
    else:
        print("-----Stats already added for", game_date + "-----")
        print("============================================")

    if path.exists("2020/hitters.txt"):
        with open("2020/hitters.txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
    else:
        with open("2020/hitters.txt", "w") as FILE:
            FILE.write("{'players':[]}")
        with open("2020/hitters.txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")

    if playername not in content_dict['players']:
        with open("2020/hitters.txt", "w") as f:
            try:
                content_dict['players'].append(playername)
                content_dict['players'].sort()
                f.write(str(content_dict))
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")

def a_add(game_date, scoredata, ID):
    index = scoredata['away']['players'][ID]
    playername = scoredata['playerInfo'][ID]['fullName']
    if playername == 'Michael Yastrzemski':
        playername = 'Mike Yastrzemski'
    # progressive
    p_averages = float(index['seasonStats']['batting']['avg'])
    p_obp = float(index['seasonStats']['batting']['obp'])
    p_slg = float(index['seasonStats']['batting']['slg'])
    p_ops = float(index['seasonStats']['batting']['ops'])
    p_runs = int(index['seasonStats']['batting']['runs'])
    p_doubles = int(index['seasonStats']['batting']['doubles'])
    p_triples = int(index['seasonStats']['batting']['triples'])
    p_homeruns = int(index['seasonStats']['batting']['homeRuns'])
    p_strikeouts = int(index['seasonStats']['batting']['strikeOuts'])
    p_walks = int(index['seasonStats']['batting']['baseOnBalls'])
    p_hits = int(index['seasonStats']['batting']['hits'])
    p_ab = int(index['seasonStats']['batting']['atBats'])
    p_sb = int(index['seasonStats']['batting']['stolenBases'])
    p_rbi = int(index['seasonStats']['batting']['rbi'])
    p_lob = int(index['seasonStats']['batting']['leftOnBase'])
    # per game
    pg_ab = index['stats']['batting']['atBats']
    pg_strikeouts = index['stats']['batting']['strikeOuts']
    pg_hits = index['stats']['batting']['hits']
    pg_walks = index['stats']['batting']['baseOnBalls']
    pg_runs = index['stats']['batting']['runs']
    pg_rbi = index['stats']['batting']['rbi']
    pg_sb = index['stats']['batting']['stolenBases']
    pg_lob = index['stats']['batting']['leftOnBase']
    pg_doubles = index['stats']['batting']['doubles']
    pg_triples = index['stats']['batting']['triples']
    pg_homeruns = index['stats']['batting']['homeRuns']

    p_categories = [p_averages, p_obp, p_slg, p_ops, p_runs, p_doubles, p_triples, p_homeruns, p_strikeouts, p_walks,
                    p_hits, p_ab, p_sb, p_rbi, p_lob]
    pg_categories = [pg_ab, pg_strikeouts, pg_hits, pg_walks, pg_runs, pg_rbi, pg_sb, pg_lob, pg_doubles, pg_triples,
                     pg_homeruns]
    p_names = ['averages', 'obp', 'slg', 'ops', 'runs', 'doubles', 'triples', 'homeruns', 'strikeouts', 'walks', 'hits',
               'ab', 'sb', 'rbi', 'lob']
    pg_names = ['ab', 'strikeouts', 'hits', 'walks', 'runs', 'rbi', 'sb', 'lob', 'doubles', 'triples', 'homeruns']

    if path.exists("2020/" + playername + ".txt"):
        print("============================================")
        print("File Exists For", playername)
        with open("2020/" + str(playername) + ".txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
            else:
                print("Read success for", playername)
    else:
        if scoredata['away']['players'][ID]['position']['abbreviation'] == 'P':
            print("============================================")
            print("Creating File For Pitcher", playername)
            with open("2020/" + str(playername) + ".txt", "w") as f:
                f.write(
                    "{'" + playername + "': {'ID':'" + ID + "', '2020': { 'pitching' : {'dates': [], 'progression': {'era': [], 'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'doubles': [], 'triples': [], 'ab': [], 'obp': [], 'wins': [], 'losses': [], 'holds': [], 'blown_saves': []}, 'per_game': {'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'pitches': [], 'strikes': []}}, 'hitting': {'dates': [], 'progression': {'averages': [], 'obp': [], 'slg': [], 'ops': [], 'runs': [], 'doubles': [], 'triples': [], 'homeruns': [], 'strikeouts': [], 'walks': [], 'hits': [], 'ab': [], 'sb': [], 'rbi': [], 'lob': []}, 'per_game': {'ab': [], 'strikeouts': [], 'hits': [], 'walks': [], 'runs': [], 'rbi': [], 'sb': [], 'lob': [], 'doubles': [], 'triples': [], 'homeruns': []}}}}}")
            with open("2020/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)
        else:
            print("============================================")
            print("Creating File For Hitter", playername)
            with open("2020/" + str(playername) + ".txt", "w") as f:
                f.write(
                    "{'" + playername + "': {'ID':'" + ID + "', '2020': { 'hitting' : {'dates': [], 'progression': {'averages': [], 'obp': [], 'slg': [], 'ops': [], 'runs': [], 'doubles': [], 'triples': [], 'homeruns': [], 'strikeouts': [], 'walks': [], 'hits': [], 'ab': [], 'sb': [], 'rbi': [], 'lob': []}, 'per_game': {'ab': [], 'strikeouts': [], 'hits': [], 'walks': [], 'runs': [], 'rbi': [], 'sb': [], 'lob': [], 'doubles': [], 'triples': [], 'homeruns': []}}, 'pitching': {'dates': [], 'progression': {'era': [], 'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'doubles': [], 'triples': [], 'ab': [], 'obp': [], 'wins': [], 'losses': [], 'holds': [], 'blown_saves': []}, 'per_game': {'innings': [], 'hits': [], 'runs': [], 'earned_runs': [], 'walks': [], 'strikeouts': [], 'homeruns': [], 'pitches': [], 'strikes': []}}}}}")
            with open("2020/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)

    if game_date not in content_dict[playername]['2020']['hitting']['dates']:
        print("-----Stats not added yet for", game_date + "-----")
        with open("2020/" + str(playername) + ".txt", "w") as f:
            try:
                content_dict[playername]['2020']['hitting']['dates'].append(game_date)
                for i in range(len(p_categories)):
                    content_dict[playername]['2020']['hitting']['progression'][p_names[i]].append(p_categories[i])
                    print(p_names[i], "(p) added to " + playername)
                for i in range(len(pg_categories)):
                    content_dict[playername]['2020']['hitting']['per_game'][pg_names[i]].append(pg_categories[i])
                    print(pg_names[i], "(pg) added to " + playername)
                f.write(str(content_dict))
                print("============================================")
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
    else:
        print("-----Stats already added for", game_date + "-----")
        print("============================================")

    if path.exists("2020/hitters.txt"):
        with open("2020/hitters.txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")
    else:
        with open("2020/hitters.txt", "w") as FILE:
            FILE.write("{'players':[]}")
        with open("2020/hitters.txt", "r") as FILE:
            content = FILE.read()
            try:
                content_dict = eval(content)
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")

    if playername not in content_dict['players']:
        with open("2020/hitters.txt", "w") as f:
            try:
                content_dict['players'].append(playername)
                content_dict['players'].sort()
                f.write(str(content_dict))
            except Exception as e:
                print("we got an error ", e)
                print("Database Error ")