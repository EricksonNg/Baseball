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
        print(game)
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

        if game['game_type'] == "R":
            createDir(homeAbbrev, year) #if needed
            createDir(awayAbbrev, year) #if needed

            hit(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore)
            pitch(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore)
            field(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore)
        else:
            print("Game type:", game['game_type'])
            if game['game_type'] != 'Postponed':
                print(game)
                input("Is there a problem here?: ")

def createDir(teamAbbrev, year):
    if path.exists("Teams/" + teamAbbrev + "/" + year):
        print(year + " " + teamAbbrev + " directory exists")
    else:
        makedirs("Teams/" + teamAbbrev + "/" + year)
        print(year + " " + teamAbbrev + " directory created")

def hit(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore):

    def findLastFlyOut(teamAbbrev, playername, year):
        category = 0
        try:
            if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
                    category = content_dict[playername]['hitting']['progression']['fly outs'][-1]
        except Exception as e:
            category = 0
        return category

    def hittersList(teamAbbrev, year, playername):
        if path.exists("Teams/" + teamAbbrev + "/" + year + "/hitters.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("3. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("4. We have an error", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open("Teams/" + teamAbbrev + "/" + year + "/hitters.txt", "w") as f:
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
        print(playername)
        # progressive
        p_flyOuts = findLastFlyOut(teamAbbrev, playername, year) + int(index['stats']['batting']['flyOuts'])
        p_groundOuts = int(index['seasonStats']['batting']['groundOuts'])
        p_runs = int(index['seasonStats']['batting']['runs'])
        p_doubles = int(index['seasonStats']['batting']['doubles'])
        p_triples = int(index['seasonStats']['batting']['triples'])
        p_homeRuns = int(index['seasonStats']['batting']['homeRuns'])
        p_strikeOuts = int(index['seasonStats']['batting']['strikeOuts'])
        p_baseOnBalls = int(index['seasonStats']['batting']['baseOnBalls'])
        p_intentionalWalks = int(index['seasonStats']['batting']['intentionalWalks'])
        p_hits = int(index['seasonStats']['batting']['hits'])
        p_hitByPitch = int(index['seasonStats']['batting']['hitByPitch'])
        p_avg = float(index['seasonStats']['batting']['avg'])
        p_atBats = int(index['seasonStats']['batting']['atBats'])
        p_obp = float(index['seasonStats']['batting']['obp'])
        p_slg = float(index['seasonStats']['batting']['slg'])
        p_ops = float(index['seasonStats']['batting']['ops'])
        p_caughtStealing = int(index['seasonStats']['batting']['caughtStealing'])
        p_stolenBases = int(index['seasonStats']['batting']['stolenBases'])
        try:
            p_stolenBasePercentage = float(index['seasonStats']['batting']['stolenBasePercentage'])
        except ValueError:
            p_stolenBasePercentage = 0.000
        p_groundIntoDoublePlay = int(index['seasonStats']['batting']['groundIntoDoublePlay'])
        p_groundIntoTriplePlay = int(index['seasonStats']['batting']['groundIntoTriplePlay'])
        p_plateAppearances = int(index['seasonStats']['batting']['plateAppearances'])
        p_totalBases = int(index['seasonStats']['batting']['totalBases'])
        p_rbi = int(index['seasonStats']['batting']['rbi'])
        p_leftOnBase = int(index['seasonStats']['batting']['leftOnBase'])
        p_sacBunts = int(index['seasonStats']['batting']['sacBunts'])
        p_sacFlies = int(index['seasonStats']['batting']['sacFlies'])
        try:
            p_babip = float(index['seasonStats']['batting']['babip'])
        except ValueError:
            p_babip = .000
        p_catchersInterference = int(index['seasonStats']['batting']['catchersInterference'])
        p_pickoffs = int(index['seasonStats']['batting']['pickoffs'])
        try:
            p_atBatsPerHomeRun = float(index['seasonStats']['batting']['atBatsPerHomeRun'])
        except ValueError:
            p_atBatsPerHomeRun = 0.00
        # per game
        pg_flyOuts = int(index['stats']['batting']['flyOuts'])
        pg_groundOuts = int(index['stats']['batting']['groundOuts'])
        pg_runs = int(index['stats']['batting']['runs'])
        pg_doubles = int(index['stats']['batting']['doubles'])
        pg_triples = int(index['stats']['batting']['triples'])
        pg_homeRuns = int(index['stats']['batting']['homeRuns'])
        pg_strikeOuts = int(index['stats']['batting']['strikeOuts'])
        pg_baseOnBalls = int(index['stats']['batting']['baseOnBalls'])
        pg_intentionalWalks = int(index['stats']['batting']['intentionalWalks'])
        pg_hits = int(index['stats']['batting']['hits'])
        pg_hitByPitch = int(index['stats']['batting']['hitByPitch'])
        pg_atBats = int(index['stats']['batting']['atBats'])
        pg_caughtStealing = int(index['stats']['batting']['caughtStealing'])
        pg_stolenBases = int(index['stats']['batting']['stolenBases'])
        try:
            pg_stolenBasePercentage = float(index['stats']['batting']['stolenBasePercentage'])
        except ValueError:
            pg_stolenBasePercentage = 0.000
        pg_groundIntoDoublePlay = int(index['stats']['batting']['groundIntoDoublePlay'])
        pg_groundIntoTriplePlay = int(index['stats']['batting']['groundIntoTriplePlay'])
        pg_plateAppearances = int(index['stats']['batting']['plateAppearances'])
        pg_totalBases = int(index['stats']['batting']['totalBases'])
        pg_rbi = int(index['stats']['batting']['rbi'])
        pg_leftOnBase = int(index['stats']['batting']['leftOnBase'])
        pg_sacBunts = int(index['stats']['batting']['sacBunts'])
        pg_sacFlies = int(index['stats']['batting']['sacFlies'])
        pg_catchersInterference = int(index['stats']['batting']['catchersInterference'])
        pg_pickoffs = int(index['stats']['batting']['pickoffs'])
        try:
            pg_atBatsPerHomeRun = float(index['stats']['batting']['atBatsPerHomeRun'])
        except ValueError:
            pg_atBatsPerHomeRun = 0.00

        p_categories = [p_flyOuts, p_groundOuts, p_runs, p_doubles, p_triples, p_homeRuns, p_strikeOuts, p_baseOnBalls, p_intentionalWalks, p_hits, p_hitByPitch, p_avg, p_atBats, p_obp, p_slg, p_ops, p_caughtStealing, p_stolenBases, p_stolenBasePercentage, p_groundIntoDoublePlay, p_groundIntoTriplePlay, p_plateAppearances, p_totalBases, p_rbi, p_leftOnBase, p_sacBunts, p_sacFlies, p_babip, p_catchersInterference, p_pickoffs, p_atBatsPerHomeRun]
        pg_categories = [pg_flyOuts, pg_groundOuts, pg_runs, pg_doubles, pg_triples, pg_homeRuns, pg_strikeOuts, pg_baseOnBalls, pg_intentionalWalks, pg_hits, pg_hitByPitch, pg_atBats, pg_caughtStealing, pg_stolenBases, pg_stolenBasePercentage, pg_groundIntoDoublePlay, pg_groundIntoTriplePlay, pg_plateAppearances, pg_totalBases, pg_rbi, pg_leftOnBase, pg_sacBunts, pg_sacFlies, pg_catchersInterference, pg_pickoffs, pg_atBatsPerHomeRun]
        p_names = ['fly outs', 'ground outs', 'runs', 'doubles', 'triples', 'home runs', 'strike outs', 'walks', 'intentional walks', 'hits', 'hbp', 'avg', 'ab', 'obp', 'slg', 'ops', 'cs', 'sb', 'sbp', 'gidp', 'gitp', 'pa', 'total bases', 'rbi', 'lob', 'sac bunts', 'sac flies', 'babip', 'ci', 'pickoffs', 'ab_per_hr']
        pg_names = ['fly outs', 'ground outs', 'runs', 'doubles', 'triples', 'home runs', 'strike outs', 'walks', 'intentional walks', 'hits', 'hbp', 'ab', 'cs', 'sb', 'sbp', 'gidp', 'gitp', 'pa', 'total bases', 'rbi', 'lob', 'sac bunts', 'sac flies', 'babip', 'ci', 'pickoffs', 'ab per hr']

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            print("============================================")
            print("File Exists For", playername)
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
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
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "pitching" : {"dates": [], "progression": {}, "per_game": {}}, "hitting": {"dates": [], "progression": {}, "per_game": {}}, "fielding" : {"dates": [], "positions": [], "progression": {}, "per_game": {}}}}')
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
            else:
                print("============================================")
                print("Creating File For Hitter", playername)
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "hitting" : {"dates": [], "progression": {}, "per_game": {}}, "fielding": {"dates": [], "positions": [], "progression": {}, "per_game": {}}, "pitching": {"dates": [], "progression": {}, "per_game": {}}}}')
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)

        if gameDate not in content_dict[playername]['hitting']['dates']:
            print("-----Stats not added yet for", gameDate + "-----")
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
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
        if path.exists("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("6. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("7. We have an error", e)
                    print("Database Error ")

    def hittingAddDates(datesFile, teamAbbrev, gameDate, year):
        if gameDate not in datesFile['dates']:
            with open("Teams/" + teamAbbrev + "/" + year + "/h_dates.txt", "w") as f:
                try:
                    datesFile['dates'].append(gameDate)
                    f.write(str(datesFile))
                except Exception as e:
                    print("8. We have an error", e)
                    print("Database Error ")

    homeHitDates = hittingDatesFile(homeAbbrev, year)
    awayHitDates = hittingDatesFile(awayAbbrev, year)

    if (gameDate not in homeHitDates['dates'] or gameDate not in awayHitDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Completed' in game['status']):
        if game["game_type"] == "R":
            awayPlayers = boxscore['teams']['away']['players']
            homePlayers = boxscore['teams']['home']['players']
            for ID in homePlayers:
                if homePlayers[ID]['stats']['batting'] != {}:
                    add('home', gameDate, boxscore, ID, homeAbbrev, year)
            for ID in awayPlayers:
                if awayPlayers[ID]['stats']['batting'] != {}:
                    add('away', gameDate, boxscore, ID, awayAbbrev, year)
            hittingAddDates(homeHitDates, homeAbbrev, gameDate, year)
            hittingAddDates(awayHitDates, awayAbbrev, gameDate, year)
    else:
        if game['status'] == 'Suspended':
            input("Suspended Game")
        else:
            print(homeAbbrev + " hitters have " + gameDate + ": " + str((gameDate in homeHitDates['dates'])))
            print(awayAbbrev + " hitters have " + gameDate + ": " + str((gameDate in awayHitDates['dates'])))
            print(game['status'])
            print("")

def pitch(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore):

    def findLast(teamAbbrev, playername, year, category):
        categories = {'p_stolenBasePercentage': 'sbp', 'p_balls': 'balls', 'p_strikes': 'strikes', 'p_battersFaced': 'batters faced', 'p_numberOfPitches': 'pitches', 'p_rbi': 'rbi'}
        last = 0
        try:
            if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)
                    last = content_dict[playername]['pitching']['progression'][categories[category]][-1]
        except Exception as e:
            print("findLast was used for: " + category + " " +str(e))
            last = 0
        return last

    def pitchersList(teamAbbrev, year, playername):
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
                    print("9. We have an error", e)
                    print("Database Error ")

    def add(homeOrAway, gameDate, boxscore, ID, teamAbbrev, year):
        index = boxscore['teams'][homeOrAway]['players'][ID]
        playername = index['person']['fullName']
        print(playername)
        if index['stats']['pitching']['numberOfPitches'] != 0:
            # per game
            pg_gamesStarted = int(index['stats']['pitching']['gamesStarted'])
            pg_groundOuts = int(index['stats']['pitching']['groundOuts'])
            pg_airOuts = int(index['stats']['pitching']['airOuts'])
            pg_runs = int(index['stats']['pitching']['runs'])
            pg_doubles = int(index['stats']['pitching']['doubles'])
            pg_triples = int(index['stats']['pitching']['triples'])
            pg_homeRuns = int(index['stats']['pitching']['homeRuns'])
            pg_strikeOuts = int(index['stats']['pitching']['strikeOuts'])
            pg_baseOnBalls = int(index['stats']['pitching']['baseOnBalls'])
            pg_intentionalWalks = int(index['stats']['pitching']['intentionalWalks'])
            pg_hits = int(index['stats']['pitching']['hits'])
            pg_hitByPitch = int(index['stats']['pitching']['hitByPitch'])
            pg_atBats = int(index['stats']['pitching']['atBats'])
            pg_caughtStealing = int(index['stats']['pitching']['caughtStealing'])
            pg_stolenBases = int(index['stats']['pitching']['stolenBases'])
            try:
                pg_stolenBasePercentage = float(index['stats']['pitching']['stolenBasePercentage'])
            except ValueError: # if value is a string instead of a number value
                pg_stolenBasePercentage = 0.000
            pg_numberOfPitches = int(index['stats']['pitching']['numberOfPitches'])
            if pg_numberOfPitches == 0:
                input(playername + " has no pitches!")
            pg_inningsPitched = float(index['stats']['pitching']['inningsPitched'])
            if ".1" in str(pg_inningsPitched):
                pg_inningsPitched = int(pg_inningsPitched) + 0.33
            if ".2" in str(pg_inningsPitched):
                pg_inningsPitched = int(pg_inningsPitched) + 0.67
            try:
                pg_whip = round(((pg_hits + pg_hitByPitch + pg_baseOnBalls + pg_intentionalWalks)/pg_inningsPitched),2)
            except ZeroDivisionError:
                pg_whip = float(pg_hits + pg_hitByPitch + pg_baseOnBalls + pg_intentionalWalks)
            pg_wins = int(index['stats']['pitching']['wins'])
            pg_losses = int(index['stats']['pitching']['losses'])
            pg_saves = int(index['stats']['pitching']['saves'])
            pg_saveOpportunities = int(index['stats']['pitching']['saveOpportunities'])
            pg_holds = int(index['stats']['pitching']['holds'])
            pg_blownSaves = int(index['stats']['pitching']['blownSaves'])
            pg_earnedRuns = int(index['stats']['pitching']['earnedRuns'])
            pg_battersFaced = int(index['stats']['pitching']['battersFaced'])
            pg_outs = int(index['stats']['pitching']['outs'])
            pg_completeGames = int(index['stats']['pitching']['completeGames'])
            pg_shutouts = int(index['stats']['pitching']['shutouts'])
            pg_balls = int(index['stats']['pitching']['balls'])
            pg_strikes = int(index['stats']['pitching']['strikes'])
            try:
                pg_strikePercentage = float(index['stats']['pitching']['strikePercentage'])
            except ValueError:
                pg_strikePercentage = 0.000
            pg_balks = int(index['stats']['pitching']['balks'])
            pg_wildPitches = int(index['stats']['pitching']['wildPitches'])
            pg_pickoffs = int(index['stats']['pitching']['pickoffs'])
            pg_rbi = int(index['stats']['pitching']['rbi'])
            pg_gamesFinished = int(index['stats']['pitching']['gamesFinished'])
            try:
                pg_runsScoredPer9 = float(index['stats']['pitching']['runsScoredPer9'])
            except ValueError:
                pg_runsScoredPer9 = float(index['stats']['pitching']['runs'])*27
            try:
                pg_homeRunsPer9 = float(index['stats']['pitching']['homeRunsPer9'])
            except ValueError:
                pg_homeRunsPer9 = float(index['stats']['pitching']['homeRuns'])*27
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

            pg_inheritedRunners = int(index['stats']['pitching']['inheritedRunners'])
            if pg_inheritedRunners > 0:
                input("Inherited Runners is actually greater than 0!")
                input()

            pg_inheritedRunnersScored = int(index['stats']['pitching']['inheritedRunnersScored'])
            pg_catchersInterference = int(index['stats']['pitching']['catchersInterference'])
            pg_sacBunts = int(index['stats']['pitching']['sacBunts'])
            pg_sacFlies = int(index['stats']['pitching']['sacFlies'])
            try:
                pg_pitchesPerInning = float(index['seasonStats']['pitching']['pitchesPerInning'])
            except ValueError:
                pg_pitchesPerInning = float(pg_numberOfPitches)  # Pitches per inning in seasonStats gives the pitches per innings for the pitcher for that one game (it's a per game average, not a season average)

            # progressive
            p_gamesPlayed = int(index['seasonStats']['pitching']['gamesPlayed'])
            p_gamesStarted = int(index['seasonStats']['pitching']['gamesStarted'])
            p_groundOuts = int(index['seasonStats']['pitching']['groundOuts'])
            p_airOuts = int(index['seasonStats']['pitching']['airOuts'])
            p_runs = int(index['seasonStats']['pitching']['runs'])
            p_doubles = int(index['seasonStats']['pitching']['doubles'])
            p_triples = int(index['seasonStats']['pitching']['triples'])
            p_homeRuns = int(index['seasonStats']['pitching']['homeRuns'])
            p_strikeOuts = int(index['seasonStats']['pitching']['strikeOuts'])
            p_baseOnBalls = int(index['seasonStats']['pitching']['baseOnBalls'])
            p_intentionalWalks = int(index['seasonStats']['pitching']['intentionalWalks'])
            p_hits = int(index['seasonStats']['pitching']['hits'])
            p_hitByPitch = int(index['seasonStats']['pitching']['hitByPitch'])
            p_atBats = int(index['seasonStats']['pitching']['atBats'])
            p_obp = float(index['seasonStats']['pitching']['obp'])
            p_caughtStealing = int(index['seasonStats']['pitching']['caughtStealing'])
            p_stolenBases = int(index['seasonStats']['pitching']['stolenBases'])
            try:
                p_stolenBasePercentage = float(index['seasonStats']['pitching']['stolenBasePercentage'])
            except ValueError:
                p_stolenBasePercentage = float(findLast(teamAbbrev, playername, year, 'p_stolenBasePercentage'))
            p_earnedRuns = int(index['seasonStats']['pitching']['earnedRuns']) # p_earnRuns has to be put above p_era to use in the calculation of p_era if there is a ValueError
            try:
                p_era = float(index['seasonStats']['pitching']['era'])
            except ValueError:
                p_era = pg_earnedRuns*27
            p_inningsPitched = float(index['seasonStats']['pitching']['inningsPitched'])
            if ".1" in str(p_inningsPitched):
                p_inningsPitched = int(p_inningsPitched) + 0.33
            if ".2" in str(p_inningsPitched):
                p_inningsPitched = int(p_inningsPitched) + 0.67
            p_wins = int(index['seasonStats']['pitching']['wins'])
            p_losses = int(index['seasonStats']['pitching']['losses'])
            p_saves = int(index['seasonStats']['pitching']['saves'])
            p_saveOpportunities = int(index['seasonStats']['pitching']['saveOpportunities'])
            p_holds = int(index['seasonStats']['pitching']['holds'])
            p_blownSaves = int(index['seasonStats']['pitching']['blownSaves'])
            try:
                p_whip = float(index['seasonStats']['pitching']['whip'])
            except ValueError:
                p_whip = float(p_hits + p_hitByPitch + p_baseOnBalls + p_intentionalWalks)
            p_battersFaced = findLast(teamAbbrev, playername, year, 'p_battersFaced') + pg_battersFaced
            p_outs = int(index['seasonStats']['pitching']['outs'])
            p_completeGames = int(index['seasonStats']['pitching']['completeGames'])
            p_shutouts = int(index['seasonStats']['pitching']['shutouts'])

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

            p_balks = int(index['seasonStats']['pitching']['balks'])
            p_wildPitches = int(index['seasonStats']['pitching']['wildPitches'])
            p_pickoffs = int(index['seasonStats']['pitching']['pickoffs'])
            try:
                p_groundOutsToAirouts = float(index['seasonStats']['pitching']['groundOutsToAirouts'])
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
                p_winPercentage = float(index['seasonStats']['pitching']['winPercentage'])
            except ValueError:
                if p_wins == 0:
                    p_winPercentage = 0.00
                else:
                    input("We have a problem")
            p_gamesFinished = int(index['seasonStats']['pitching']['gamesFinished'])
            try:
                p_strikeoutWalkRatio = float(index['seasonStats']['pitching']['strikeoutWalkRatio'])
            except ValueError:
                if p_strikeOuts == 0 and p_baseOnBalls == 0:
                    p_strikeoutWalkRatio = 0.00
                elif p_baseOnBalls == 0:
                    p_strikeoutWalkRatio = float(p_strikeOuts)
                elif p_strikeOuts == 0:
                    p_strikeoutWalkRatio = 1.0/p_baseOnBalls
            try:
                p_strikeoutsPer9Inn = float(index['seasonStats']['pitching']['strikeoutsPer9Inn'])
            except ValueError:
                p_strikeoutsPer9Inn = float(pg_strikeOuts)*27 # Relates to pg_strikeOutsPer9
            try:
                p_walksPer9Inn = float(index['seasonStats']['pitching']['walksPer9Inn'])
            except ValueError:
                p_walksPer9Inn = float(pg_baseOnBalls)*27 # Relates to pg_walksPer9
            try:
                p_hitsPer9Inn = float(index['seasonStats']['pitching']['hitsPer9Inn'])
            except ValueError:
                p_hitsPer9Inn = float(pg_hits)*27 # Relates to pg_hitsPer9
            try:
                p_runsScoredPer9 = float(index['seasonStats']['pitching']['runsScoredPer9'])
            except ValueError:
                p_runsScoredPer9 = float(pg_runs)*27
            try:
                p_homeRunsPer9 = float(index['seasonStats']['pitching']['homeRunsPer9'])
            except ValueError:
                p_homeRunsPer9 = float(pg_homeRuns)*27
            p_inheritedRunnersScored = int(index['seasonStats']['pitching']['inheritedRunnersScored'])
            p_catchersInterference = int(index['seasonStats']['pitching']['catchersInterference'])
            p_sacBunts = int(index['seasonStats']['pitching']['sacBunts'])
            p_sacFlies = int(index['seasonStats']['pitching']['sacFlies'])

            p_categories = [p_gamesPlayed, p_gamesStarted, p_groundOuts, p_airOuts, p_runs, p_doubles, p_triples, p_homeRuns, p_strikeOuts, p_baseOnBalls, p_intentionalWalks, p_hits, p_hitByPitch, p_atBats, p_obp, p_caughtStealing, p_stolenBases, p_stolenBasePercentage, p_era, p_inningsPitched, p_wins, p_losses, p_saves, p_saveOpportunities, p_holds, p_blownSaves, p_earnedRuns, p_whip, p_battersFaced, p_outs, p_completeGames, p_shutouts, p_balls, p_strikes, p_numberOfPitches, p_strikePercentage, p_pitchesPerInning,p_balks,p_wildPitches, p_pickoffs, p_groundOutsToAirouts, p_rbi,p_winPercentage, p_gamesFinished, p_strikeoutWalkRatio, p_strikeoutsPer9Inn, p_walksPer9Inn, p_hitsPer9Inn, p_runsScoredPer9, p_homeRunsPer9, p_inheritedRunnersScored, p_catchersInterference, p_sacBunts, p_sacFlies]

            p_names = ['g', 'gs', 'ground outs', 'air outs', 'runs', 'doubles', 'triples', 'home runs', 'strike outs', 'walks', 'intentional walks', 'hits', 'hbp', 'ab', 'obp', 'cs', 'sb', 'sbp', 'era', 'innings', 'wins', 'losses', 'saves', 'save opportunities', 'holds', 'blown saves', 'earned runs', 'whip', 'batters faced', 'outs', 'complete games', 'shut outs', 'balls', 'strikes', 'pitches', 'strike percentage', 'pitches per inning','balks', 'wild pitches', 'pickoffs', 'ground to air', 'rbi', 'win percentage', 'games finished', 'strikeout to walk', 'strikeouts per 9', 'walks per 9', 'hits per 9', 'runs per 9', 'home runs per 9', 'inherited runners scored', 'catchers interference', 'sac bunts', 'sac flies']

            pg_categories = [pg_gamesStarted, pg_groundOuts, pg_airOuts, pg_runs, pg_doubles, pg_triples, pg_homeRuns, pg_strikeOuts, pg_baseOnBalls, pg_intentionalWalks, pg_hits, pg_hitByPitch, pg_atBats, pg_caughtStealing, pg_stolenBases, pg_stolenBasePercentage, pg_numberOfPitches, pg_inningsPitched, pg_whip, pg_pitchesPerInning, pg_wins, pg_losses, pg_saves, pg_saveOpportunities, pg_holds, pg_blownSaves, pg_earnedRuns, pg_battersFaced, pg_outs, pg_completeGames, pg_shutouts, pg_balls, pg_strikes, pg_strikePercentage, pg_balks, pg_wildPitches, pg_pickoffs, pg_rbi, pg_gamesFinished, pg_runsScoredPer9, pg_homeRunsPer9, pg_strikeOutsPer9, pg_walksPer9, pg_hitsPer9,pg_inheritedRunnersScored, pg_catchersInterference, pg_sacBunts, pg_sacFlies]
            pg_names = ['gs', 'ground outs', 'air outs', 'runs', 'doubles', 'triples', 'home runs', 'strike outs', 'walks', 'intentional walks', 'hits', 'hbp', 'ab', 'cs', 'sb', 'sbp', 'pitches', 'innings', 'whip','pitches per inning','wins', 'losses', 'saves', 'save opportunities', 'holds', 'blown saves', 'earned runs', 'batters faced', 'outs', 'complete games', 'shut outs', 'balls', 'strikes', 'strike percentage', 'balks', 'wild pitches', 'pickoffs', 'rbi', 'games finished', 'runs per 9', 'home runs per 9', 'strikeouts per 9', 'walks per 9', 'hits per 9', 'inherited runners scored', 'catchers interference', 'sac bunts', 'sac flies']

            if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                print("============================================")
                print("File Exists For", playername)
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    try:
                        content_dict = eval(content)
                    except Exception as e:
                        print("we got an error ", e)
                        print("Database Error ")
                    else:
                        print("Read success for", playername)
            else:
                print("============================================")
                print("Creating File For Pitcher", playername)
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                    f.write(
                        '{"' + playername + '": {"ID":"' + ID + '", "pitching" : {"dates": [], "progression": {}, "per_game": {}}, "hitting": {"dates": [], "progression": {}, "per_game": {}}, "fielding" : {"dates": [], "positions": [], "progression": {}, "per_game": {}}}}')
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                    content = FILE.read()
                    content_dict = eval(content)

            if gameDate not in content_dict[playername]['pitching']['dates']:
                print("-----Stats not added yet for", gameDate + "-----")
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
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
                        print("we got an error ", e)
                        print("Database Error ")
            else:
                print("-----Stats already added for", gameDate + "-----")
                print("============================================")
        else:
            print(playername + " has " + str(index['stats']['pitching']['numberOfPitches']) + " pitches with " + str(index['stats']['pitching']['caughtStealing']) + " caught stealing and " + str(index['stats']['pitching']['pickoffs']) + " pickoffs")

        pitchersList(teamAbbrev, year, playername)

    def pitchingDatesFile(teamAbbrev, year):
        if path.exists("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("10. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("11. We have an error", e)
                    print("Database Error ")

    def pitchingAddDates(datesFile, teamAbbrev, gameDate, year):
        if gameDate not in datesFile['dates']:
            with open("Teams/" + teamAbbrev + "/" + year + "/p_dates.txt", "w") as f:
                try:
                    datesFile['dates'].append(gameDate)
                    f.write(str(datesFile))
                except Exception as e:
                    print("12. We have an error", e)
                    print("Database Error ")

    homePitchDates = pitchingDatesFile(homeAbbrev, year)
    awayPitchDates = pitchingDatesFile(awayAbbrev, year)

    if (gameDate not in homePitchDates['dates'] or gameDate not in awayPitchDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Completed' in game['status']):
        if game["game_type"] == "R":
            awayPlayers = boxscore['teams']['away']['players']
            homePlayers = boxscore['teams']['home']['players']
            for ID in homePlayers:
                if homePlayers[ID]['stats']['pitching'] != {}:
                    add('home', gameDate, boxscore, ID, homeAbbrev, year)
            for ID in awayPlayers:
                if awayPlayers[ID]['stats']['pitching'] != {}:
                    add('away', gameDate, boxscore, ID, awayAbbrev, year)
            pitchingAddDates(homePitchDates, homeAbbrev, gameDate, year)
            pitchingAddDates(awayPitchDates, awayAbbrev, gameDate, year)
    else:
        if game['status'] == 'Suspended':
            input("Suspended Game")
        else:
            print(homeAbbrev + " pitchers have " + gameDate + ": " + str((gameDate in homePitchDates['dates'])))
            print(awayAbbrev + " pitchers have " + gameDate + ": " + str((gameDate in awayPitchDates['dates'])))
            print(game['status'])
            print("")

def field(homeAbbrev, awayAbbrev, year, gameDate, game, boxscore):

    def fieldersList(teamAbbrev, year, playername):
        if path.exists("Teams/" + teamAbbrev + "/" + year + "/fielders.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/fielders.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("3. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/fielders.txt", "w") as FILE:
                FILE.write("{'players':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/fielders.txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("4. We have an error", e)
                    print("Database Error ")

        if playername not in content_dict['players']:
            with open("Teams/" + teamAbbrev + "/" + year + "/fielders.txt", "w") as f:
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
            if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
                with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
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
        print(playername)
        # per game (placed above progressive so p_gamesStarted can get value of pg_gamesStarted)
        pg_assists = int(index['stats']['fielding']['assists'])
        pg_putOuts = int(index['stats']['fielding']['putOuts'])
        pg_errors = int(index['stats']['fielding']['errors'])
        pg_chances = int(index['stats']['fielding']['chances'])
        pg_caughtStealing = int(index['stats']['fielding']['caughtStealing'])
        pg_passedBall = int(index['stats']['fielding']['passedBall'])
        try:
            pg_gamesStarted = int(index['stats']['fielding']['gamesStarted'])
        except KeyError:
            pg_gamesStarted = 0
        pg_stolenBases = int(index['stats']['fielding']['stolenBases'])
        try:
            pg_stolenBasePercentage = float(index['stats']['fielding']['stolenBasePercentage'])
        except ValueError:
            pg_stolenBasePercentage = 0.000
        pg_pickoffs = int(index['stats']['fielding']['pickoffs'])
        # progressive
        p_assists = int(index['seasonStats']['fielding']['assists'])
        p_putOuts = int(index['seasonStats']['fielding']['putOuts'])
        p_errors = int(index['seasonStats']['fielding']['errors'])
        p_chances = int(index['seasonStats']['fielding']['chances'])
        p_fielding = float(index['seasonStats']['fielding']['fielding'])
        p_caughtStealing = int(index['seasonStats']['fielding']['caughtStealing'])
        p_passedBall = int(index['seasonStats']['fielding']['passedBall'])
        p_gamesStarted = findLastGameStart(teamAbbrev, playername, year) + pg_gamesStarted
        p_stolenBases = int(index['seasonStats']['fielding']['stolenBases'])
        try:
            p_stolenBasePercentage = float(index['seasonStats']['fielding']['stolenBasePercentage'])
        except ValueError:
            p_stolenBasePercentage = 0.000
        p_pickoffs = int(index['seasonStats']['fielding']['pickoffs'])

        p_categories = [p_assists, p_putOuts, p_errors, p_chances, p_fielding, p_caughtStealing, p_passedBall, p_gamesStarted, p_stolenBases, p_stolenBasePercentage, p_pickoffs]
        pg_categories = [pg_assists, pg_putOuts, pg_errors, pg_chances, pg_caughtStealing, pg_passedBall, pg_gamesStarted, pg_stolenBases, pg_stolenBasePercentage, pg_pickoffs]
        p_names = ['assists', 'put outs', 'errors', 'chances', 'fielding percentage', 'cs', 'passed balls', 'gs', 'sb', 'sbp', 'pickoffs']
        pg_names = ['assists', 'put outs', 'errors', 'chances', 'cs', 'passed balls', 'gs', 'sb', 'sbp', 'pickoffs']

        if path.exists("Teams/" + teamAbbrev + "/" + year + "/" + playername + ".txt"):
            print("============================================")
            print("File Exists For", playername)
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                try:
                    content_dict = eval(content)
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
                else:
                    print("Read success for", playername)
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
                f.write(
                    '{"' + playername + '": {"ID":"' + ID + '", "hitting" : {"dates": [], "progression": {}, "per_game": {}}, "fielding": {"dates": [], "positions": [], "progression": {}, "per_game": {}},"pitching": {"dates": [], "progression": {}, "per_game": {}}}}')
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "r") as FILE:
                content = FILE.read()
                content_dict = eval(content)

        if gameDate not in content_dict[playername]['fielding']['dates']:
            print("-----Stats not added yet for", gameDate + "-----")
            with open("Teams/" + teamAbbrev + "/" + year + "/" + str(playername) + ".txt", "w") as f:
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
                    position = index['position']['abbreviation']
                    content_dict[playername]['fielding']['positions'].append(position)
                    f.write(str(content_dict))
                    print("============================================")
                except Exception as e:
                    print("we got an error ", e)
                    print("Database Error ")
        else:
            print("-----Stats already added for", gameDate + "-----")
            print("============================================")

        fieldersList(teamAbbrev, year, playername)

    def fieldingDatesFile(teamAbbrev, year):
        if path.exists("Teams/" + teamAbbrev + "/" + year + "/f_dates.txt"):
            with open("Teams/" + teamAbbrev + "/" + year + "/f_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("6. We have an error", e)
                    print("Database Error ")
        else:
            with open("Teams/" + teamAbbrev + "/" + year + "/f_dates.txt", "w") as FILE:
                FILE.write("{'dates':[]}")
            with open("Teams/" + teamAbbrev + "/" + year + "/f_dates.txt", "r") as FILE:
                content = FILE.read()
                try:
                    return eval(content)
                except Exception as e:
                    print("7. We have an error", e)
                    print("Database Error ")

    def fieldingAddDates(datesFile, teamAbbrev, gameDate, year):
        if gameDate not in datesFile['dates']:
            with open("Teams/" + teamAbbrev + "/" + year + "/f_dates.txt", "w") as f:
                try:
                    datesFile['dates'].append(gameDate)
                    f.write(str(datesFile))
                except Exception as e:
                    print("8. We have an error", e)
                    print("Database Error ")

    homeFieldDates = fieldingDatesFile(homeAbbrev, year)
    awayFieldDates = fieldingDatesFile(awayAbbrev, year)

    if (gameDate not in homeFieldDates['dates'] or gameDate not in awayFieldDates['dates']) and (
            game['status'] == "Final" or game['status'] == "Game Over" or 'Completed' in game['status']):
        if game["game_type"] == "R":
            awayPlayers = boxscore['teams']['away']['players']
            homePlayers = boxscore['teams']['home']['players']
            for ID in homePlayers:
                if homePlayers[ID]['stats']['fielding'] != {}:
                    add('home', gameDate, boxscore, ID, homeAbbrev, year)
            for ID in awayPlayers:
                if awayPlayers[ID]['stats']['fielding'] != {}:
                    add('away', gameDate, boxscore, ID, awayAbbrev, year)
            fieldingAddDates(homeFieldDates, homeAbbrev, gameDate, year)
            fieldingAddDates(awayFieldDates, awayAbbrev, gameDate, year)
    else:
        if game['status'] == 'Suspended':
            input("Suspended Game")
        else:
            print(homeAbbrev + " fielders have " + gameDate + ": " + str((gameDate in homeFieldDates['dates'])))
            print(awayAbbrev + " fielders have " + gameDate + ": " + str((gameDate in awayFieldDates['dates'])))
            print(game['status'])
            print("")


everything()
