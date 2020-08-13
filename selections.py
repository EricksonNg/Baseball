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
    categories = ['Select A Category','At Bats', 'Average', 'Doubles', 'Hits', 'Home Runs', 'Left On Base', 'On Base Percentage', 'On Base Plus Slugging', 'Runs', 'Runs Batted In', 'Slugging', 'Stolen Bases', 'Strikeouts', 'Triples', 'Walks']
    data = []
    for i in range(len(categories)):
        data.append((categories[i],categories[i]))
    return data

def h_pg_categories():
    categories = ['Select A Category','At Bats', 'Doubles', 'Hits', 'Home Runs', 'Left On Base', 'Runs', 'Runs Batted In', 'Stolen Bases', 'Strikeouts', 'Triples', 'Walks']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_p_categories():
    categories = ['ERA', 'Innings', 'Hits', 'Runs', 'Earned Runs', 'Walks', 'Strikeouts', 'Home Runs', 'Doubles', 'Triples', 'At Bats', 'On Base Percentage', 'Wins', 'Losses', 'Holds', 'Blown Saves']
    print(sorted(categories))
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_pg_categories():
    categories = ['Innings', 'Hits', 'Runs', 'Earned Runs', 'Walks', 'Strikeouts', 'Home Runs', 'Pitches', 'Strikes']
    print(sorted(categories))
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data