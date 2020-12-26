def p(playername, category, year, team):

    with open("Teams/" + team + "/" + year + "/" + playername + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        index = content_dict[playername]['hitting']['progression']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername]['hitting']['dates']
        flyOuts = index['fly outs']
        groundOuts = index['ground outs']
        runs = index['runs']
        doubles = index['doubles']
        triples = index['triples']
        homeRuns = index['home runs']
        strikeOuts = index['strike outs']
        walks = index['walks']
        intentionalWalks = index['intentional walks']
        hits = index['hits']
        hitByPitches = index['hbp']
        average = index['avg']
        atBats = index['ab']
        onBasePercentage = index['obp']
        slugging = index['slg']
        onBasePlusSlugging = index['ops']
        caughtStealings = index['cs']
        stolenBases = index['sb']
        stolenBasePercentage = index['sbp']
        groundedIntoDoublePlays = index['gidp']
        groundedIntoTriplePlays = index['gitp']
        plateAppearances = index['pa']
        totalBases = index['total bases']
        runsBattedIn = index['rbi']
        leftOnBase = index['lob']
        sacBunts = index['sac bunts']
        sacFlies = index['sac flies']
        battingAverageOnBallsInPlay = index['babip']
        catchersInterfences = index['ci']
        pickoffs = index['pickoffs']
        atBatsPerHomeRun = index['ab per hr']

    # sanitize
    stat = {
        'Fly Outs': flyOuts,

        'Ground Outs': groundOuts,

        'Intentional Walks': intentionalWalks,

        'Hit By Pitches': hitByPitches,

        'Caught Stealings': caughtStealings,

        'Stolen Base Percentage': stolenBasePercentage,

        'Double Plays': groundedIntoDoublePlays,
        'Grounded Into Double Plays': groundedIntoDoublePlays,

        'Triple Plays': groundedIntoTriplePlays,
        'Grounded Into Triple Plays': groundedIntoTriplePlays,

        'Plate Appearances': plateAppearances,

        'Total Bases': totalBases,

        'Sacrifice Bunts': sacBunts,

        'Sacrifice Flies': sacFlies,

        'BABIP': battingAverageOnBallsInPlay,
        'Batting Average On Balls In Play': battingAverageOnBallsInPlay,

        'Catchers Interferences': catchersInterfences,

        'Pickoffs': pickoffs,

        'At Bats Per Home Run': atBatsPerHomeRun,

        'avg': average,
        'average': average,
        'averages': average,
        'Avg': average,
        'Average': average,
        'Averages': average,
        'AVG': average,

        'obp': onBasePercentage,
        'on base percentage': onBasePercentage,
        'on base percentages': onBasePercentage,
        'Obp': onBasePercentage,
        'On base percentage': onBasePercentage,
        'On base percentages': onBasePercentage,
        'On Base Percentage': onBasePercentage,
        'On Base Percentages': onBasePercentage,
        'OBP': onBasePercentage,

        'slg': slugging,
        'slugging': slugging,
        'Slugging': slugging,
        'SLG': slugging,

        'ops': onBasePlusSlugging,
        'on base plus slugging': onBasePlusSlugging,
        'On base plus slugging': onBasePlusSlugging,
        'On Base Plus Slugging': onBasePlusSlugging,
        'OPS': onBasePlusSlugging,

        'r': runs,
        'run': runs,
        'runs': runs,
        'Run': runs,
        'Runs': runs,
        'R': runs,

        'double': doubles,
        'doubles': doubles,
        'Double': doubles,
        'Doubles': doubles,
        'DOUBLES': doubles,

        'triple': triples,
        'triples': triples,
        'Triple': triples,
        'Triples': triples,
        'TRIPLES': triples,

        'hr': homeRuns,
        'hrs': homeRuns,
        'homer': homeRuns,
        'homers': homeRuns,
        'homerun': homeRuns,
        'homeruns': homeRuns,
        'home run': homeRuns,
        'home runs': homeRuns,
        'Homer': homeRuns,
        'Homers': homeRuns,
        'Home runs': homeRuns,
        'Home run': homeRuns,
        'Home Run': homeRuns,
        'Home Runs': homeRuns,

        'k': strikeOuts,
        'strikeouts': strikeOuts,
        'Strikeouts': strikeOuts,
        'K': strikeOuts,

        'bb': walks,
        'base on ball': walks,
        'base on balls': walks,
        'walks': walks,
        'Base on ball': walks,
        'Base on balls': walks,
        'Base On Balls': walks,
        'Walks': walks,
        'BB': walks,

        'h': hits,
        'hit': hits,
        'hits': hits,
        'Hit': hits,
        'Hits': hits,
        'H': hits,

        'ab': atBats,
        'at bats': atBats,
        'At bats': atBats,
        'At Bats': atBats,
        'AB': atBats,

        'sb': stolenBases,
        'stolen bases': stolenBases,
        'Stolen bases': stolenBases,
        'Stolen Bases': stolenBases,
        'SB': stolenBases,

        'rbi': runsBattedIn,
        'run batted in': runsBattedIn,
        'runs batted in': runsBattedIn,
        'Rbi': runsBattedIn,
        'Run batted in': runsBattedIn,
        'Runs batted in': runsBattedIn,
        'Run Batted In': runsBattedIn,
        'Runs Batted In': runsBattedIn,
        'RBI': runsBattedIn,

        'lob': leftOnBase,
        'left on base': leftOnBase,
        'Left on base': leftOnBase,
        'Left On Base': leftOnBase,
        'LOB': leftOnBase,

        '': None,
        'Optional': None
    }

    name = {
        'Fly Outs': 'Fly Outs',

        'Ground Outs': 'Ground Outs',

        'Intentional Walks': 'Intentional Walks',

        'Hit By Pitches': 'Hit By Pitches',

        'Caught Stealings': 'Caught Stealings',

        'Stolen Base Percentage': 'Stolen Bases',

        'Double Plays': 'Grounded Into Double Plays',
        'Grounded Into Double Plays': 'Grounded Into Double Plays',

        'Triple Plays': 'Grounded Into Triple Plays',
        'Grounded Into Triple Plays': 'Grounded Into Triple Plays',

        'Plate Appearances': 'Playe Appearances',

        'Total Bases': 'Total Bases',

        'Sacrifice Bunts': 'Sacrifice Bunts',

        'Sacrifice Flies': 'Sacrifice Flies',

        'BABIP': 'BABIP',
        'Batting Average On Balls In Play': 'Batting Average On Balls In Play',

        'Catchers Interferences': 'Catchers Interferences',

        'Pickoffs': 'Pickoffs',

        'At Bats Per Home Run': 'At Bats Per Home Run',

        'avg': 'Averages',
        'average': 'Averages',
        'averages': 'Averages',
        'Avg': 'Averages',
        'Average': 'Averages',
        'Averages': 'Averages',
        'AVG': 'Averages',

        'obp': 'On Base Percentages',
        'on base percentage': 'On Base Percentages',
        'on base percentages': 'On Base Percentages',
        'Obp': 'On Base Percentages',
        'On base percentage': 'On Base Percentages',
        'On base percentages': 'On Base Percentages',
        'On Base Percentage': 'On Base Percentages',
        'On Base Percentages': 'On Base Percentages',
        'OBP': 'On Base Percentages',

        'slg': 'Slugging Percentage',
        'slugging': 'Slugging Percentage',
        'Slugging': 'Slugging Percentage',
        'SLG': 'Slugging Percentage',

        'ops': 'On Base Plus Slugging Percentage',
        'on base plus slugging': 'On Base Plus Slugging Percentage',
        'On base plus slugging': 'On Base Plus Slugging Percentage',
        'On Base Plus Slugging': 'On Base Plus Slugging Percentage',
        'OPS': 'On Base Plus Slugging Percentage',

        'r': 'Runs',
        'run': 'Runs',
        'runs': 'Runs',
        'Run': 'Runs',
        'Runs': 'Runs',
        'R': 'Runs',

        'double': 'Doubles',
        'doubles': 'Doubles',
        'Double': 'Doubles',
        'Doubles': 'Doubles',
        'DOUBLES': 'Doubles',

        'triple': 'Triples',
        'triples': 'Triples',
        'Triple': 'Triples',
        'Triples': 'Triples',
        'TRIPLES': 'Triples',

        'hr': 'Home Runs',
        'hrs': 'Home Runs',
        'homer': 'Home Runs',
        'homers': 'Home Runs',
        'homerun': 'Home Runs',
        'homeruns': 'Home Runs',
        'home run': 'Home Runs',
        'home runs': 'Home Runs',
        'Homer': 'Home Runs',
        'Homers': 'Home Runs',
        'Home runs': 'Home Runs',
        'Home run': 'Home Runs',
        'Home Run': 'Home Runs',
        'Home Runs': 'Home Runs',

        'k': 'Strikeouts',
        'strikeouts': 'Strikeouts',
        'Strikeouts': 'Strikeouts',
        'K': 'Strikeouts',

        'bb': 'Walks',
        'base on ball': 'Walks',
        'base on balls': 'Walks',
        'walks': 'Walks',
        'Base on ball': 'Walks',
        'Base on balls': 'Walks',
        'Base On Balls': 'Walks',
        'Walks': 'Walks',
        'BB': 'Walks',

        'h': 'Hits',
        'hit': 'Hit',
        'hits': 'Hits',
        'Hit': 'Hits',
        'Hits': 'Hits',
        'H': 'Hits',

        'ab': 'At Bats',
        'at bats': 'At Bats',
        'At bats': 'At Bats',
        'At Bats': 'At Bats',
        'AB': 'At Bats',

        'sb': 'Stolen Bases',
        'stolen bases': 'Stolen Bases',
        'Stolen bases': 'Stolen Bases',
        'Stolen Bases': 'Stolen Bases',
        'SB': 'Stolen Bases',

        'rbi': 'Runs Batted In',
        'run batted in': 'Runs Batted In',
        'runs batted in': 'Runs Batted In',
        'Rbi': 'Runs Batted In',
        'Run batted in': 'Runs Batted In',
        'Runs batted in': 'Runs Batted In',
        'Run Batted In': 'Runs Batted In',
        'Runs Batted In': 'Runs Batted In',
        'RBI': 'Runs Batted In',

        'lob': 'Left On Base',
        'left on base': 'Left On Base',
        'Left on base': 'Left On Base',
        'Left On Base': 'Left On Base',
        "LOB": 'Left On Base',

        '': None,
        'Optional': None
    }

    return dates, stat[category], playername + "'s " + name[category] + " (Progressive)"


def pg(playername, category, year, team):

    with open("Teams/" + team + "/" + year + "/" + playername + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        index = content_dict[playername]['hitting']['per_game']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername]['hitting']['dates']
        flyOuts = index['fly outs']
        groundOuts = index['ground outs']
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
        groundedIntoDoublePlays = index['gidp']
        groundedIntoTriplePlays = index['gitp']
        plateAppearances = index['pa']
        totalBases = index['total bases']
        runsBattedIn = index['rbi']
        leftOnBase = index['lob']
        sacBunts = index['sac bunts']
        sacFlies = index['sac flies']
        catchersInterfences = index['ci']
        pickoffs = index['pickoffs']

    stat = {

        'Fly Outs': flyOuts,

        'Ground Outs': groundOuts,

        'Intentional Walks': intentionalWalks,

        'Hit By Pitches': hitByPitches,

        'Caught Stealings': caughtStealings,

        'Stolen Base Percentage': stolenBasePercentage,

        'Double Plays': groundedIntoDoublePlays,
        'Grounded Into Double Plays': groundedIntoDoublePlays,

        'Triple Plays': groundedIntoTriplePlays,
        'Grounded Into Triple Plays': groundedIntoTriplePlays,

        'Plate Appearances': plateAppearances,

        'Total Bases': totalBases,

        'Sacrifice Bunts': sacBunts,

        'Sacrifice Flies': sacFlies,

        'Catchers Interferences': catchersInterfences,

        'Pickoffs': pickoffs,

        'r': runs,
        'run': runs,
        'runs': runs,
        'Run': runs,
        'Runs': runs,
        'R': runs,

        'double': doubles,
        'doubles': doubles,
        'Double': doubles,
        'Doubles': doubles,
        'DOUBLES': doubles,

        'triple': triples,
        'triples': triples,
        'Triple': triples,
        'Triples': triples,
        'TRIPLES': triples,

        'hr': homeRuns,
        'hrs': homeRuns,
        'homer': homeRuns,
        'homers': homeRuns,
        'homerun': homeRuns,
        'homeruns': homeRuns,
        'home run': homeRuns,
        'home runs': homeRuns,
        'Homer': homeRuns,
        'Homers': homeRuns,
        'Home runs': homeRuns,
        'Home run': homeRuns,
        'Home Run': homeRuns,
        'Home Runs': homeRuns,

        'k': strikeOuts,
        'strikeouts': strikeOuts,
        'Strikeouts': strikeOuts,
        'K': strikeOuts,

        'bb': walks,
        'base on ball': walks,
        'base on balls': walks,
        'walks': walks,
        'Base on ball': walks,
        'Base on balls': walks,
        'Base On Balls': walks,
        'Walks': walks,
        'BB': walks,

        'h': hits,
        'hit': hits,
        'hits': hits,
        'Hit': hits,
        'Hits': hits,
        'H': hits,

        'ab': atBats,
        'at bats': atBats,
        'At bats': atBats,
        'At Bats': atBats,
        'AB': atBats,

        'sb': stolenBases,
        'stolen bases': stolenBases,
        'Stolen bases': stolenBases,
        'Stolen Bases': stolenBases,
        'SB': stolenBases,

        'rbi': runsBattedIn,
        'run batted in': runsBattedIn,
        'runs batted in': runsBattedIn,
        'Rbi': runsBattedIn,
        'Run batted in': runsBattedIn,
        'Runs batted in': runsBattedIn,
        'Run Batted In': runsBattedIn,
        'Runs Batted In': runsBattedIn,
        'RBI': runsBattedIn,

        'lob': leftOnBase,
        'left on base': leftOnBase,
        'Left on base': leftOnBase,
        'Left On Base': leftOnBase,
        "LOB": leftOnBase,

        '': None,
        'Optional': None
    }

    name = {
        'Fly Outs': 'Fly Outs',

        'Ground Outs': 'Ground Outs',

        'Intentional Walks': 'Intentional Walks',

        'Hit By Pitches': 'Hit By Pitches',

        'Caught Stealings': 'Caught Stealings',

        'Stolen Base Percentage': 'Stolen Bases',

        'Double Plays': 'Ground Into Double Plays',
        'Grounded Into Double Plays': 'Grounded Into Double Plays',

        'Triple Plays': 'Ground into Triple Plays',
        'Grounded Into Triple Plays': 'Grounded Into Double Plays',

        'Plate Appearances': 'Playe Appearances',

        'Total Bases': 'Total Bases',

        'Sacrifice Bunts': 'Sacrifice Bunts',

        'Sacrifice Flies': 'Sacrifice Flies',

        'Catchers Interferences': 'Catchers Interferences',

        'Pickoffs': 'Pickoffs',

        'avg': 'Averages',
        'average': 'Averages',
        'averages': 'Averages',
        'Avg': 'Averages',
        'Average': 'Averages',
        'Averages': 'Averages',
        'AVG': 'Averages',

        'obp': 'On Base Percentages',
        'on base percentage': 'On Base Percentages',
        'on base percentages': 'On Base Percentages',
        'Obp': 'On Base Percentages',
        'On base percentage': 'On Base Percentages',
        'On base percentages': 'On Base Percentages',
        'On Base Percentage': 'On Base Percentages',
        'On Base Percentages': 'On Base Percentages',
        'OBP': 'On Base Percentages',

        'slg': 'Slugging Percentage',
        'slugging': 'Slugging Percentage',
        'Slugging': 'Slugging Percentage',
        'SLG': 'Slugging Percentage',

        'ops': 'On Base Plus Slugging Percentage',
        'on base plus slugging': 'On Base Plus Slugging Percentage',
        'On base plus slugging': 'On Base Plus Slugging Percentage',
        'OPS': 'On Base Plus Slugging Percentage',

        'r': 'Runs',
        'run': 'Runs',
        'runs': 'Runs',
        'Run': 'Runs',
        'Runs': 'Runs',
        'R': 'Runs',

        'double': 'Doubles',
        'doubles': 'Doubles',
        'Double': 'Doubles',
        'Doubles': 'Doubles',
        'DOUBLES': 'Doubles',

        'triple': 'Triples',
        'triples': 'Triples',
        'Triple': 'Triples',
        'Triples': 'Triples',
        'TRIPLES': 'Triples',

        'hr': 'Home Runs',
        'hrs': 'Home Runs',
        'homer': 'Home Runs',
        'homers': 'Home Runs',
        'homerun': 'Home Runs',
        'homeruns': 'Home Runs',
        'home run': 'Home Runs',
        'home runs': 'Home Runs',
        'Homer': 'Home Runs',
        'Homers': 'Home Runs',
        'Home runs': 'Home Runs',
        'Home run': 'Home Runs',
        'Home Run': 'Home Runs',
        'Home Runs': 'Home Runs',

        'k': 'Strikeouts',
        'strikeouts': 'Strikeouts',
        'Strikeouts': 'Strikeouts',
        'K': 'Strikeouts',

        'bb': 'Walks',
        'base on ball': 'Walks',
        'base on balls': 'Walks',
        'walks': 'Walks',
        'Base on ball': 'Walks',
        'Base on balls': 'Walks',
        'Base On Balls': 'Walks',
        'Walks': 'Walks',
        'BB': 'Walks',

        'h': 'Hits',
        'hit': 'Hits',
        'hits': 'Hits',
        'Hit': 'Hits',
        'Hits': 'Hits',
        'H': 'Hits',

        'ab': 'At Bats',
        'at bats': 'At Bats',
        'At bats': 'At Bats',
        'At Bats': 'At Bats',
        'AB': 'At Bats',

        'sb': 'Stolen Bases',
        'stolen bases': 'Stolen Bases',
        'Stolen bases': 'Stolen Bases',
        'Stolen Bases': 'Stolen Bases',
        'SB': 'Stolen Bases',

        'rbi': 'Runs Batted In',
        'run batted in': 'Runs Batted In',
        'runs batted in': 'Runs Batted In',
        'Rbi': 'Runs Batted In',
        'Run batted in': 'Runs Batted In',
        'Runs batted in': 'Runs Batted In',
        'Run Batted In': 'Runs Batted In',
        'Runs Batted In': 'Runs Batted In',
        'RBI': 'Runs Batted In',

        'lob': 'Left On Base',
        'left on base': 'Left On Base',
        'Left on base': 'Left On Base',
        'Left On Base': 'Left On Base',
        "LOB": 'Left On Base',

        '': None,
        'Optional': None
    }

    return dates, stat[category], playername + "'s " + name[category] + " (Per Game)"

def getID(playername, year, team):

    with open("Teams/" + team + "/" + year + "/" + playername + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        front, ID = content_dict[playername]['ID'].split("ID")
    return ID
