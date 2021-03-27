def p(playername, category, year, team):

    with open("Teams/" + team + "/" + year + "/" + playername + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)

        index = content_dict[playername]['fielding']['progression']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername]['fielding']['dates']

    assists = index['assists']
    putOuts = index['put outs']
    errors = index['errors']
    chances = index['chances']
    fieldingPercentage = index['fielding percentage']
    caughtStealings = index['cs']
    passedBalls = index['passed balls']
    gamesStarted = index['gs']
    stolenBases = index['sb']
    stolenBasePercentage = index['sbp']
    pickoffs = index['pickoffs']

    sanitize = {'Assists': assists, 'Put Outs': putOuts, 'Errors': errors, 'Chances': chances, 'Fielding Percentage': fieldingPercentage, 'Caught Stealings': caughtStealings, 'Passed Balls': passedBalls, 'Games Started': gamesStarted, 'Stolen Bases': stolenBases, 'Stolen Base Percentage': stolenBasePercentage, 'Pickoffs': pickoffs}

    return dates, sanitize[category], playername + "'s " + category + " (Progressive)"

def pg(playername, category, year, team):

    with open("Teams/" + team + "/" + year + "/" + playername + ".txt", "r") as FILE:
        try:
            content = FILE.read()
            content_dict = eval(content)
        except Exception as e:
            input(e)
        index = content_dict[playername]['fielding']['per_game']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername]['fielding']['dates']

    assists = index['assists']
    putOuts = index['put outs']
    errors = index['errors']
    chances = index['chances']
    caughtStealings = index['cs']
    passedBalls = index['passed balls']
    gamesStarted = index['gs']
    stolenBases = index['sb']
    stolenBasePercentage = index['sbp']
    pickoffs = index['pickoffs']

    sanitize = {'Assists': assists, 'Put Outs': putOuts, 'Errors': errors, 'Chances': chances, 'Caught Stealings': caughtStealings, 'Passed Balls': passedBalls, 'Games Started': gamesStarted, 'Stolen Bases': stolenBases, 'Stolen Base Percentage': stolenBasePercentage, 'Pickoffs': pickoffs}

    return dates, sanitize[category], playername + "'s " + category + " (Per Game)"
