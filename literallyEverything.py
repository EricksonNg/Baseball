from os import path, makedirs
import statsapi
import datetime

def everything():
    year = '2021'
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=2)
    tomorrow = today + datetime.timedelta(days=1)
    sched = statsapi.schedule(start_date= yesterday, end_date = tomorrow)
    for game in sched:
        gameId = game["game_id"]
        gameDate = game["game_date"]
        gameData = statsapi.get('game', {'gamePk': gameId})
        boxscore = gameData['liveData']['boxscore']
        if game['doubleheader'] != 'N':
            gameDate = game["game_date"] + "(" + str(game["game_num"]) + ")" # adds number to the back of the game date if the game is a part of a doubleheader

        homeId = game["home_id"]
        awayId = game["away_id"]
        homeAbbrev = statsapi.get('team', {'teamId': homeId})['teams'][0]['abbreviation']
        awayAbbrev = statsapi.get('team', {'teamId': awayId})['teams'][0]['abbreviation']

        homeGameDate = gameDate + " vs. " + awayAbbrev
        awayGameDate = gameDate + " @ " + homeAbbrev

        if game['game_type'] == "R":
            createDir("Teams", homeAbbrev, year) #if needed
            createDir("Teams", awayAbbrev, year) #if needed

            hit(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
            pitch(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
            field(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
        else:
            input("Game type: "+ game['game_type'])

def springTraining2021():
    year = '2021'
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=2)
    tomorrow = today + datetime.timedelta(days=1)
    sched = statsapi.schedule(start_date=yesterday, end_date=today)
    for game in sched:
        gameId = game["game_id"]
        gameDate = game["game_date"]
        gameData = statsapi.get('game', {'gamePk': gameId})
        boxscore = gameData['liveData']['boxscore']
        if game['doubleheader'] != 'N':
            gameDate = game["game_date"] + "(" + str(game["game_num"]) + ")"  # adds number to the back of the game date if the game is a part of a doubleheader

        homeId = game["home_id"]
        awayId = game["away_id"]
        homeAbbrev = statsapi.get('team', {'teamId': homeId})['teams'][0]['abbreviation']
        awayAbbrev = statsapi.get('team', {'teamId': awayId})['teams'][0]['abbreviation']

        homeGameDate = gameDate + " vs. " + awayAbbrev
        awayGameDate = gameDate + " @ " + homeAbbrev

        if game['game_type'] == "S":
            createDir("ST", homeAbbrev, year)  # if needed
            createDir("ST", awayAbbrev, year)  # if needed

            hit(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "ST")
            pitch(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "ST")
            field(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "ST")
        else:
            input("Game type: " + game['game_type'])

def everything2019():
    year = '2019'
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=2)
    tomorrow = today + datetime.timedelta(days=1)
    sched = statsapi.schedule(start_date= '03/28/2019', end_date = '09/29/2019')
    for game in sched:
        gameId = game["game_id"]
        gameDate = game["game_date"]
        dateYear, dateMonth, dateDay = gameDate.split("-")
        gameDate = dateMonth+"-"+dateDay+"-"+dateYear
        gameData = statsapi.get('game', {'gamePk': gameId})
        boxscore = gameData['liveData']['boxscore']
        if game['doubleheader'] != 'N':
            gameDate = game["game_date"] + "(" + str(game["game_num"]) + ")" # adds number to the back of the game date if the game is a part of a doubleheader

        homeId = game["home_id"]
        awayId = game["away_id"]
        homeAbbrev = statsapi.get('team', {'teamId': homeId})['teams'][0]['abbreviation']
        awayAbbrev = statsapi.get('team', {'teamId': awayId})['teams'][0]['abbreviation']

        homeGameDate = gameDate + " vs. " + awayAbbrev
        awayGameDate = gameDate + " @ " + homeAbbrev

        if game['game_type'] == "R":
            createDir("Teams",homeAbbrev, year) #if needed
            createDir("Teams",awayAbbrev, year) #if needed

            hit(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
            pitch(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
            field(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
        else:
            input("Game type: "+ game['game_type'])

def everything2020():
    year = '2020'
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=2)
    tomorrow = today + datetime.timedelta(days=1)
    sched = statsapi.schedule(start_date= '07/23/2020', end_date = '09/27/2020')
    for game in sched:
        skip = False
        gameId = game["game_id"]
        gameDate = game["game_date"]
        if gameId == 630882:
            if gameDate == '2020-08-14':
                skip = True
        gameData = statsapi.get('game', {'gamePk': gameId})
        boxscore = gameData['liveData']['boxscore']
        if game['doubleheader'] != 'N':
            gameDate = game["game_date"] + "(" + str(game["game_num"]) + ")" # adds number to the back of the game date if the game is a part of a doubleheader

        homeId = game["home_id"]
        awayId = game["away_id"]
        homeAbbrev = statsapi.get('team', {'teamId': homeId})['teams'][0]['abbreviation']
        awayAbbrev = statsapi.get('team', {'teamId': awayId})['teams'][0]['abbreviation']

        homeGameDate = gameDate + " vs. " + awayAbbrev
        awayGameDate = gameDate + " @ " + homeAbbrev

        if game['game_type'] == "R" and skip == False:
            createDir("Teams",homeAbbrev, year) #if needed
            createDir("Teams",awayAbbrev, year) #if needed

            hit(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
            # pitch(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
            # field(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, "Teams")
        else:
            print(game)
            print("Is this the suspended game?")
            input("Game type: " + game['game_type'])

def createDir(directory, teamAbbrev, year):
    if path.exists(directory+"/" + teamAbbrev + "/" + year):
        # print(year + " " + teamAbbrev + " directory exists")
        pass
    else:
        makedirs(directory+"/" + teamAbbrev + "/" + year)
        # print(year + " " + teamAbbrev + " directory created")

def hit(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, directory):

    def findLastFlyOut(teamAbbrev, playername, year):
        category = 0
        try:
            if path.exists(directory + "/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
                    category = content_dict[playername]['hitting']['progression']['fly outs'][-1]
        except Exception as e:
            category = 0
        return category

    def hittersList(teamAbbrev, year, playername):
        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/hitters.txt"):
            with open(directory + "/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("3. We have an error", e)
                    print("Database Error ")
        else:
            with open(directory + "/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open(directory + "/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("4. We have an error", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open(directory + "/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as f:
                try:
                    content_dict['players'].append(playername)
                    content_dict['players'].sort()
                    f.write(str(content_dict))
                except Exception as e:
                    print("5. We have an error", e)
                    print("Database Error ")

    def add(homeOrAway, gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['teams'][homeOrAway]['players'][ID]
        playername = index['person']['fullName']
        perGameStats = index['stats']['batting']
        seasonStats = index['seasonStats']['batting']
        print(playername)
        # progressive
        p_flyOuts = findLastFlyOut(teamAbbrev, playername, year) + int(perGameStats['flyOuts'])
        p_groundOuts = int(seasonStats['groundOuts'])
        p_runs = int(seasonStats['runs'])
        p_doubles = int(seasonStats['doubles'])
        p_triples = int(seasonStats['triples'])
        p_homeRuns = int(seasonStats['homeRuns'])
        p_strikeOuts = int(seasonStats['strikeOuts'])
        p_baseOnBalls = int(seasonStats['baseOnBalls'])
        p_intentionalWalks = int(seasonStats['intentionalWalks'])
        p_hits = int(seasonStats['hits'])
        p_hitByPitch = int(seasonStats['hitByPitch'])
        p_avg = float(seasonStats['avg'])
        p_atBats = int(seasonStats['atBats'])
        p_obp = float(seasonStats['obp'])
        p_slg = float(seasonStats['slg'])
        p_ops = float(seasonStats['ops'])
        p_caughtStealing = int(seasonStats['caughtStealing'])
        p_stolenBases = int(seasonStats['stolenBases'])
        try:
            p_stolenBasePercentage = float(seasonStats['stolenBasePercentage'])
        except ValueError:
            p_stolenBasePercentage = 0.000
        p_groundIntoDoublePlay = int(seasonStats['groundIntoDoublePlay'])
        p_groundIntoTriplePlay = int(seasonStats['groundIntoTriplePlay'])
        p_plateAppearances = int(seasonStats['plateAppearances'])
        p_totalBases = int(seasonStats['totalBases'])
        p_rbi = int(seasonStats['rbi'])
        p_leftOnBase = int(seasonStats['leftOnBase'])
        p_sacBunts = int(seasonStats['sacBunts'])
        p_sacFlies = int(seasonStats['sacFlies'])
        try:
            p_babip = float(seasonStats['babip'])
        except ValueError:
            p_babip = .000
        p_catchersInterference = int(seasonStats['catchersInterference'])
        p_pickoffs = int(seasonStats['pickoffs'])
        try:
            p_atBatsPerHomeRun = float(seasonStats['atBatsPerHomeRun'])
        except ValueError:
            p_atBatsPerHomeRun = 0.00
        p_iso = round(p_slg - p_avg, 3)
        p_extraBaseHits = p_doubles+p_triples+p_homeRuns
        try:
            p_strikeOutPercentage = round(p_strikeOuts/p_plateAppearances, 3)
        except ZeroDivisionError:
            p_strikeOutPercentage = 0.00
        try:
            p_walkPercentage = round((p_baseOnBalls+p_intentionalWalks)/p_plateAppearances, 3)
        except ZeroDivisionError:
            p_walkPercentage = (p_baseOnBalls+p_intentionalWalks) * 1.000
        # per game
        pg_flyOuts = int(perGameStats['flyOuts'])
        pg_groundOuts = int(perGameStats['groundOuts'])
        pg_runs = int(perGameStats['runs'])
        pg_doubles = int(perGameStats['doubles'])
        pg_triples = int(perGameStats['triples'])
        pg_homeRuns = int(perGameStats['homeRuns'])
        pg_strikeOuts = int(perGameStats['strikeOuts'])
        pg_baseOnBalls = int(perGameStats['baseOnBalls'])
        pg_intentionalWalks = int(perGameStats['intentionalWalks'])
        pg_hits = int(perGameStats['hits'])
        pg_hitByPitch = int(perGameStats['hitByPitch'])
        pg_atBats = int(perGameStats['atBats'])
        pg_caughtStealing = int(perGameStats['caughtStealing'])
        pg_stolenBases = int(perGameStats['stolenBases'])
        try:
            pg_stolenBasePercentage = float(perGameStats['stolenBasePercentage'])
        except ValueError:
            pg_stolenBasePercentage = 0.000
        pg_groundIntoDoublePlay = int(perGameStats['groundIntoDoublePlay'])
        pg_groundIntoTriplePlay = int(perGameStats['groundIntoTriplePlay'])
        pg_plateAppearances = int(perGameStats['plateAppearances'])
        pg_totalBases = int(perGameStats['totalBases'])
        pg_rbi = int(perGameStats['rbi'])
        pg_leftOnBase = int(perGameStats['leftOnBase'])
        pg_sacBunts = int(perGameStats['sacBunts'])
        pg_sacFlies = int(perGameStats['sacFlies'])
        pg_catchersInterference = int(perGameStats['catchersInterference'])
        pg_pickoffs = int(perGameStats['pickoffs'])
        try:
            pg_atBatsPerHomeRun = float(perGameStats['atBatsPerHomeRun'])
        except ValueError:
            pg_atBatsPerHomeRun = 0.00
        pg_extraBaseHits = pg_doubles+pg_triples+pg_homeRuns

        p_categories = [p_flyOuts, p_groundOuts, p_runs, p_doubles, p_triples, p_homeRuns, p_extraBaseHits, p_strikeOuts, p_strikeOutPercentage, p_baseOnBalls, p_walkPercentage, p_intentionalWalks, p_hits, p_hitByPitch, p_avg, p_atBats, p_obp, p_slg, p_ops, p_iso, p_caughtStealing, p_stolenBases, p_stolenBasePercentage, p_groundIntoDoublePlay, p_groundIntoTriplePlay, p_plateAppearances, p_totalBases, p_rbi, p_leftOnBase, p_sacBunts, p_sacFlies, p_babip, p_catchersInterference, p_pickoffs, p_atBatsPerHomeRun]
        pg_categories = [pg_flyOuts, pg_groundOuts, pg_runs, pg_doubles, pg_triples, pg_homeRuns, pg_extraBaseHits,pg_strikeOuts, pg_baseOnBalls, pg_intentionalWalks, pg_hits, pg_hitByPitch, pg_atBats, pg_caughtStealing, pg_stolenBases, pg_stolenBasePercentage, pg_groundIntoDoublePlay, pg_groundIntoTriplePlay, pg_plateAppearances, pg_totalBases, pg_rbi, pg_leftOnBase, pg_sacBunts, pg_sacFlies, pg_catchersInterference, pg_pickoffs, pg_atBatsPerHomeRun]
        p_names = ['fly outs', 'ground outs', 'runs', 'doubles', 'triples', 'home runs', 'extra-base hits','strike outs', 'strike out percentage', 'walks', 'walk percentage', 'intentional walks', 'hits', 'hbp', 'avg', 'ab', 'obp', 'slg', 'ops', 'iso', 'cs', 'sb', 'sbp', 'gidp', 'gitp', 'pa', 'total bases', 'rbi', 'lob', 'sac bunts', 'sac flies', 'babip', 'ci', 'pickoffs', 'ab per hr']
        pg_names = ['fly outs', 'ground outs', 'runs', 'doubles', 'triples', 'home runs', 'extra-base hits', 'strike outs', 'walks', 'intentional walks', 'hits', 'hbp', 'ab', 'cs', 'sb', 'sbp', 'gidp', 'gitp', 'pa', 'total bases', 'rbi', 'lob', 'sac bunts', 'sac flies', 'ci', 'pickoffs', 'ab per hr']

        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            print("============================================")
            print("File Exists For", playername)
            with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("1. We have an error", e)
                    print("Database Error ")
                else:
                    print("Read success for", playername)
        else:
            if index['position']['abbreviation'] == 'P':
                print("============================================")
                print("Creating File For Pitcher", playername)
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "pitching" : {"dates": [], "progression": {}, "per_game": {}}, "hitting": {"dates": [], "progression": {}, "per_game": {}}, "fielding" : {"dates": [], "positions": [], "progression": {}, "per_game": {}}}}')
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
            else:
                print("============================================")
                print("Creating File For Hitter", playername)
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write('{"' + playername + '": {"ID":"' + ID + '", "hitting" : {"dates": [], "progression": {}, "per_game": {}}, "fielding": {"dates": [], "positions": [], "progression": {}, "per_game": {}}, "pitching": {"dates": [], "progression": {}, "per_game": {}}}}')
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)

        if gameDate not in content_dict[playername]['hitting']['dates']:
            print("-----Stats not added yet for", gameDate + "-----")
            with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                try:
                    content_dict[playername]['hitting']['dates'].append(gameDate)
                    for i in range(len(p_categories)):
                        try:
                            content_dict[playername]['hitting']['progression'][p_names[i]].append(
                                p_categories[i])
                            print(p_names[i], "(p) added to " + playername)
                        except Exception as e:
                            content_dict[playername]['hitting']['progression'][p_names[i]] = []
                            content_dict[playername]['hitting']['progression'][p_names[i]].append(
                                p_categories[i])
                            print(p_names[i], "(p) added to " + playername)
                    for i in range(len(pg_categories)):
                        try:
                            content_dict[playername]['hitting']['per_game'][pg_names[i]].append(
                                pg_categories[i])
                            print(pg_names[i], "(pg) added to " + playername)
                        except Exception as e:
                            content_dict[playername]['hitting']['per_game'][pg_names[i]] = []
                            content_dict[playername]['hitting']['per_game'][pg_names[i]].append(
                                pg_categories[i])
                            print(pg_names[i], "(pg) added to " + playername)
                    f.write(str(content_dict))
                    print("============================================")
                except Exception as e:
                    print("2. We have an error", e)
                    print("Database Error ")
        else:
            print("-----Stats already added for", gameDate + "-----")
            print("============================================")

        hittersList(teamAbbrev, year, playername)

    def hittingDatesFile(teamAbbrev, year):
        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/h_dates.txt"):
            with open(directory + "/" + teamAbbrev + "/" + year + "/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("6. We have an error", e)
                    print("Database Error ")
        else:
            with open(directory + "/" + teamAbbrev + "/" + year + "/h_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open(directory + "/" + teamAbbrev + "/" + year + "/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("7. We have an error", e)
                    print("Database Error ")

    def hittingAddDates(datesFile, teamAbbrev, gameDate, year):
        if gameDate not in datesFile['dates']:
            with open(directory + "/" + teamAbbrev + "/" + year + "/h_dates.txt", "w") as f:
                try:
                    datesFile['dates'].append(gameDate)
                    f.write(str(datesFile))
                except Exception as e:
                    print("8. We have an error", e)
                    print("Database Error ")

    homeHitDates = hittingDatesFile(homeAbbrev, year)
    awayHitDates = hittingDatesFile(awayAbbrev, year)

    if (homeGameDate not in homeHitDates['dates'] or awayGameDate not in awayHitDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Tied' in game['status'] or 'Completed' in game['status']):
        if game["game_type"] == "S":
            awayPlayers = boxscore['teams']['away']['players']
            homePlayers = boxscore['teams']['home']['players']
            for ID in homePlayers:
                if homePlayers[ID]['stats']['batting'] != {}:
                    add('home', homeGameDate, boxscore, ID, homeAbbrev, year)
            for ID in awayPlayers:
                if awayPlayers[ID]['stats']['batting'] != {}:
                    add('away', awayGameDate, boxscore, ID, awayAbbrev, year)
            hittingAddDates(homeHitDates, homeAbbrev, homeGameDate, year)
            hittingAddDates(awayHitDates, awayAbbrev, awayGameDate, year)
    else:
        print("==============================")
        if homeGameDate in homeHitDates['dates']:
            print(homeAbbrev + " hitting stats already added for " + homeGameDate)
        if awayGameDate in awayHitDates['dates']:
            print(awayAbbrev + " hitting stats already added for " + awayGameDate)
        if game['status'] == 'Suspended':
            input("Suspended Game")
    #     else:
    #         print(homeAbbrev + " hitters have " + homeGameDate + ": " + str((homeGameDate in homeHitDates['dates'])))
    #         print(awayAbbrev + " hitters have " + awayGameDate + ": " + str((awayGameDate in awayHitDates['dates'])))
    #         print(game['status'])
    #         print("")

def pitch(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, directory):

    def findLast(teamAbbrev, playername, year, category):
        categories = {'p_stolenBasePercentage': 'sbp', 'p_balls': 'balls', 'p_strikes': 'strikes', 'p_battersFaced': 'batters faced', 'p_numberOfPitches': 'pitches', 'p_rbi': 'rbi'}
        last = 0
        try:
            if path.exists(directory + "/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
                    last = content_dict[playername]['pitching']['progression'][categories[category]][-1]
        except Exception as e:
            print("findLast was used for: " + category + " " +str(e))
            last = 0
        return last

    def pitchersList(teamAbbrev, year, playername):
        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/pitchers.txt"):
            with open(directory + "/" + teamAbbrev + "/" + year + "/pitchers.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("We got an error ", e)
                    print("Database Error ")
        else:
            with open(directory + "/" + teamAbbrev + "/" + year + "/pitchers.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open(directory + "/" + teamAbbrev + "/" + year + "/pitchers.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("We got an error ", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open(directory + "/" + teamAbbrev + "/" + year + "/pitchers.txt", "w") as f:
                try:
                    content_dict['players'].append(playername)
                    content_dict['players'].sort()
                    f.write(str(content_dict))
                except Exception as e:
                    print("9. We have an error", e)
                    print("Database Error ")

    def add(homeOrAway, gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['teams'][homeOrAway]['players'][ID]
        playername = index['person']['fullName']
        perGameStats = index['stats']['pitching']
        seasonStats = index['seasonStats']['pitching']
        print(playername)
        if perGameStats['numberOfPitches'] != 0:
            # per game
            pg_gamesStarted = int(perGameStats['gamesStarted'])
            pg_groundOuts = int(perGameStats['groundOuts'])
            pg_airOuts = int(perGameStats['airOuts'])
            pg_runs = int(perGameStats['runs'])
            pg_doubles = int(perGameStats['doubles'])
            pg_triples = int(perGameStats['triples'])
            pg_homeRuns = int(perGameStats['homeRuns'])
            pg_strikeOuts = int(perGameStats['strikeOuts'])
            pg_baseOnBalls = int(perGameStats['baseOnBalls'])
            pg_intentionalWalks = int(perGameStats['intentionalWalks'])
            pg_hits = int(perGameStats['hits'])
            pg_hitByPitch = int(perGameStats['hitByPitch'])
            pg_atBats = int(perGameStats['atBats'])
            pg_caughtStealing = int(perGameStats['caughtStealing'])
            pg_stolenBases = int(perGameStats['stolenBases'])
            try:
                pg_stolenBasePercentage = float(perGameStats['stolenBasePercentage'])
            except ValueError: # if value is a string instead of a number value
                pg_stolenBasePercentage = 0.000
            pg_numberOfPitches = int(perGameStats['numberOfPitches'])
            if pg_numberOfPitches == 0:
                input(playername + " has no pitches!")
            pg_inningsPitched = float(perGameStats['inningsPitched'])
            if ".1" in str(pg_inningsPitched):
                pg_inningsPitched = int(pg_inningsPitched) + 0.33
            if ".2" in str(pg_inningsPitched):
                pg_inningsPitched = int(pg_inningsPitched) + 0.67
            try:
                pg_whip = round(((pg_hits + pg_hitByPitch + pg_baseOnBalls + pg_intentionalWalks)/pg_inningsPitched),2)
            except ZeroDivisionError:
                pg_whip = float(pg_hits + pg_hitByPitch + pg_baseOnBalls + pg_intentionalWalks)
            pg_wins = int(perGameStats['wins'])
            pg_losses = int(perGameStats['losses'])
            pg_saves = int(perGameStats['saves'])
            pg_saveOpportunities = int(perGameStats['saveOpportunities'])
            pg_holds = int(perGameStats['holds'])
            pg_blownSaves = int(perGameStats['blownSaves'])
            pg_earnedRuns = int(perGameStats['earnedRuns'])
            pg_battersFaced = int(perGameStats['battersFaced'])
            pg_outs = int(perGameStats['outs'])
            pg_completeGames = int(perGameStats['completeGames'])
            pg_shutouts = int(perGameStats['shutouts'])
            pg_balls = int(perGameStats['balls'])
            pg_strikes = int(perGameStats['strikes'])
            try:
                pg_strikePercentage = float(perGameStats['strikePercentage'])
            except ValueError:
                pg_strikePercentage = 0.000
            pg_balks = int(perGameStats['balks'])
            pg_wildPitches = int(perGameStats['wildPitches'])
            pg_pickoffs = int(perGameStats['pickoffs'])
            pg_rbi = int(perGameStats['rbi'])
            pg_gamesFinished = int(perGameStats['gamesFinished'])
            try:
                pg_runsScoredPer9 = float(perGameStats['runsScoredPer9'])
            except ValueError:
                pg_runsScoredPer9 = float(perGameStats['runs'])*27
            try:
                pg_homeRunsPer9 = float(perGameStats['homeRunsPer9'])
            except ValueError:
                pg_homeRunsPer9 = float(perGameStats['homeRuns'])*27
            try:
                pg_strikeOutsPer9 = round(((9/pg_inningsPitched)*pg_strikeOuts),2)
            except ZeroDivisionError:
                pg_strikeOutsPer9 = float(pg_strikeOuts)*27
            try:
                pg_walksPer9 = round(((9/pg_inningsPitched)*pg_baseOnBalls), 2)
            except ZeroDivisionError:
                pg_walksPer9 = float(pg_baseOnBalls*27)
            try:
                pg_hitsPer9 = round(((9/pg_inningsPitched)*pg_hits),2)
            except ZeroDivisionError:
                pg_hitsPer9 = float(pg_hits)*27

            pg_inheritedRunners = int(perGameStats['inheritedRunners'])
            if pg_inheritedRunners > 0:
                input("Inherited Runners is actually greater than 0!")
                input()

            pg_inheritedRunnersScored = int(perGameStats['inheritedRunnersScored'])
            pg_catchersInterference = int(perGameStats['catchersInterference'])
            pg_sacBunts = int(perGameStats['sacBunts'])
            pg_sacFlies = int(perGameStats['sacFlies'])
            try:
                pg_pitchesPerInning = float(seasonStats['pitchesPerInning'])
            except ValueError:
                pg_pitchesPerInning = float(pg_numberOfPitches)  # Pitches per inning in seasonStats gives the pitches per innings for the pitcher for that one game (it's a per game average, not a season average)
            try:
                pg_battingAverageAgainst = round(pg_hits/pg_atBats, 3)
            except ZeroDivisionError:
                pg_battingAverageAgainst = 0.000

            # progressive
            p_gamesPlayed = int(seasonStats['gamesPlayed'])
            p_gamesStarted = int(seasonStats['gamesStarted'])
            p_groundOuts = int(seasonStats['groundOuts'])
            p_airOuts = int(seasonStats['airOuts'])
            p_runs = int(seasonStats['runs'])
            p_doubles = int(seasonStats['doubles'])
            p_triples = int(seasonStats['triples'])
            p_homeRuns = int(seasonStats['homeRuns'])
            p_strikeOuts = int(seasonStats['strikeOuts'])
            p_baseOnBalls = int(seasonStats['baseOnBalls'])
            p_intentionalWalks = int(seasonStats['intentionalWalks'])
            p_hits = int(seasonStats['hits'])
            p_hitByPitch = int(seasonStats['hitByPitch'])
            p_atBats = int(seasonStats['atBats'])
            p_obp = float(seasonStats['obp'])
            p_caughtStealing = int(seasonStats['caughtStealing'])
            p_stolenBases = int(seasonStats['stolenBases'])
            try:
                p_stolenBasePercentage = float(seasonStats['stolenBasePercentage'])
            except ValueError:
                p_stolenBasePercentage = float(findLast(teamAbbrev, playername, year, 'p_stolenBasePercentage'))
            p_earnedRuns = int(seasonStats['earnedRuns']) # p_earnRuns has to be put above p_era to use in the calculation of p_era if there is a ValueError
            try:
                p_era = float(seasonStats['era'])
            except ValueError:
                p_era = pg_earnedRuns*27
            p_inningsPitched = float(seasonStats['inningsPitched'])
            if ".1" in str(p_inningsPitched):
                p_inningsPitched = int(p_inningsPitched) + 0.33
            if ".2" in str(p_inningsPitched):
                p_inningsPitched = int(p_inningsPitched) + 0.67
            p_wins = int(seasonStats['wins'])
            p_losses = int(seasonStats['losses'])
            p_saves = int(seasonStats['saves'])
            p_saveOpportunities = int(seasonStats['saveOpportunities'])
            p_holds = int(seasonStats['holds'])
            p_blownSaves = int(seasonStats['blownSaves'])
            try:
                p_whip = float(seasonStats['whip'])
            except ValueError:
                p_whip = float(p_hits + p_hitByPitch + p_baseOnBalls + p_intentionalWalks)
            p_battersFaced = findLast(teamAbbrev, playername, year, 'p_battersFaced') + pg_battersFaced
            p_outs = int(seasonStats['outs'])
            p_completeGames = int(seasonStats['completeGames'])
            p_shutouts = int(seasonStats['shutouts'])

            try:
                p_balls = findLast(teamAbbrev, playername, year, "p_balls") + pg_balls
            except Exception:
                input("Something is wrong with p_balls")
            try:
                p_strikes = findLast(teamAbbrev, playername, year, "p_strikes") + pg_strikes
            except Exception:
                input("Something is wrong with p_strikes")
            try:
                p_numberOfPitches = findLast(teamAbbrev, playername, year, "p_numberOfPitches") + pg_numberOfPitches
            except Exception:
                input("Something is wrong with p_numberOfPitches")
            try:
                p_strikePercentage = round(p_strikes/p_numberOfPitches,3)
            except Exception:
                input("Something is wrong with p_strikePercentage")
            try:
                p_pitchesPerInning = round((p_numberOfPitches/p_inningsPitched), 2)
            except ZeroDivisionError:
                p_pitchesPerInning = float(pg_numberOfPitches)

            p_balks = int(seasonStats['balks'])
            p_wildPitches = int(seasonStats['wildPitches'])
            p_pickoffs = int(seasonStats['pickoffs'])
            try:
                p_groundOutsToAirouts = float(seasonStats['groundOutsToAirouts'])
            except ValueError:
                if p_groundOuts == 0 and p_airOuts == 0:
                    p_groundOutsToAirouts = 0.00
                elif p_airOuts == 0:
                    p_groundOutsToAirouts = float(p_groundOuts)
                elif p_groundOuts == 0:
                    p_groundOutsToAirouts = 1.0/p_airOuts
            try:
                p_rbi = findLast(teamAbbrev, playername, year, 'p_rbi') + pg_rbi
            except Exception:
                input("Something is wrong with p_rbi")
            try:
                p_winPercentage = float(seasonStats['winPercentage'])
            except ValueError:
                if p_wins == 0:
                    p_winPercentage = 0.00
                else:
                    input("We have a problem")
            p_gamesFinished = int(seasonStats['gamesFinished'])
            try:
                p_strikeoutWalkRatio = float(seasonStats['strikeoutWalkRatio'])
            except ValueError:
                if p_strikeOuts == 0 and p_baseOnBalls == 0:
                    p_strikeoutWalkRatio = 0.00
                elif p_baseOnBalls == 0:
                    p_strikeoutWalkRatio = float(p_strikeOuts)
                elif p_strikeOuts == 0:
                    p_strikeoutWalkRatio = 1.0/p_baseOnBalls
            try:
                p_strikeoutsPer9Inn = float(seasonStats['strikeoutsPer9Inn'])
            except ValueError:
                p_strikeoutsPer9Inn = float(pg_strikeOuts)*27 # Relates to pg_strikeOutsPer9
            try:
                p_walksPer9Inn = float(seasonStats['walksPer9Inn'])
            except ValueError:
                p_walksPer9Inn = float(pg_baseOnBalls)*27 # Relates to pg_walksPer9
            try:
                p_hitsPer9Inn = float(seasonStats['hitsPer9Inn'])
            except ValueError:
                p_hitsPer9Inn = float(pg_hits)*27 # Relates to pg_hitsPer9
            try:
                p_runsScoredPer9 = float(seasonStats['runsScoredPer9'])
            except ValueError:
                p_runsScoredPer9 = float(pg_runs)*27
            try:
                p_homeRunsPer9 = float(seasonStats['homeRunsPer9'])
            except ValueError:
                p_homeRunsPer9 = float(pg_homeRuns)*27
            p_inheritedRunnersScored = int(seasonStats['inheritedRunnersScored'])
            p_catchersInterference = int(seasonStats['catchersInterference'])
            p_sacBunts = int(seasonStats['sacBunts'])
            p_sacFlies = int(seasonStats['sacFlies'])
            try:
                p_battingAverageAgainst = round(p_hits/p_atBats, 3)
            except ZeroDivisionError:
                p_battingAverageAgainst = 0.000
            p_strikeOutPercentage = round(p_strikeOuts/p_battersFaced, 3)

            p_categories = [p_gamesPlayed, p_gamesStarted, p_groundOuts, p_airOuts, p_runs, p_doubles, p_triples, p_homeRuns, p_strikeOuts, p_strikeOutPercentage,p_baseOnBalls, p_intentionalWalks, p_hits, p_hitByPitch, p_atBats, p_obp, p_caughtStealing, p_stolenBases, p_stolenBasePercentage, p_era, p_inningsPitched, p_wins, p_losses, p_saves, p_saveOpportunities, p_holds, p_blownSaves, p_earnedRuns, p_whip, p_battersFaced, p_outs, p_completeGames, p_shutouts, p_balls, p_strikes, p_numberOfPitches, p_strikePercentage, p_pitchesPerInning,p_balks,p_wildPitches, p_pickoffs, p_groundOutsToAirouts, p_rbi,p_winPercentage, p_gamesFinished, p_strikeoutWalkRatio, p_strikeoutsPer9Inn, p_walksPer9Inn, p_hitsPer9Inn, p_runsScoredPer9, p_homeRunsPer9, p_battingAverageAgainst, p_inheritedRunnersScored, p_catchersInterference, p_sacBunts, p_sacFlies]

            p_names = ['g', 'gs', 'ground outs', 'air outs', 'runs', 'doubles', 'triples', 'home runs', 'strike outs', 'strike out percentage', 'walks', 'intentional walks', 'hits', 'hbp', 'ab', 'obp', 'cs', 'sb', 'sbp', 'era', 'innings', 'wins', 'losses', 'saves', 'save opportunities', 'holds', 'blown saves', 'earned runs', 'whip', 'batters faced', 'outs', 'complete games', 'shut outs', 'balls', 'strikes', 'pitches', 'strike percentage', 'pitches per inning','balks', 'wild pitches', 'pickoffs', 'ground to air', 'rbi', 'win percentage', 'games finished', 'strikeout to walk', 'strikeouts per 9', 'walks per 9', 'hits per 9', 'runs per 9', 'home runs per 9', 'baa', 'inherited runners scored', 'catchers interference', 'sac bunts', 'sac flies']

            pg_categories = [pg_gamesStarted, pg_groundOuts, pg_airOuts, pg_runs, pg_doubles, pg_triples, pg_homeRuns, pg_strikeOuts, pg_baseOnBalls, pg_intentionalWalks, pg_hits, pg_hitByPitch, pg_atBats, pg_caughtStealing, pg_stolenBases, pg_stolenBasePercentage, pg_numberOfPitches, pg_inningsPitched, pg_whip, pg_pitchesPerInning, pg_wins, pg_losses, pg_saves, pg_saveOpportunities, pg_holds, pg_blownSaves, pg_earnedRuns, pg_battersFaced, pg_outs, pg_completeGames, pg_shutouts, pg_balls, pg_strikes, pg_strikePercentage, pg_balks, pg_wildPitches, pg_pickoffs, pg_rbi, pg_gamesFinished, pg_runsScoredPer9, pg_homeRunsPer9, pg_strikeOutsPer9, pg_walksPer9, pg_hitsPer9, pg_battingAverageAgainst,pg_inheritedRunnersScored, pg_catchersInterference, pg_sacBunts, pg_sacFlies]
            pg_names = ['gs', 'ground outs', 'air outs', 'runs', 'doubles', 'triples', 'home runs', 'strike outs', 'walks', 'intentional walks', 'hits', 'hbp', 'ab', 'cs', 'sb', 'sbp', 'pitches', 'innings', 'whip','pitches per inning','wins', 'losses', 'saves', 'save opportunities', 'holds', 'blown saves', 'earned runs', 'batters faced', 'outs', 'complete games', 'shut outs', 'balls', 'strikes', 'strike percentage', 'balks', 'wild pitches', 'pickoffs', 'rbi', 'games finished', 'runs per 9', 'home runs per 9', 'strikeouts per 9', 'walks per 9', 'hits per 9', 'baa', 'inherited runners scored', 'catchers interference', 'sac bunts', 'sac flies']

            if path.exists(directory + "/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                print("============================================")
                print("File Exists For", playername)
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    try:
                        content_dict = eval(content)
                    except Exception as e:
                        print("We got an error ", e)
                        print("Database Error ")
                    else:
                        print("Read success for", playername)
            else:
                print("============================================")
                print("Creating File For Pitcher", playername)
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "pitching" : {"dates": [], "progression": {}, "per_game": {}}, "hitting": {"dates": [], "progression": {}, "per_game": {}}, "fielding" : {"dates": [], "positions": [], "progression": {}, "per_game": {}}}}')
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)

            if gameDate not in content_dict[playername]['pitching']['dates']:
                print("-----Stats not added yet for", gameDate + "-----")
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    try:
                        content_dict[playername]['pitching']['dates'].append(gameDate)
                        for i in range(len(p_categories)):
                            try:
                                content_dict[playername]['pitching']['progression'][p_names[i]].append(p_categories[i])
                                print(p_names[i], "(p) " + str(p_categories[i]) + " added to " + playername)
                            except Exception as e:
                                content_dict[playername]['pitching']['progression'][p_names[i]] = []
                                content_dict[playername]['pitching']['progression'][p_names[i]].append(p_categories[i])
                                print(p_names[i], "(p) " + str(p_categories[i]) + " added to " + playername)
                        for i in range(len(pg_categories)):
                            try:
                                content_dict[playername]['pitching']['per_game'][pg_names[i]].append(pg_categories[i])
                                print(pg_names[i], "(pg) " + str(pg_categories[i]) + " added to " + playername)
                            except Exception as e:
                                content_dict[playername]['pitching']['per_game'][pg_names[i]] = []
                                content_dict[playername]['pitching']['per_game'][pg_names[i]].append(pg_categories[i])
                                print(pg_names[i], "(pg) " + str(pg_categories[i]) + " added to " + playername)
                        f.write(str(content_dict))
                        print("============================================")
                    except Exception as e:
                        print("We got an error ", e)
                        print("Database Error ")
            else:
                print("-----Stats already added for", gameDate + "-----")
                print("============================================")
        else:
            print(playername + " has " + str(perGameStats['numberOfPitches']) + " pitches with " + str(perGameStats['caughtStealing']) + " caught stealing and " + str(perGameStats['pickoffs']) + " pickoffs")

        pitchersList(teamAbbrev, year, playername)

    def pitchingDatesFile(teamAbbrev, year):
        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/p_dates.txt"):
            with open(directory + "/" + teamAbbrev + "/" + year + "/p_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("10. We have an error", e)
                    print("Database Error ")
        else:
            with open(directory + "/" + teamAbbrev + "/" + year + "/p_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open(directory + "/" + teamAbbrev + "/" + year + "/p_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("11. We have an error", e)
                    print("Database Error ")

    def pitchingAddDates(datesFile, teamAbbrev, gameDate, year):
        if gameDate not in datesFile['dates']:
            with open(directory + "/" + teamAbbrev + "/" + year + "/p_dates.txt", "w") as f:
                try:
                    datesFile['dates'].append(gameDate)
                    f.write(str(datesFile))
                except Exception as e:
                    print("12. We have an error", e)
                    print("Database Error ")

    homePitchDates = pitchingDatesFile(homeAbbrev, year)
    awayPitchDates = pitchingDatesFile(awayAbbrev, year)

    if (homeGameDate not in homePitchDates['dates'] or awayGameDate not in awayPitchDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Tied' in game['status'] or 'Completed' in game['status']):
        if game["game_type"] == "S":
            awayPlayers = boxscore['teams']['away']['players']
            homePlayers = boxscore['teams']['home']['players']
            for ID in homePlayers:
                if homePlayers[ID]['stats']['pitching'] != {}:
                    add('home', homeGameDate, boxscore, ID, homeAbbrev, year)
            for ID in awayPlayers:
                if awayPlayers[ID]['stats']['pitching'] != {}:
                    add('away', awayGameDate, boxscore, ID, awayAbbrev, year)
            pitchingAddDates(homePitchDates, homeAbbrev, homeGameDate, year)
            pitchingAddDates(awayPitchDates, awayAbbrev, awayGameDate, year)
    else:
        if homeGameDate in homePitchDates['dates']:
            print(homeAbbrev + " pitching stats already added for " + homeGameDate)
        if awayGameDate in awayPitchDates['dates']:
            print(awayAbbrev + " pitching stats already added for " + awayGameDate)
        if game['status'] == 'Suspended':
            input("Suspended Game")
    #     else:
    #         print(homeAbbrev + " pitchers have " + homeGameDate + ": " + str((homeGameDate in homePitchDates['dates'])))
    #         print(awayAbbrev + " pitchers have " + awayGameDate + ": " + str((awayGameDate in awayPitchDates['dates'])))
    #         print(game['status'])
    #         print("")

def field(homeAbbrev, awayAbbrev, year, homeGameDate, awayGameDate, game, boxscore, directory):

    def fieldersList(teamAbbrev, year, playername):
        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/fielders.txt"):
            with open(directory + "/" + teamAbbrev + "/" + year + "/fielders.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("3. We have an error", e)
                    print("Database Error ")
        else:
            with open(directory + "/" + teamAbbrev + "/" + year + "/fielders.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open(directory + "/" + teamAbbrev + "/" + year + "/fielders.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("4. We have an error", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open(directory + "/" + teamAbbrev + "/" + year + "/fielders.txt", "w") as f:
                try:
                    content_dict['players'].append(playername)
                    content_dict['players'].sort()
                    f.write(str(content_dict))
                except Exception as e:
                    print("5. We have an error", e)
                    print("Database Error ")

    def findLastGameStart(teamAbbrev, playername, year):
        category = 0
        try:
            if path.exists(directory + "/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
                    category = content_dict[playername]['fielding']['progression']['gs'][-1]
        except Exception as e:
            print("findLast was used for: " + str(e))
            category = 0
        return category

    def add(homeOrAway, gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['teams'][homeOrAway]['players'][ID]
        playername = index['person']['fullName']
        perGameStats = index['stats']['fielding']
        seasonStats = index['seasonStats']['fielding']
        print(playername)
        # per game (placed above progressive so p_gamesStarted can get value of pg_gamesStarted)
        pg_assists = int(perGameStats['assists'])
        pg_putOuts = int(perGameStats['putOuts'])
        pg_errors = int(perGameStats['errors'])
        pg_chances = int(perGameStats['chances'])
        pg_caughtStealing = int(perGameStats['caughtStealing'])
        pg_passedBall = int(perGameStats['passedBall'])
        try:
            pg_gamesStarted = int(perGameStats['gamesStarted'])
        except KeyError:
            pg_gamesStarted = 0
        pg_stolenBases = int(perGameStats['stolenBases'])
        try:
            pg_stolenBasePercentage = float(perGameStats['stolenBasePercentage'])
        except ValueError:
            pg_stolenBasePercentage = 0.000
        pg_pickoffs = int(perGameStats['pickoffs'])
        # progressive
        p_assists = int(seasonStats['assists'])
        p_putOuts = int(seasonStats['putOuts'])
        p_errors = int(seasonStats['errors'])
        p_chances = int(seasonStats['chances'])
        p_fielding = float(seasonStats['fielding'])
        p_caughtStealing = int(seasonStats['caughtStealing'])
        p_passedBall = int(seasonStats['passedBall'])
        p_gamesStarted = findLastGameStart(teamAbbrev, playername, year) + pg_gamesStarted
        p_stolenBases = int(seasonStats['stolenBases'])
        try:
            p_stolenBasePercentage = float(seasonStats['stolenBasePercentage'])
        except ValueError:
            p_stolenBasePercentage = 0.000
        p_pickoffs = int(seasonStats['pickoffs'])

        p_categories = [p_assists, p_putOuts, p_errors, p_chances, p_fielding, p_caughtStealing, p_passedBall, p_gamesStarted, p_stolenBases, p_stolenBasePercentage, p_pickoffs]
        pg_categories = [pg_assists, pg_putOuts, pg_errors, pg_chances, pg_caughtStealing, pg_passedBall, pg_gamesStarted, pg_stolenBases, pg_stolenBasePercentage, pg_pickoffs]
        p_names = ['assists', 'put outs', 'errors', 'chances', 'fielding percentage', 'cs', 'passed balls', 'gs', 'sb', 'sbp', 'pickoffs']
        pg_names = ['assists', 'put outs', 'errors', 'chances', 'cs', 'passed balls', 'gs', 'sb', 'sbp', 'pickoffs']

        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            print("============================================")
            print("File Exists For", playername)
            with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("1. We got an error ", e)
                    print("Database Error ")
                else:
                    print("Read success for", playername)
        else:
            with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                f.write(
                    '{"' + playername + '": {"ID":"' + ID + '", "hitting" : {"dates": [], "progression": {}, "per_game": {}}, "fielding": {"dates": [], "positions": [], "progression": {}, "per_game": {}},"pitching": {"dates": [], "progression": {}, "per_game": {}}}}')
            with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)

        if gameDate not in content_dict[playername]['fielding']['dates']:
            print("-----Stats not added yet for", gameDate + "-----")
            with open(directory + "/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                try:
                    content_dict[playername]['fielding']['dates'].append(gameDate)
                    for i in range(len(p_categories)):
                        try:
                            content_dict[playername]['fielding']['progression'][p_names[i]].append(
                                p_categories[i])
                            print(p_names[i], "(p) added to " + playername)
                        except Exception as e:
                            content_dict[playername]['fielding']['progression'][p_names[i]] = []
                            content_dict[playername]['fielding']['progression'][p_names[i]].append(
                                p_categories[i])
                            print(p_names[i], "(p) added to " + playername)
                    for i in range(len(pg_categories)):
                        try:
                            content_dict[playername]['fielding']['per_game'][pg_names[i]].append(pg_categories[i])
                            print(pg_names[i], "(pg) added to " + playername)
                        except Exception as e:
                            content_dict[playername]['fielding']['per_game'][pg_names[i]] = []
                            content_dict[playername]['fielding']['per_game'][pg_names[i]].append(pg_categories[i])
                            print(pg_names[i], "(pg) added to " + playername)
                    position = index['allPositions'][0]['abbreviation']
                    if len(index['allPositions']) > 1:
                        for i in range(1, len(index['allPositions'])):
                            position += "-"+index['allPositions'][i]['abbreviation']
                    content_dict[playername]['fielding']['positions'].append(position)
                    f.write(str(content_dict))
                    print("============================================")
                except Exception as e:
                    print("2. We got an error ", e)
                    print("Database Error ")
        else:
            print("-----Stats already added for", gameDate + "-----")
            print("============================================")

        fieldersList(teamAbbrev, year, playername)

    def fieldingDatesFile(teamAbbrev, year):
        if path.exists(directory + "/" + teamAbbrev + "/" + year + "/f_dates.txt"):
            with open(directory + "/" + teamAbbrev + "/" + year + "/f_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("6. We have an error", e)
                    print("Database Error ")
        else:
            with open(directory + "/" + teamAbbrev + "/" + year + "/f_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open(directory + "/" + teamAbbrev + "/" + year + "/f_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("7. We have an error", e)
                    print("Database Error ")

    def fieldingAddDates(datesFile, teamAbbrev, gameDate, year):
        if gameDate not in datesFile['dates']:
            with open(directory + "/" + teamAbbrev + "/" + year + "/f_dates.txt", "w") as f:
                try:
                    datesFile['dates'].append(gameDate)
                    f.write(str(datesFile))
                except Exception as e:
                    print("8. We have an error", e)
                    print("Database Error ")

    homeFieldDates = fieldingDatesFile(homeAbbrev, year)
    awayFieldDates = fieldingDatesFile(awayAbbrev, year)

    if (homeGameDate not in homeFieldDates['dates'] or awayGameDate not in awayFieldDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Tied' in game['status'] or 'Completed' in game['status']):
        if game["game_type"] == "S":
            awayPlayers = boxscore['teams']['away']['players']
            homePlayers = boxscore['teams']['home']['players']
            for ID in homePlayers:
                if homePlayers[ID]['stats']['fielding'] != {}:
                    add('home', homeGameDate, boxscore, ID, homeAbbrev, year)
            for ID in awayPlayers:
                if awayPlayers[ID]['stats']['fielding'] != {}:
                    add('away', awayGameDate, boxscore, ID, awayAbbrev, year)
            fieldingAddDates(homeFieldDates, homeAbbrev, homeGameDate, year)
            fieldingAddDates(awayFieldDates, awayAbbrev, awayGameDate, year)
    else:
        if homeGameDate in homeFieldDates['dates']:
            print(homeAbbrev + " fielding stats already added for " + homeGameDate)
        if awayGameDate in awayFieldDates['dates']:
            print(awayAbbrev + " fielding stats already added for " + awayGameDate)
        print("==============================")
        if game['status'] == 'Suspended':
            input("Suspended Game")
    #     else:
    #         print(homeAbbrev + " fielders have " + homeGameDate + ": " + str((homeGameDate in homeFieldDates['dates'])))
    #         print(awayAbbrev + " fielders have " + awayGameDate + ": " + str((awayGameDate in awayFieldDates['dates'])))
    #         print(game['status'])
    #         print("")

springTraining2021()