def p2019(playername, category, year):
    with open(year+"/" + playername + ".txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
        index = content_dict[playername][year]['pitching']['progression']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername][year]['pitching']['dates']
        era = index['era']
        ip = index['innings']
        h = index['hits']
        r = index['runs']
        er = index['earned_runs']
        bb = index['walks']
        k = index['strikeouts']
        hr = index['homeruns']
        double = index['doubles']
        triple = index['triples']
        ab = index['ab']
        obp = index['obp']
        win = index['wins']
        loss = index['losses']
        hold = index['holds']
        blown_save = index['blown_saves']

    # sanitize
    stat = {
        'era': era,
        'Era': era,
        'ERA': era,

        'ip': ip,
        'innings': ip,
        'IP': ip,
        'Innings': ip,

        'h': h,
        'hits': h,
        'H': h,
        'Hits': h,

        'r': r,
        'run': r,
        'runs': r,
        'R': r,
        'Run': r,
        'Runs': r,

        'er': er,
        'earned run': er,
        'earned runs': er,
        'Er': er,
        'ER': er,
        'Earned run': er,
        'Earned runs': er,
        'Earned Runs': er,

        'bb': bb,
        'base on ball': bb,
        'base on balls': bb,
        'walk': bb,
        'walks': bb,
        'Bb': bb,
        'BB': bb,
        'Base on ball': bb,
        'Base on balls': bb,
        'Walk': bb,
        'Walks': bb,

        'k': k,
        'strikeout': k,
        'strikeouts': k,
        'K': k,
        'Strikeout': k,
        'Strikeouts': k,

        'hr': hr,
        'homerun': hr,
        'home run': hr,
        'homeruns': hr,
        'home runs': hr,
        'Hr': hr,
        'Homerun': hr,
        'Homeruns': hr,
        'Home run': hr,
        'Home runs': hr,
        'Home Run': hr,
        'Home Runs': hr,
        'HR': hr,

        'double': double,
        'doubles': double,
        'Double': double,
        'Doubles': double,

        'triple': triple,
        'triples': triple,
        'Triple': triple,
        'Triples': triple,

        'ab': ab,
        'at bat': ab,
        'at bats': ab,
        'At bat': ab,
        'At bats': ab,
        'At Bat': ab,
        'At Bats': ab,
        'AB': ab,

        'obp': obp,
        'on base percentage': obp,
        'on base percentages': obp,
        'Obp': obp,
        'On base percentage': obp,
        'On base percentages': obp,
        'On Base Percentage': obp,
        'On Base Percentages': obp,
        'OBP': obp,

        'win': win,
        'wins': win,
        'w': win,
        'Win': win,
        'Wins': win,
        'W': win,

        'loss': loss,
        'losses': loss,
        'l': loss,
        'Loss': loss,
        'Losses': loss,
        'L': loss,

        'hold': hold,
        'holds': hold,
        'Hold': hold,
        'Holds': hold,

        'blown save': blown_save,
        'blown saves': blown_save,
        'Blown save': blown_save,
        'Blown saves': blown_save,
        'Blown Save': blown_save,
        'Blown Saves': blown_save
    }

    name = {
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

    return dates, stat[category], name[category]


def pg2019(playername, category, year):
    with open(year+"/" + playername + ".txt", "r") as FILE:
        content = FILE.read()
        content_dict = eval(content)
        index = content_dict[playername][year]['pitching']['per_game']
        ID = content_dict[playername]["ID"]
        dates = content_dict[playername][year]['pitching']['dates']
        ip = index['innings']
        h = index['hits']
        r = index['runs']
        er = index['earned_runs']
        bb = index['walks']
        k = index['strikeouts']
        hr = index['homeruns']
        p = index['pitches']
        s = index['strikes']

    stat = {
        'ip': ip,
        'innings': ip,
        'IP': ip,
        'Innings': ip,

        'h': h,
        'hits': h,
        'H': h,
        'Hits': h,

        'r': r,
        'run': r,
        'runs': r,
        'R': r,
        'Run': r,
        'Runs': r,

        'er': er,
        'earned run': er,
        'earned runs': er,
        'Er': er,
        'ER': er,
        'Earned run': er,
        'Earned runs': er,
        'Earned Run': er,
        'Earned Runs': er,

        'bb': bb,
        'base on ball': bb,
        'base on balls': bb,
        'walk': bb,
        'walks': bb,
        'Bb': bb,
        'BB': bb,
        'Base on ball': bb,
        'Base on balls': bb,
        'Walk': bb,
        'Walks': bb,

        'k': k,
        'strikeout': k,
        'strikeouts': k,
        'K': k,
        'Strikeout': k,
        'Strikeouts': k,

        'hr': hr,
        'homerun': hr,
        'home run': hr,
        'homeruns': hr,
        'home runs': hr,
        'Hr': hr,
        'Homerun': hr,
        'Homeruns': hr,
        'Home run': hr,
        'Home runs': hr,
        'Home Run': hr,
        'Home Runs': hr,
        'HR': hr,

        'p': p,
        'pitch': p,
        'pitches': p,
        'P': p,
        'Pitch': p,
        'Pitches': p,

        's': s,
        'strike': s,
        'strikes': s,
        'S': s,
        'Strike': s,
        'Strikes': s
    }
    name = {
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

    return dates, stat[category], name[category]
