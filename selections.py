def hitter_names():
    with open("2020/hitters.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('None', 'Select A Player')]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def pitcher_names():
    with open("2020/pitchers.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('None', 'Select A Player')]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def h_p_categories():
    categories = ['Average', 'On Base Percentage', 'Slugging', 'On Base Plus Slugging', 'Runs', 'Doubles', 'Triples', 'Home Runs', 'Strikeouts', 'Walks', 'Hits', 'At Bats', 'Stolen Bases', 'Runs Batted In', 'Left On Base']
    data = []
    for i in range(len(categories)):
        data.append((categories[i],categories[i]))
    return data

def h_pg_categories():
    categories = ['At Bats', 'Strikeouts', 'Hits', 'Walks', 'Runs', 'Runs Batted In', 'Stolen Bases', 'Left On Base', 'Doubles', 'Triples', 'Home Runs']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_p_categories():
    categories = ['ERA', 'Innings', 'Hits', 'Runs', 'Earned Runs', 'Walks', 'Strikeouts', 'Home Runs', 'Doubles', 'Triples', 'At Bats', 'On Base Percentage', 'Wins', 'Losses', 'Holds', 'Blown Saves']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_pg_categories():
    categories = ['Innings', 'Hits', 'Runs', 'Earned Runs', 'Walks', 'Strikeouts', 'Home Runs', 'Pitches', 'Strikes']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data