def hitter_names():
    with open("Teams/SF/2020/hitters.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('Select A Player', 'Select A Player')]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def all_hitters(team):
    with open("Teams/"+team+"/2020/hitters.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('Select A Player', 'Select A Player For '+team)]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def pitcher_names():
    with open("Teams/SF/2020/pitchers.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('Select A Player', 'Select A Player')]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def all_pitchers(team):
    with open("Teams/"+team+"/2020/pitchers.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('Select A Player', 'Select A Player')]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def h_p_categories():
    categories = ['At Bats', 'Average', 'Doubles', 'Hits', 'Home Runs', 'Left On Base', 'On Base Percentage', 'On Base Plus Slugging', 'Runs', 'Runs Batted In', 'Slugging', 'Stolen Bases', 'Strikeouts', 'Triples', 'Walks']
    data = []
    for i in range(len(categories)):
        data.append((categories[i],categories[i]))
    return data

def h_pg_categories():
    categories = ['At Bats', 'Doubles', 'Hits', 'Home Runs', 'Left On Base', 'Runs', 'Runs Batted In', 'Stolen Bases', 'Strikeouts', 'Triples', 'Walks']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_p_categories():
    categories = ['At Bats', 'Blown Saves', 'Doubles', 'ERA', 'Earned Runs', 'Hits', 'Holds', 'Home Runs', 'Innings', 'Losses', 'On Base Percentage', 'Runs', 'Strikeouts', 'Triples', 'Walks', 'Wins']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_pg_categories():
    categories = ['Earned Runs', 'Hits', 'Home Runs', 'Innings', 'Pitches', 'Runs', 'Strikeouts', 'Strikes', 'Walks']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def optional():
    data = [('','')]
    return data