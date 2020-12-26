from os import path, makedirs
import statsapi
import datetime

def everythingBefore():
    year = '2018'
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=2)
    tomorrow = today + datetime.timedelta(days=1)
    sched = statsapi.schedule(start_date= '03/28/'+year, end_date = '10/05/'+year)
    for game in sched:
        gameId = game["game_id"]
        boxscore = statsapi.boxscore_data(gameId)
        gameDate = game["game_date"]
        if game['doubleheader'] != 'N':
            gameDate = game["game_date"] + "(" + str(game["game_num"]) + ")" #adds number to the back of the game date if the game is a part of a doubleheader

        homeId = game["home_id"]
        awayId = game["away_id"]
        homeAbbrev = statsapi.get('team', {'teamId':homeId})['teams'][0]['abbreviation']
        awayAbbrev = statsapi.get('team', {'teamId':awayId})['teams'][0]['abbreviation']

        if game['game_type'] == "R":
            createDir(homeAbbrev, year) #if needed
            createDir(awayAbbrev, year) #if needed

            hit(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore)
            pitch(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore)
        else:
            print(game['game_type'])

def createDir(teamAbbrev, year):
    if path.exists("Teams/" + teamAbbrev + "/" + year):
        print(year + " " + teamAbbrev + " directory exists")
    else:
        makedirs("Teams/" + teamAbbrev + "/" + year)
        print(year + " " + teamAbbrev + " directory created")

def hit(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore):

    def h_add(gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['home']['players'][ID]
        playername = boxscore['playerInfo'][ID]['fullName']
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

        p_categories = [p_averages, p_obp, p_slg, p_ops, p_runs, p_doubles, p_triples, p_homeruns, p_strikeouts,
                        p_walks, p_hits, p_ab, p_sb, p_rbi, p_lob]
        pg_categories = [pg_ab, pg_strikeouts, pg_hits, pg_walks, pg_runs, pg_rbi, pg_sb, pg_lob, pg_doubles,
                         pg_triples, pg_homeruns]
        p_names = ['averages', 'obp', 'slg', 'ops', 'runs', 'doubles', 'triples', 'homeruns', 'strikeouts', 'walks',
                   'hits', 'ab', 'sb', 'rbi', 'lob']
        pg_names = ['ab', 'strikeouts', 'hits', 'walks', 'runs', 'rbi', 'sb', 'lob', 'doubles', 'triples', 'homeruns']

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("4. We have an error", e)
                    print("Database Error ")
        else:
            if boxscore['home']['players'][ID]['position']['abbreviation'] == 'P':
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "' + year + '": { "pitching" : {"dates": [], "progression": {"era": [], "innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "doubles": [], "triples": [], "ab": [], "obp": [], "wins": [], "losses": [], "holds": [], "blown_saves": []}, "per_game": {"innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "pitches": [], "strikes": []}}, "hitting": {"dates": [], "progression": {"averages": [], "obp": [], "slg": [], "ops": [], "runs": [], "doubles": [], "triples": [], "homeruns": [], "strikeouts": [], "walks": [], "hits": [], "ab": [], "sb": [], "rbi": [], "lob": []}, "per_game": {"ab": [], "strikeouts": [], "hits": [], "walks": [], "runs": [], "rbi": [], "sb": [], "lob": [], "doubles": [], "triples": [], "homeruns": []}}}}}')
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
            else:
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "' + year + '": { "hitting" : {"dates": [], "progression": {"averages": [], "obp": [], "slg": [], "ops": [], "runs": [], "doubles": [], "triples": [], "homeruns": [], "strikeouts": [], "walks": [], "hits": [], "ab": [], "sb": [], "rbi": [], "lob": []}, "per_game": {"ab": [], "strikeouts": [], "hits": [], "walks": [], "runs": [], "rbi": [], "sb": [], "lob": [], "doubles": [], "triples": [], "homeruns": []}}, "pitching": {"dates": [], "progression": {"era": [], "innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "doubles": [], "triples": [], "ab": [], "obp": [], "wins": [], "losses": [], "holds": [], "blown_saves": []}, "per_game": {"innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "pitches": [], "strikes": []}}}}}')
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)

        if gameDate not in content_dict[playername][year]['hitting']['dates']:
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                try:
                    content_dict[playername][year]['hitting']['dates'].append(gameDate)
                    for i in range(len(p_categories)):
                        content_dict[playername][year]['hitting']['progression'][p_names[i]].append(p_categories[i])
                    for i in range(len(pg_categories)):
                        content_dict[playername][year]['hitting']['per_game'][pg_names[i]].append(pg_categories[i])
                    f.write(str(content_dict))
                    print("Stats added for " + playername + " for " + gameDate)
                except Exception as e:
                    print("5. We have an error", e)
                    print("Database Error ")

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/hitters.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("6. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("7. We have an error", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as f:
                try:
                    content_dict['players'].append(playername)
                    content_dict['players'].sort()
                    f.write(str(content_dict))
                except Exception as e:
                    print("8. We have an error", e)
                    print("Database Error ")

    def a_add(gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['away']['players'][ID]
        playername = boxscore['playerInfo'][ID]['fullName']
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

        p_categories = [p_averages, p_obp, p_slg, p_ops, p_runs, p_doubles, p_triples, p_homeruns, p_strikeouts,
                        p_walks,
                        p_hits, p_ab, p_sb, p_rbi, p_lob]
        pg_categories = [pg_ab, pg_strikeouts, pg_hits, pg_walks, pg_runs, pg_rbi, pg_sb, pg_lob, pg_doubles,
                         pg_triples,
                         pg_homeruns]
        p_names = ['averages', 'obp', 'slg', 'ops', 'runs', 'doubles', 'triples', 'homeruns', 'strikeouts', 'walks',
                   'hits',
                   'ab', 'sb', 'rbi', 'lob']
        pg_names = ['ab', 'strikeouts', 'hits', 'walks', 'runs', 'rbi', 'sb', 'lob', 'doubles', 'triples', 'homeruns']

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("9. We have an error", e)
                    print("Database Error ")
        else:
            if boxscore['away']['players'][ID]['position']['abbreviation'] == 'P':
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "' + year + '": { "pitching" : {"dates": [], "progression": {"era": [], "innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "doubles": [], "triples": [], "ab": [], "obp": [], "wins": [], "losses": [], "holds": [], "blown_saves": []}, "per_game": {"innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "pitches": [], "strikes": []}}, "hitting": {"dates": [], "progression": {"averages": [], "obp": [], "slg": [], "ops": [], "runs": [], "doubles": [], "triples": [], "homeruns": [], "strikeouts": [], "walks": [], "hits": [], "ab": [], "sb": [], "rbi": [], "lob": []}, "per_game": {"ab": [], "strikeouts": [], "hits": [], "walks": [], "runs": [], "rbi": [], "sb": [], "lob": [], "doubles": [], "triples": [], "homeruns": []}}}}}')
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
            else:
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "' + year + '": { "hitting" : {"dates": [], "progression": {"averages": [], "obp": [], "slg": [], "ops": [], "runs": [], "doubles": [], "triples": [], "homeruns": [], "strikeouts": [], "walks": [], "hits": [], "ab": [], "sb": [], "rbi": [], "lob": []}, "per_game": {"ab": [], "strikeouts": [], "hits": [], "walks": [], "runs": [], "rbi": [], "sb": [], "lob": [], "doubles": [], "triples": [], "homeruns": []}}, "pitching": {"dates": [], "progression": {"era": [], "innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "doubles": [], "triples": [], "ab": [], "obp": [], "wins": [], "losses": [], "holds": [], "blown_saves": []}, "per_game": {"innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "pitches": [], "strikes": []}}}}}')
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)

        if gameDate not in content_dict[playername][year]['hitting']['dates']:
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                try:
                    content_dict[playername][year]['hitting']['dates'].append(gameDate)
                    for i in range(len(p_categories)):
                        content_dict[playername][year]['hitting']['progression'][p_names[i]].append(p_categories[i])
                    for i in range(len(pg_categories)):
                        content_dict[playername][year]['hitting']['per_game'][pg_names[i]].append(pg_categories[i])
                    f.write(str(content_dict))
                    print("Stats added for " + playername + " for " + gameDate)
                except Exception as e:
                    print("10. We have an error", e)
                    print("Database Error ")

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/hitters.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("11. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("12. We have an error", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as f:
                try:
                    content_dict['players'].append(playername)
                    content_dict['players'].sort()
                    f.write(str(content_dict))
                except Exception as e:
                    print("13. We have an error", e)
                    print("Database Error ")

    def hittingDatesFile(teamAbbrev, year):
        if path.exists("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("1. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("2. We have an error", e)
                    print("Database Error ")

    def hittingAddDates(datesFile, teamAbbrev, gameDate, year):
        with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "w") as f:
            try:
                datesFile['dates'].append(gameDate)
                f.write(str(datesFile))
            except Exception as e:
                print("3. We have an error", e)
                print("Database Error ")

    homeHitDates = hittingDatesFile(homeAbbrev, year)
    awayHitDates = hittingDatesFile(awayAbbrev, year)

    if (gameDate not in homeHitDates['dates'] or gameDate not in awayHitDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Completed' in game['status']):
        if game["game_type"] == "R":
            for ID in boxscore['playerInfo']:
                if ID in boxscore['home']['players']:
                    if boxscore['home']['players'][ID]['stats']['batting'] != {}:
                        h_add(gameDate, boxscore, ID, homeAbbrev, year)
                if ID in boxscore['away']['players']:
                    if boxscore['away']['players'][ID]['stats']['batting'] != {}:
                        a_add(gameDate, boxscore, ID, awayAbbrev, year)
            hittingAddDates(homeHitDates, homeAbbrev, gameDate, year)
            hittingAddDates(awayHitDates, awayAbbrev, gameDate, year)
    else:
        print("")
        print(homeAbbrev + " hitters have " + gameDate + ": " + str((gameDate in homeHitDates['dates'])))
        print(awayAbbrev + " hitters have " + gameDate + ": " + str((gameDate in awayHitDates['dates'])))
        print(game['status'])
        print("")

def pitch(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore):

    def h_add(gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['home']['players'][ID]
        playername = boxscore['playerInfo'][ID]['fullName']
        # progressive
        try:
            p_era = float(index['seasonStats']['pitching']['era'])
        except ValueError:
            print("Something is wrong with", playername + "'s era category")
            p_era = 0.0
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
        p_names = ['era', 'innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'doubles',
                   'triples',
                   'ab', 'obp', 'wins', 'losses', 'holds', 'blown_saves']
        pg_names = ['innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'pitches', 'strikes']

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                f.write(
                    '{"' + playername + '": {"ID":"' + ID + '", "' + year + '": { "pitching" : {"dates": [], "progression": {"era": [], "innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "doubles": [], "triples": [], "ab": [], "obp": [], "wins": [], "losses": [], "holds": [], "blown_saves": []}, "per_game": {"innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "pitches": [], "strikes": []}}, "hitting": {"dates": [], "progression": {"averages": [], "obp": [], "slg": [], "ops": [], "runs": [], "doubles": [], "triples": [], "homeruns": [], "strikeouts": [], "walks": [], "hits": [], "ab": [], "sb": [], "rbi": [], "lob": []}, "per_game": {"ab": [], "strikeouts": [], "hits": [], "walks": [], "runs": [], "rbi": [], "sb": [], "lob": [], "doubles": [], "triples": [], "homeruns": []}}}}}')
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)

        if gameDate not in content_dict[playername][year]['pitching']['dates']:
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                try:
                    content_dict[playername][year]['pitching']['dates'].append(gameDate)
                    for i in range(len(p_categories)):
                        content_dict[playername][year]['pitching']['progression'][p_names[i]].append(p_categories[i])
                    for i in range(len(pg_categories)):
                        content_dict[playername][year]['pitching']['per_game'][pg_names[i]].append(pg_categories[i])
                    f.write(str(content_dict))
                    print("Stats added for " + playername + " for " + gameDate)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "w") as f:
                try:
                    content_dict['players'].append(playername)
                    content_dict['players'].sort()
                    f.write(str(content_dict))
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")

    def a_add(gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['away']['players'][ID]
        playername = boxscore['playerInfo'][ID]['fullName']
        # progressive
        try:
            p_era = float(index['seasonStats']['pitching']['era'])
        except ValueError:
            print("Something is wrong with", playername + "'s era category")
            p_era = 0.0
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
        p_names = ['era', 'innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'doubles',
                   'triples',
                   'ab', 'obp', 'wins', 'losses', 'holds', 'blown_saves']
        pg_names = ['innings', 'hits', 'runs', 'earned_runs', 'walks', 'strikeouts', 'homeruns', 'pitches', 'strikes']

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                f.write(
                    '{"' + playername + '": {"ID":"' + ID + '", "' + year + '": { "pitching" : {"dates": [], "progression": {"era": [], "innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "doubles": [], "triples": [], "ab": [], "obp": [], "wins": [], "losses": [], "holds": [], "blown_saves": []}, "per_game": {"innings": [], "hits": [], "runs": [], "earned_runs": [], "walks": [], "strikeouts": [], "homeruns": [], "pitches": [], "strikes": []}}, "hitting": {"dates": [], "progression": {"averages": [], "obp": [], "slg": [], "ops": [], "runs": [], "doubles": [], "triples": [], "homeruns": [], "strikeouts": [], "walks": [], "hits": [], "ab": [], "sb": [], "rbi": [], "lob": []}, "per_game": {"ab": [], "strikeouts": [], "hits": [], "walks": [], "runs": [], "rbi": [], "sb": [], "lob": [], "doubles": [], "triples": [], "homeruns": []}}}}}')
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)

        if gameDate not in content_dict[playername][year]['pitching']['dates']:
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                try:
                    content_dict[playername][year]['pitching']['dates'].append(gameDate)
                    for i in range(len(p_categories)):
                        content_dict[playername][year]['pitching']['progression'][p_names[i]].append(p_categories[i])
                    for i in range(len(pg_categories)):
                        content_dict[playername][year]['pitching']['per_game'][pg_names[i]].append(pg_categories[i])
                    f.write(str(content_dict))
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open("Teams/" + teamAbbrev + "/" + year + "/pitchers.txt", "w") as f:
                try:
                    content_dict['players'].append(playername)
                    content_dict['players'].sort()
                    f.write(str(content_dict))
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")

    def pitchingDatesFile(teamAbbrev, year):
        if path.exists("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("1. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("2. We have an error", e)
                    print("Database Error ")

    def pitchingAddDates(datesFile, teamAbbrev, gameDate, year):
        with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "w") as f:
            try:
                datesFile['dates'].append(gameDate)
                f.write(str(datesFile))
            except Exception as e:
                print("3. We have an error", e)
                print("Database Error ")

    homePitchDates = pitchingDatesFile(homeAbbrev, year)
    awayPitchDates = pitchingDatesFile(awayAbbrev, year)

    if (gameDate not in homePitchDates['dates'] or gameDate not in awayPitchDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Completed' in game['status']):
        if game["game_type"] == "R":
            for ID in boxscore['playerInfo']:
                if ID in boxscore['home']['players']:
                    if boxscore['home']['players'][ID]['stats']['pitching'] != {}:
                        if boxscore['home']['players'][ID]['position']['abbreviation'] == 'P':
                            h_add(gameDate, boxscore, ID, homeAbbrev, year)
                if ID in boxscore['away']['players']:
                    if boxscore['away']['players'][ID]['stats']['pitching'] != {}:
                        if boxscore['away']['players'][ID]['position']['abbreviation'] == 'P':
                            a_add(gameDate, boxscore, ID, awayAbbrev, year)
            pitchingAddDates(homePitchDates, homeAbbrev, gameDate, year)
            pitchingAddDates(awayPitchDates, awayAbbrev, gameDate, year)
    else:
        print("")
        print(homeAbbrev + " pitchers have " + gameDate + ": " + str((gameDate in homePitchDates['dates'])))
        print(awayAbbrev + " pitchers have " + gameDate + ": " + str((gameDate in awayPitchDates['dates'])))
        print(game['status'])
        print("")

everythingBefore()
