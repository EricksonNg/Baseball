def p(playername, category, year, team):

    with open("Teams/"+team+"/"+year+"/"+playername+".txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
        index = content_dict[playername]['pitching']['progression']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername]['pitching']['dates']
        games = index['g']
        gamesStarted = index['gs']
        groundOuts = index['ground outs']
        airOuts = index['air outs']
        era = index['era']
        innings = index['innings']
        hits = index['hits']
        runs = index['runs']
        doubles = index['doubles']
        triples = index['triples']
        homeRuns = index['home runs']
        strikeOuts = index['strike outs']
        walks = index['walks']
        earnedRuns = index['earned runs']
        whip = index['whip']
        battersFaced = index['batters faced']
        outs = index['outs']
        completeGames = index['complete games']
        shutOuts = index['shut outs']
        balls = index['balls']
        strikes = index['strikes']
        pitches = index['pitches']
        strikePercentage = index['strike percentage']
        pitchesPerInning = index['pitches per inning']
        balks = index['balks']
        wildPitches = index['wild pitches']
        pickoffs = index['pickoffs']
        groundToAir = index['ground to air']
        runsBattedIn = index['rbi']
        winPercentage = index['win percentage']
        gamesFinished = index['games finished']
        strikeoutToWalk = index['strikeout to walk']
        strikeoutsPer9 = index['strikeouts per 9']
        walksPer9 = index['walks per 9']
        hitsPer9 = index['hits per 9']
        runsPer9 = index['runs per 9']
        homeRunsPer9 = index['home runs per 9']
        inheritedRunnersScored = index['inherited runners scored']
        catchersInterference = index['catchers interference']
        sacBunts = index['sac bunts']
        sacFlies = index['sac flies']
        intentionalWalks = index['intentional walks']
        hitByPitches = index['hbp']
        atBats = index['ab']
        onBasePercentage = index['obp']
        caughtStealing = index['cs']
        stolenBases = index['sb']
        stolenBasePercentage = index['sbp']
        wins = index['wins']
        losses = index['losses']
        saves = index['saves']
        saveOpportunities = index['save opportunities']
        holds = index['holds']
        blownSaves = index['blown saves']
        battingAverageAgainst = index['baa']
        strikeOutPercentage = index['strike out percentage']

    # sanitize
    stat = {
        'Strikeout Percentage': strikeOutPercentage,

        'Batting Average Against': battingAverageAgainst,

        'Games': games,

        'Games Started': gamesStarted,

        'Ground Outs': groundOuts,

        'Air Outs': airOuts,

        'WHIP': whip,

        'Batters Faced': battersFaced,

        'Outs': outs,

        'Complete Games': completeGames,

        'Shut Outs': shutOuts,

        'Balls': balls,

        'Strikes': strikes,

        'Pitches': pitches,

        'Strike Percentage': strikePercentage,

        'Pitches Per Inning': pitchesPerInning,

        'Balks': balks,

        'Wild Pitches': wildPitches,

        'Pickoffs': pickoffs,

        'Ground to Air': groundToAir,

        'Runs Batted In': runsBattedIn,

        'Win Percentage': winPercentage,

        'Games Finished': gamesFinished,

        'Strikeout To Walk': strikeoutToWalk,

        'Strikeouts Per 9': strikeoutsPer9,

        'Walks Per 9': walksPer9,

        'Hits Per 9': hitsPer9,

        'Runs Per 9': runsPer9,

        'Home Runs Per 9': homeRunsPer9,

        'Inherited Runners Scored': inheritedRunnersScored,

        'Catchers Interferences': catchersInterference,

        'Sacrifice Bunts': sacBunts,

        'Sacrifice Flies': sacFlies,

        'Intentional Walks': intentionalWalks,

        'Hit By Pitches': hitByPitches,

        'Caught Stealings': caughtStealing,

        'Stolen Bases': stolenBases,

        'Stolen Base Percentage': stolenBasePercentage,

        'Saves': saves,

        'Save Opportunities': saveOpportunities,

        'era': era,
        'Era': era,
        'ERA': era,

        'ip': innings,
        'innings': innings,
        'IP': innings,
        'Innings': innings,

        'h': hits,
        'hits': hits,
        'H': hits,
        'Hits': hits,

        'r': runs,
        'run': runs,
        'runs': runs,
        'R': runs,
        'Run': runs,
        'Runs': runs,

        'er': earnedRuns,
        'earned run': earnedRuns,
        'earned runs': earnedRuns,
        'Er': earnedRuns,
        'ER': earnedRuns,
        'Earned run': earnedRuns,
        'Earned runs': earnedRuns,
        'Earned Runs': earnedRuns,

        'bb': walks,
        'base on ball': walks,
        'base on balls': walks,
        'walk': walks,
        'walks': walks,
        'Bb': walks,
        'BB': walks,
        'Base on ball': walks,
        'Base on balls': walks,
        'Walk': walks,
        'Walks': walks,

        'k': strikeOuts,
        'strikeout': strikeOuts,
        'strikeouts': strikeOuts,
        'K': strikeOuts,
        'Strikeout': strikeOuts,
        'Strikeouts': strikeOuts,

        'hr': homeRuns,
        'homerun': homeRuns,
        'home run': homeRuns,
        'homeruns': homeRuns,
        'home runs': homeRuns,
        'Hr': homeRuns,
        'Homerun': homeRuns,
        'Homeruns': homeRuns,
        'Home run': homeRuns,
        'Home runs': homeRuns,
        'Home Run': homeRuns,
        'Home Runs': homeRuns,
        'HR': homeRuns,

        'double': doubles,
        'doubles': doubles,
        'Double': doubles,
        'Doubles': doubles,

        'triple': triples,
        'triples': triples,
        'Triple': triples,
        'Triples': triples,

        'ab': atBats,
        'at bat': atBats,
        'at bats': atBats,
        'At bat': atBats,
        'At bats': atBats,
        'At Bat': atBats,
        'At Bats': atBats,
        'AB': atBats,

        'obp': onBasePercentage,
        'on base percentage': onBasePercentage,
        'on base percentages': onBasePercentage,
        'Obp': onBasePercentage,
        'On base percentage': onBasePercentage,
        'On base percentages': onBasePercentage,
        'On Base Percentage': onBasePercentage,
        'On Base Percentages': onBasePercentage,
        'OBP': onBasePercentage,

        'win': wins,
        'wins': wins,
        'w': wins,
        'Win': wins,
        'Wins': wins,
        'W': wins,

        'loss': losses,
        'losses': losses,
        'l': losses,
        'Loss': losses,
        'Losses': losses,
        'L': losses,

        'hold': holds,
        'holds': holds,
        'Hold': holds,
        'Holds': holds,

        'blown save': blownSaves,
        'blown saves': blownSaves,
        'Blown save': blownSaves,
        'Blown saves': blownSaves,
        'Blown Save': blownSaves,
        'Blown Saves': blownSaves
    }

    name = {
        'Strikeout Percentage': 'Strikeout Percentage',

        'Batting Average Against': 'Batting Average Against',

        'Games': 'Games',

        'Games Started': 'Games Started',

        'Ground Outs': 'Ground Outs',

        'Air Outs': 'Air Outs',

        'WHIP': 'WHIP',

        'Batters Faced': 'Batters Faced',

        'Outs': 'Outs',

        'Complete Games': 'Complete Games',

        'Shut Outs': 'Shut Outs',

        'Balls': 'Balls',

        'Strikes': 'Strikes',

        'Pitches': 'Pitches',

        'Strike Percentage': 'Strike Percentage',

        'Pitches Per Inning': 'Pitches Per Inning',

        'Balks': 'Balks',

        'Wild Pitches': 'Wild Pitches',

        'Pickoffs': 'Pickoffs',

        'Ground to Air': 'Ground To Air',

        'Runs Batted In': 'Runs Batted In Against',

        'Win Percentage': 'Win Percentage',

        'Games Finished': 'Games Finished',

        'Strikeout To Walk': 'Strikeout To Walk',

        'Strikeouts Per 9': 'Strikeouts Per 9',

        'Walks Per 9': 'Walks Per 9',

        'Hits Per 9': 'Hits Per 9',

        'Runs Per 9': 'Runs Per 9',

        'Home Runs Per 9': 'Home Runs Per 9',

        'Inherited Runners Scored': 'Inherited Runners Scored',

        'Catchers Interferences': 'Catchers Interferences',

        'Sacrifice Bunts': 'Sacrifice Bunts',

        'Sacrifice Flies': 'Sacrifice Flies',

        'Intentional Walks': 'Intentional Walks',

        'Hit By Pitches': 'Hit By Pitches',

        'Caught Stealings': 'Caught Stealings',

        'Stolen Bases': 'Stolen Bases',

        'Stolen Base Percentage': 'Stolen Base Percentage',

        'Saves': 'Saves',

        'Save Opportunities': 'Save Opportunities',

        'era': 'ERA',
        'Era': 'ERA',
        'ERA': 'ERA',

        'ip': 'Innings',
        'innings': 'Innings',
        'IP': 'Innings',
        'Innings': 'Innings',

        'h': 'Hits',
        'hits': 'Hits',
        'H': 'Hits',
        'Hits': 'Hits',

        'r': 'Runs',
        'run': 'Runs',
        'runs': 'Runs',
        'R': 'Runs',
        'Run': 'Runs',
        'Runs': 'Runs',

        'er': 'Earned Runs',
        'earned run': 'Earned Runs',
        'earned runs': 'Earned Runs',
        'Er': 'Earned Runs',
        'ER': 'Earned Runs',
        'Earned run': 'Earned Runs',
        'Earned runs': 'Earned Runs',
        'Earned Runs': 'Earned Runs',

        'bb': 'Walks',
        'base on ball': 'Walks',
        'base on balls': 'Walks',
        'walk': 'Walks',
        'walks': 'Walks',
        'Bb': 'Walks',
        'BB': 'Walks',
        'Base on ball': 'Walks',
        'Base on balls': 'Walks',
        'Walk': 'Walks',
        'Walks': 'Walks',

        'k': 'Strikeouts',
        'strikeout': 'Strikeouts',
        'strikeouts': 'Strikeouts',
        'K': 'Strikeouts',
        'Strikeout': 'Strikeouts',
        'Strikeouts': 'Strikeouts',

        'hr': 'Home Runs',
        'homerun': 'Home Runs',
        'home run': 'Home Runs',
        'homeruns': 'Home Runs',
        'home runs': 'Home Runs',
        'Hr': 'Home Runs',
        'Homerun': 'Home Runs',
        'Homeruns': 'Home Runs',
        'Home run': 'Home Runs',
        'Home runs': 'Home Runs',
        'Home Run': 'Home Runs',
        'Home Runs': 'Home Runs',
        'HR': 'Home Runs',

        'double': 'Doubles',
        'doubles': 'Doubles',
        'Double': 'Doubles',
        'Doubles': 'Doubles',

        'triple': 'Triples',
        'triples': 'Triples',
        'Triple': 'Triples',
        'Triples': 'Triples',

        'ab': 'At Bats',
        'at bat': 'At Bats',
        'at bats': 'At Bats',
        'At bat': 'At Bats',
        'At bats': 'At Bats',
        'At Bat': 'At Bats',
        'At Bats': 'At Bats',
        'AB': 'At Bats',

        'obp': 'On Base Percentage',
        'on base percentage': 'On Base Percentage',
        'on base percentages': 'On Base Percentage',
        'Obp': 'On Base Percentage',
        'On base percentage': 'On Base Percentage',
        'On base percentages': 'On Base Percentage',
        'On Base Percentage': 'On Base Percentage',
        'On Base Percentages': 'On Base Percentage',
        'OBP': 'On Base Percentage',

        'win': 'Wins',
        'wins': 'Wins',
        'w': 'Wins',
        'Win': 'Wins',
        'Wins': 'Wins',
        'W': 'Wins',

        'loss': 'Losses',
        'losses': 'Losses',
        'l': 'Losses',
        'Loss': 'Losses',
        'Losses': 'Losses',
        'L': 'Losses',

        'hold': 'Holds',
        'holds': 'Holds',
        'Hold': 'Holds',
        'Holds': 'Holds',

        'blown save': 'Blown Saves',
        'blown saves': 'Blown Saves',
        'Blown save': 'Blown Saves',
        'Blown saves': 'Blown Saves',
        'Blown Save': 'Blown Saves',
        'Blown Saves': 'Blown Saves'
    }

    return dates, stat[category], playername+"'s "+name[category]+" (Progressive)"

def pg(playername, category, year, team):

    with open("Teams/"+team+"/"+year+"/"+playername+".txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
        index = content_dict[playername]['pitching']['per_game']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername]['pitching']['dates']
        gamesStarted = index['gs']
        groundOuts = index['ground outs']
        airOuts = index['air outs']
        runs = index['runs']
        doubles = index['doubles']
        triples = index['triples']
        homeRuns = index['home runs']
        strikeOuts = index['strike outs']
        walks = index['walks']
        intentionalWalks = index['intentional walks']
        hits = index['hits']
        hitByPitches = index['hbp']
        atBats = index['ab']
        caughtStealings = index['cs']
        stolenBases = index['sb']
        stolenBasePercentage = index['sbp']
        pitches = index['pitches']
        innings = index['innings']
        wins = index['wins']
        losses = index['losses']
        saves = index['saves']
        saveOpportunities = index['save opportunities']
        holds = index['holds']
        blownSaves = index['blown saves']
        earnedRuns = index['earned runs']
        battersFaced = index['batters faced']
        completeGames = index['complete games']
        shutOuts = index['shut outs']
        balls = index['balls']
        strikes = index['strikes']
        strikePercentage = index['strike percentage']
        balks = index['balks']
        wildPitches = index['wild pitches']
        pickoffs = index['pickoffs']
        runsBattedIn = index['rbi']
        gamesFinished = index['games finished']
        runsPer9 = index['runs per 9']
        homeRunsPer9 = index['home runs per 9']
        inheritedRunnersScored = index['inherited runners scored']
        catchersInterferences = index['catchers interference']
        sacrificeBunts = index['sac bunts']
        sacrificeFlies = index['sac flies']

    stat = {
        'Games Started': gamesStarted,

        'Ground Outs': groundOuts,

        'Air Outs': airOuts,

        'Doubles': doubles,

        'Triples': triples,

        'Intentional Walks': intentionalWalks,

        'Hit By Pitches': hitByPitches,

        'At Bats': atBats,

        'Caught Stealings': caughtStealings,

        'Stolen Bases': stolenBases,

        'Stolen Base Percentage': stolenBasePercentage,

        'Wins': wins,

        'Losses': losses,

        'Saves': saves,

        'Save Opportunities': saveOpportunities,

        'Holds': holds,

        'Blown Saves': blownSaves,

        'Batters Faced': battersFaced,

        'Complete Games': completeGames,

        'Shut Outs': shutOuts,

        'Balls': balls,

        'Strike Percentage': strikePercentage,

        'Balks': balks,

        'Wild Pitches': wildPitches,

        'Pickoffs': pickoffs,

        'Runs Batted In': runsBattedIn,

        'Games Finished': gamesFinished,

        'Runs Per 9': runsPer9,

        'Home Runs Per 9': homeRunsPer9,

        'Inherited Runners Scored': inheritedRunnersScored,

        'Catchers Interferences': catchersInterferences,

        'Sacrifice Bunts': sacrificeBunts,

        'Sac Flies': sacrificeFlies,

        'ip': innings,
        'innings': innings,
        'IP': innings,
        'Innings': innings,

        'h': hits,
        'hits': hits,
        'H': hits,
        'Hits': hits,

        'r': runs,
        'run': runs,
        'runs': runs,
        'R': runs,
        'Run': runs,
        'Runs': runs,

        'er': earnedRuns,
        'earned run': earnedRuns,
        'earned runs': earnedRuns,
        'Er': earnedRuns,
        'ER': earnedRuns,
        'Earned run': earnedRuns,
        'Earned runs': earnedRuns,
        'Earned Run': earnedRuns,
        'Earned Runs': earnedRuns,

        'bb': walks,
        'base on ball': walks,
        'base on balls': walks,
        'walk': walks,
        'walks': walks,
        'Bb': walks,
        'BB': walks,
        'Base on ball': walks,
        'Base on balls': walks,
        'Walk': walks,
        'Walks': walks,

        'k': strikeOuts,
        'strikeout': strikeOuts,
        'strikeouts': strikeOuts,
        'K': strikeOuts,
        'Strikeout': strikeOuts,
        'Strikeouts': strikeOuts,

        'hr': homeRuns,
        'homerun': homeRuns,
        'home run': homeRuns,
        'homeruns': homeRuns,
        'home runs': homeRuns,
        'Hr': homeRuns,
        'Homerun': homeRuns,
        'Homeruns': homeRuns,
        'Home run': homeRuns,
        'Home runs': homeRuns,
        'Home Run': homeRuns,
        'Home Runs': homeRuns,
        'HR': homeRuns,

        'p': pitches,
        'pitch': pitches,
        'pitches': pitches,
        'P': pitches,
        'Pitch': pitches,
        'Pitches': pitches,

        's': strikes,
        'strike': strikes,
        'strikes': strikes,
        'S': strikes,
        'Strike': strikes,
        'Strikes': strikes

    }

    name = {
        'Games Started': 'Games Started',

        'Ground Outs': 'Ground Outs',

        'Air Outs': 'Air Outs',

        'Doubles': 'Doubles',

        'Triples': 'Triples',

        'Intentional Walks': 'Intentional Walks',

        'Hit By Pitches': 'Hit By Pitches',

        'At Bats': 'At Bats',

        'Caught Stealings': 'Caught Stealings',

        'Stolen Bases': 'Stolen Bases',

        'Stolen Base Percentage': 'Stolen Base Percentage',

        'Wins': 'Wins',

        'Losses': 'Losses',

        'Saves': 'Saves',

        'Save Opportunities': 'Save Opportunites',

        'Holds': 'Holds',

        'Blown Saves': 'Blown Saves',

        'Batters Faced': 'Batters Faced',

        'Complete Games': 'Complete Games',

        'Shut Outs': 'Shut Outs',

        'Balls': 'Balls',

        'Strike Percentage': 'Strike Percentage',

        'Balks': 'Balks',

        'Wild Pitches': 'Wild Pitches',

        'Pickoffs': 'Pickoffs',

        'Runs Batted In': 'Runs Batted In',

        'Games Finished': 'Games Finished',

        'Runs Per 9': 'Runs Per 9',

        'Home Runs Per 9': 'Home Runs Per 9',

        'Inherited Runners Scored': 'Inherited Runners Scored',

        'Catchers Interferences': 'Catchers Interferences',

        'Sacrifice Bunts': 'Sacrifice Bunts',

        'Sac Flies': 'Sac Flies',

        'ip': 'Innings',
        'innings': 'Innings',
        'IP': 'Innings',
        'Innings': 'Innings',

        'h': 'Hits',
        'hits': 'Hits',
        'H': 'Hits',
        'Hits': 'Hits',

        'r': 'Runs',
        'run': 'Runs',
        'runs': 'Runs',
        'R': 'Runs',
        'Run': 'Runs',
        'Runs': 'Runs',

        'er': 'Earned Runs',
        'earned run': 'Earned Runs',
        'earned runs': 'Earned Runs',
        'Er': 'Earned Runs',
        'ER': 'Earned Runs',
        'Earned run': 'Earned Runs',
        'Earned runs': 'Earned Runs',
        'Earned Run': 'Earned Runs',
        'Earned Runs': 'Earned Runs',

        'bb': 'Walks',
        'base on ball': 'Walks',
        'base on balls': 'Walks',
        'walk': 'Walks',
        'walks': 'Walks',
        'Bb': 'Walks',
        'BB': 'Walks',
        'Base on ball': 'Walks',
        'Base on balls': 'Walks',
        'Walk': 'Walks',
        'Walks': 'Walks',

        'k': 'Strikeouts',
        'strikeout': 'Strikeouts',
        'strikeouts': 'Strikeouts',
        'K': 'Strikeouts',
        'Strikeout': 'Strikeouts',
        'Strikeouts': 'Strikeouts',

        'hr': 'Home Runs',
        'homerun': 'Home Runs',
        'home run': 'Home Runs',
        'homeruns': 'Home Runs',
        'home runs': 'Home Runs',
        'Hr': 'Home Runs',
        'Homerun': 'Home Runs',
        'Homeruns': 'Home Runs',
        'Home run': 'Home Runs',
        'Home runs': 'Home Runs',
        'Home Run': 'Home Runs',
        'Home Runs': 'Home Runs',
        'HR': 'Home Runs',

        'p': 'Pitches',
        'pitch': 'Pitches',
        'pitches': 'Pitches',
        'P': 'Pitches',
        'Pitch': 'Pitches',
        'Pitches': 'Pitches',

        's': 'Strikes',
        'strike': 'Strikes',
        'strikes': 'Strikes',
        'S': 'Strikes',
        'Strike': 'Strikes',
        'Strikes': 'Strikes'
    }

    return dates, stat[category], playername+"'s "+name[category]+" (Per Game)"
