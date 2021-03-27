def all(team, year, playerName):
    categories = {'avg': 'Average', 'hits': 'Hits', 'obp': 'On Base Percentage', 'slg': 'Slugging', 'ops': 'On Base Plus Slugging', 'babip': 'BABIP', 'doubles': 'Doubles', 'triples': 'Triples', 'home runs': 'Home Runs', 'extra-base hits': 'Extra-Base Hits', 'iso': 'ISO', 'rbi': 'Runs Batted In', 'runs': 'Runs', 'strike outs': 'Strike Outs', 'strike out percentage': 'Strike Out Percentage', 'walks': 'Walks', 'walk percentage': 'Walk Percentage', 'hbp': 'Hit By Pitches', 'sb': 'Stolen Bases', 'cs': 'Caught Stealings', 'sbp': 'Stolen Base Percentage', 'total bases': 'Total Bases', 'lob': 'Left On Base', 'pa': 'Plate Appearances', 'ab': 'At Bats', 'ab per hr': 'At Bats Per Home Run', 'intentional walks': 'Intentional Walks', 'sac flies': 'Sacrifice Flies', 'ground outs': 'Ground Outs', 'fly outs': 'Fly Outs', 'gidp': 'Grounded Into Double Plays', 'gitp': 'Grounded Into Triple Plays', 'sac bunts': 'Sacrifice Bunts', 'pickoffs': 'Pickoffs', 'ci': 'Catcher Inteference'}
    catStats = {}

    with open("Teams/" + team + "/" + year + "/" + playerName + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        index = content_dict[playerName]['hitting']['progression']
        dates = content_dict[playerName]['hitting']['dates']
        for i in categories:
            catStats[categories[i]] = index[i]

    return catStats, dates

def allChartsPG(team, year, playerName):
    categories = {'hits': 'Hits', 'doubles': 'Doubles', 'triples': 'Triples', 'home runs': 'Home Runs', 'extra-base hits': 'Extra-Base Hits', 'rbi': 'Runs Batted In', 'runs': 'Runs', 'strike outs': 'Strike Outs', 'walks': 'Walks', 'hbp': 'Hit By Pitches', 'sb': 'Stolen Bases', 'cs': 'Caught Stealings', 'total bases': 'Total Bases', 'lob': 'Left On Base', 'pa': 'Plate Appearances', 'ab': 'At Bats', 'intentional walks': 'Intentional Walks', 'sac flies': 'Sacrifice Flies', 'ground outs': 'Ground Outs', 'fly outs': 'Fly Outs', 'gidp': 'Grounded Into Double Plays', 'gitp': 'Grounded Into Triple Plays', 'sac bunts': 'Sacrifice Bunts', 'pickoffs': 'Pickoffs', 'ci': 'Catcher Inteference'}
    catStats = {}

    with open("Teams/" + team + "/" + year + "/" + playerName + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        index = content_dict[playerName]['hitting']['per_game']
        dates = content_dict[playerName]['hitting']['dates']
        for i in categories:
            catStats[categories[i]] = index[i]

    return catStats, dates

def allpg(team, year, playerName):
    with open("Teams/" + team + "/" + year + "/" + playerName + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        perGameData = content_dict[playerName]['hitting']['per_game']
        dates = content_dict[playerName]['hitting']['dates']
        formattedDates = []
        for date in dates:
            year, month, day = date.split("-")
            if "vs" in day:
                code = "vs"
                day, otherTeam = day.split(" vs. ")
            if "@" in day:
                code = "@"
                day, otherTeam = day.split(" @ ")
            newDate = month+"-"+day+"-"+year+" "+code+" "+otherTeam
            formattedDates.append(newDate)
        dates = formattedDates
        positions = content_dict[playerName]['fielding']['positions']
    order = {'hits': 'H', 'ab': 'AB', 'pa': 'PA', 'rbi': 'RBI', 'runs': 'R', 'total bases': 'TB', 'doubles': '2B', 'triples': '3B', 'home runs': 'HR', 'extra-base hits': 'XBH', 'strike outs': 'SO', 'walks': 'BB', 'intentional walks': 'IBB', 'hbp': 'HBP', 'sb': 'SB', 'cs': 'CS', 'lob': 'LOB', 'sac bunts': 'Sac Bunts', 'sac flies': 'Sac Flies', 'ground outs': 'GO', 'fly outs': 'FO', 'gidp': 'GIDP', 'gitp': 'GITP'}

    return perGameData, dates, order, positions

def allp(team, year, playerName):
    with open("Teams/" + team + "/" + year + "/" + playerName + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        progressionData = content_dict[playerName]['hitting']['progression']
    order = {'avg': 'AVG', 'obp': 'OBP', 'slg': 'SLG', 'ops': 'OPS', 'babip': 'BABIP', 'hits': 'H', 'ab': 'AB', 'pa': 'PA', 'rbi': 'RBI', 'runs': 'R', 'total bases': 'TB', 'doubles': '2B', 'triples': '3B', 'home runs': 'HR', 'extra-base hits': 'XBH', 'iso': 'ISO', 'strike outs': 'SO', 'strike out percentage': 'SO%', 'walks': 'BB', 'walk percentage': 'BB%', 'intentional walks': 'IBB', 'hbp': 'HBP', 'sb': 'SB', 'cs': 'CS', 'sbp': 'SB%', 'lob': 'LOB', 'sac bunts': 'Sac Bunts', 'sac flies': 'Sac Flies', 'ground outs': 'GO', 'fly outs': 'FO', 'gidp': 'GIDP', 'gitp': 'GITP'}


    return progressionData, order
