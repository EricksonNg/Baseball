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
    categoriesInAlph = ['At Bats', 'At Bats Per Home Run', 'Average', 'BABIP', 'Catchers Interferences', 'Caught Stealings', 'Doubles', 'Extra-Base Hits', 'Fly Outs', 'Ground Outs', 'Double Plays', 'Triple Plays', 'Hit By Pitches', 'Hits', 'Home Runs', 'Intentional Walks', 'ISO', 'Left On Base', 'On Base Percentage', 'On Base Plus Slugging', 'Pickoffs', 'Plate Appearances', 'Runs', 'Runs Batted In', 'Sacrifice Bunts', 'Sacrifice Flies', 'Slugging', 'Stolen Base Percentage', 'Stolen Bases', 'Strikeouts', 'Strikeout Percentage', 'Total Bases', 'Triples', 'Walk Percentage', 'Walks']
    categories = ['Average', 'Hits', 'On Base Percentage', 'Slugging', 'On Base Plus Slugging', 'BABIP', 'Doubles', 'Triples', 'Home Runs', 'Extra-Base Hits', 'ISO', 'Runs Batted In', 'Runs', 'Strikeouts', 'Strikeout Percentage', 'Walks', 'Walk Percentage', 'Hit By Pitches', 'Stolen Bases', 'Caught Stealings', 'Stolen Base Percentage', 'Total Bases', 'Left On Base', 'Plate Appearances', 'At Bats', 'At Bats Per Home Run', 'Intentional Walks', 'Sacrifice Flies', 'Ground Outs', 'Fly Outs', 'Double Plays', 'Triple Plays', 'Sacrifice Bunts', 'Pickoffs', 'Catcher Interferences']
    data = []
    for i in range(len(categories)):
        data.append((categories[i],categories[i]))
    return data

def h_pg_categories():
    categoriesInAlphSortOf = ['At Bats', 'Catchers Interferences', 'Caught Stealings', 'Doubles', 'Extra-Base Hits', 'Fly Outs', 'Ground Outs', 'Double Plays', 'Triple Plays', 'Hit By Pitches', 'Hits', 'Home Runs', 'Intentional Walks', 'Left On Base', 'On Base Percentage', 'On Base Plus Slugging', 'Pickoffs', 'Plate Appearances', 'Runs', 'Runs Batted In', 'Sacrifice Bunts', 'Sacrifice Flies', 'Slugging', 'Stolen Base Percentage', 'Stolen Bases', 'Strikeouts', 'Total Bases', 'Triples', 'Walks']
    categories = ['Hits', 'Doubles', 'Triples', 'Home Runs', 'Extra-Base Hits', 'Runs Batted In', 'Runs', 'Strikeouts', 'Walks', 'Hit By Pitches', 'Stolen Bases', 'Caught Stealings', 'Stolen Base Percentage', 'Total Bases', 'Left On Base', 'Plate Appearances', 'At Bats', 'Intentional Walks', 'Sacrifice Flies', 'Ground Outs', 'Fly Outs', 'Double Plays', 'Triple Plays', 'Sacrifice Bunts', 'Pickoffs', 'Catcher Interferences']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_p_categories():
    categories = ['Air Outs', 'At Bats', 'Balks', 'Balls', 'Batters Faced', 'Batting Average Against', 'Blown Saves', 'Catchers Interferences', 'Caught Stealings', 'Complete Games', 'Doubles', 'ERA', 'Earned Runs', 'Games', 'Games Finished', 'Games Started', 'Ground Outs', 'Ground to Air', 'Hit By Pitches', 'Hits', 'Hits Per 9', 'Holds', 'Home Runs', 'Home Runs Per 9', 'Inherited Runners Scored', 'Innings', 'Intentional Walks', 'Losses', 'On Base Percentage', 'Outs', 'Pickoffs', 'Pitches', 'Pitches Per Inning', 'Runs', 'Runs Batted In', 'Runs Per 9', 'Sacrifice Bunts', 'Sacrifice Flies', 'Save Opportunities', 'Saves', 'Shut Outs', 'Stolen Base Percentage', 'Stolen Bases', 'Strike Percentage', 'Strikeout Percentage','Strikeout To Walk', 'Strikeouts', 'Strikeouts Per 9', 'Strikes', 'Triples', 'WHIP', 'Walks', 'Walks Per 9', 'Wild Pitches', 'Win Percentage', 'Wins']
    # categories = ['Innings', 'Strikeouts', 'Strikeouts Per 9', '']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data

def p_pg_categories():
    categories = ['Air Outs', 'At Bats', 'Balks', 'Balls', 'Batters Faced', 'Blown Saves', 'Catchers Interferences', 'Caught Stealings', 'Complete Games', 'Doubles', 'Earned Runs', 'Games Finished', 'Games Started', 'Ground Outs', 'Hit By Pitches', 'Hits', 'Hits Per 9', 'Holds', 'Home Runs', 'Home Runs Per 9', 'Inherited Runners Scored', 'Innings', 'Intentional Walks', 'Losses', 'On Base Percentage', 'Outs', 'Pickoffs', 'Pitches', 'Pitches Per Inning', 'Runs', 'Runs Batted In', 'Runs Per 9', 'Sacrifice Bunts', 'Sacrifice Flies', 'Save Opportunities', 'Saves', 'Shut Outs', 'Stolen Base Percentage', 'Stolen Bases', 'Strike Percentage', 'Strikeouts', 'Strikeouts Per 9', 'Strikes', 'Triples', 'WHIP', 'Walks', 'Walks Per 9', 'Wild Pitches', 'Wins']
    data = []
    for i in range(len(categories)):
        data.append((categories[i], categories[i]))
    return data


def optional():
    data = [('','')]
    return data