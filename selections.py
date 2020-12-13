def hitter_names():
    with open("Teams/SF/2020/hitters.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('Select A Player', 'Select A Player')]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def all_hitters(team, year):
    with open("Teams/"+team+"/"+year+"/hitters.txt", "r") as FILE:
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

def all_pitchers(team,year):
    with open("Teams/"+team+"/"+year+"/pitchers.txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
    players = content_dict['players']
    data = [('Select A Player', 'Select A Player For '+team)]
    for i in range(len(players)):
        data.append((players[i], players[i]))
    return data

def h_p_categories():
    categories = ['At Bats', 'At Bats Per Home Run', 'Average', 'BABIP', 'Catchers Interferences', 'Caught Stealings', 'Doubles', 'Fly Outs', 'Ground Outs', 'Double Plays', 'Triple Plays', 'Hit By Pitches', 'Hits', 'Home Runs', 'Intentional Walks', 'Left On Base', 'On Base Percentage', 'On Base Plus Slugging', 'Pickoffs', 'Plate Appearances', 'Runs', 'Runs Batted In', 'Sacrifice Bunts', 'Sacrifice Flies', 'Slugging', 'Stolen Base Percentage', 'Stolen Bases', 'Strikeouts', 'Total Bases', 'Triples', 'Walks']
    data = []
    for i in range(len(categories)):
        data.append((categories[i],categories[i]))
    return data

def h_pg_categories():
    categories = ['At Bats', 'Catchers Interferences', 'Caught Stealings', 'Doubles', 'Fly Outs', 'Ground Outs', 'Double Plays', 'Triple Plays', 'Hit By Pitches', 'Hits', 'Home Runs', 'Intentional Walks', 'Left On Base', 'On Base Percentage', 'On Base Plus Slugging', 'Pickoffs', 'Plate Appearances', 'Runs', 'Runs Batted In', 'Sacrifice Bunts', 'Sacrifice Flies', 'Slugging', 'Stolen Base Percentage', 'Stolen Bases', 'Strikeouts', 'Total Bases', 'Triples', 'Walks']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_p_categories():
    categories = ['Air Outs', 'At Bats', 'Balks', 'Balls', 'Batters Faced', 'Blown Saves', 'Catchers Interferences', 'Caught Stealings', 'Complete Games', 'Doubles', 'ERA', 'Earned Runs', 'Games', 'Games Finished', 'Games Started', 'Ground Outs', 'Ground to Air', 'Hit By Pitches', 'Hits', 'Hits Per 9', 'Holds', 'Home Runs', 'Home Runs Per 9', 'Inherited Runners Scored', 'Innings', 'Intentional Walks', 'Losses', 'On Base Percentage', 'Outs', 'Pickoffs', 'Pitches', 'Pitches Per Inning', 'Runs', 'Runs Batted In', 'Runs Per 9', 'Sacrifice Bunts', 'Sacrifice Flies', 'Save Opportunities', 'Saves', 'Shut Outs', 'Stolen Base Percentage', 'Stolen Bases', 'Strike Percentage', 'Strikeout To Walk', 'Strikeouts', 'Strikeouts Per 9', 'Strikes', 'Triples', 'WHIP', 'Walks', 'Walks Per 9', 'Wild Pitches', 'Win Percentage', 'Wins']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_pg_categories():
    categories = ['Air Outs', 'At Bats', 'Balks', 'Balls', 'Batters Faced', 'Blown Saves', 'Catchers Interferences', 'Caught Stealings', 'Complete Games', 'Doubles', 'ERA', 'Earned Runs', 'Games', 'Games Finished', 'Games Started', 'Ground Outs', 'Ground to Air', 'Hit By Pitches', 'Hits', 'Hits Per 9', 'Holds', 'Home Runs', 'Home Runs Per 9', 'Inherited Runners Scored', 'Innings', 'Intentional Walks', 'Losses', 'On Base Percentage', 'Outs', 'Pickoffs', 'Pitches', 'Pitches Per Inning', 'Runs', 'Runs Batted In', 'Runs Per 9', 'Sacrifice Bunts', 'Sacrifice Flies', 'Save Opportunities', 'Saves', 'Shut Outs', 'Stolen Base Percentage', 'Stolen Bases', 'Strike Percentage', 'Strikeout To Walk', 'Strikeouts', 'Strikeouts Per 9', 'Strikes', 'Triples', 'WHIP', 'Walks', 'Walks Per 9', 'Wild Pitches', 'Win Percentage', 'Wins']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data


def optional():
    data = [('','')]
    return data