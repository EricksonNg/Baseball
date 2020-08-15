def p2019(playername, category, year):

  with open(year+"/"+playername+".txt", "r") as FILE:
    content = FILE.read()
    content_dict = eval( content )
    index = content_dict[playername][year]['hitting']['progression']
    ID = content_dict[playername]["ID"]
    dates=content_dict[playername][year]['hitting']['dates']
    avg=index['averages']
    obp=index['obp']
    slg=index['slg']
    ops=index['ops']
    r=index['runs']
    double=index['doubles']
    triple=index['triples']
    hr=index['homeruns']
    k=index['strikeouts']
    bb=index['walks']
    h=index['hits']
    ab=index['ab']
    sb=index['sb']
    rbi=index['rbi']
    lob=index['lob']

  #sanitize
  stat={
    'avg':avg,
    'average':avg,
    'averages':avg,
    'Avg':avg,
    'Average':avg,
    'Averages':avg,
    'AVG':avg,

    'obp':obp,
    'on base percentage':obp,
    'on base percentages':obp,
    'Obp':obp,
    'On base percentage':obp,
    'On base percentages':obp,
    'On Base Percentage':obp,
    'On Base Percentages':obp,
    'OBP':obp,

    'slg':slg,
    'slugging':slg,
    'Slugging':slg,
    'SLG':slg,

    'ops':ops,
    'on base plus slugging':ops,
    'On base plus slugging':ops,
    'On Base Plus Slugging':ops,
    'OPS':ops,

    'r':r,
    'run':r,
    'runs':r,
    'Run':r,
    'Runs':r,
    'R':r,

    'double':double,
    'doubles':double,
    'Double':double,
    'Doubles':double,
    'DOUBLES':double,

    'triple':triple,
    'triples':triple,
    'Triple':triple,
    'Triples':triple,
    'TRIPLES':triple,

    'hr':hr,
    'hrs':hr,
    'homer':hr,
    'homers':hr,
    'homerun':hr,
    'homeruns':hr,
    'home run':hr,
    'home runs':hr,
    'Homer':hr,
    'Homers':hr,
    'Home runs':hr,
    'Home run':hr,
    'Home Run':hr,
    'Home Runs': hr,

    'k':k,
    'strikeouts':k,
    'Strikeouts':k,
    'K':k,

    'bb':bb,
    'base on ball':bb,
    'base on balls':bb,
    'walks':bb,
    'Base on ball':bb,
    'Base on balls':bb,
    'Base On Balls':bb,
    'Walks':bb,
    'BB':bb,

    'h':h,
    'hit':h,
    'hits':h,
    'Hit':h,
    'Hits':h,
    'H':h,

    'ab':ab,
    'at bats':ab,
    'At bats':ab,
    'At Bats':ab,
    'AB':ab,

    'sb':sb,
    'stolen bases':sb,
    'Stolen bases':sb,
    'Stolen Bases':sb,
    'SB':sb,

    'rbi':rbi,
    'run batted in':rbi,
    'runs batted in':rbi,
    'Rbi':rbi,
    'Run batted in':rbi,
    'Runs batted in':rbi,
    'Run Batted In':rbi,
    'Runs Batted In':rbi,
    'RBI':rbi,

    'lob':lob,
    'left on base':lob,
    'Left on base':lob,
    'Left On Base':lob,
    "LOB":lob
    }

  name={
    'avg':'Averages',
    'average':'Averages',
    'averages':'Averages',
    'Avg':'Averages',
    'Average':'Averages',
    'Averages':'Averages',
    'AVG':'Averages',

    'obp':'On Base Percentages',
    'on base percentage':'On Base Percentages',
    'on base percentages':'On Base Percentages',
    'Obp':'On Base Percentages',
    'On base percentage':'On Base Percentages',
    'On base percentages':'On Base Percentages',
    'On Base Percentage':'On Base Percentages',
    'On Base Percentages':'On Base Percentages',
    'OBP':'On Base Percentages',

    'slg':'Slugging Percentage',
    'slugging':'Slugging Percentage',
    'Slugging':'Slugging Percentage',
    'SLG':'Slugging Percentage',

    'ops':'On Base Plus Slugging Percentage',
    'on base plus slugging':'On Base Plus Slugging Percentage',
    'On base plus slugging':'On Base Plus Slugging Percentage',
    'On Base Plus Slugging': 'On Base Plus Slugging Percentage',
    'OPS':'On Base Plus Slugging Percentage',

    'r':'Runs',
    'run':'Runs',
    'runs':'Runs',
    'Run':'Runs',
    'Runs':'Runs',
    'R':'Runs',

    'double':'Doubles',
    'doubles':'Doubles',
    'Double':'Doubles',
    'Doubles':'Doubles',
    'DOUBLES':'Doubles',

    'triple':'Triples',
    'triples':'Triples',
    'Triple':'Triples',
    'Triples':'Triples',
    'TRIPLES':'Triples',

    'hr':'Home Runs',
    'hrs':'Home Runs',
    'homer':'Home Runs',
    'homers':'Home Runs',
    'homerun':'Home Runs',
    'homeruns':'Home Runs',
    'home run':'Home Runs',
    'home runs':'Home Runs',
    'Homer':'Home Runs',
    'Homers':'Home Runs',
    'Home runs':'Home Runs',
    'Home run':'Home Runs',
    'Home Run':'Home Runs',
    'Home Runs':'Home Runs',

    'k':'Strikeouts',
    'strikeouts':'Strikeouts',
    'Strikeouts':'Strikeouts',
    'K':'Strikeouts',

    'bb':'Walks',
    'base on ball':'Walks',
    'base on balls':'Walks',
    'walks':'Walks',
    'Base on ball':'Walks',
    'Base on balls':'Walks',
    'Base On Balls':'Walks',
    'Walks':'Walks',
    'BB':'Walks',

    'h':'Hits',
    'hit':'Hit',
    'hits':'Hits',
    'Hit':'Hits',
    'Hits':'Hits',
    'H':'Hits',

    'ab':'At Bats',
    'at bats':'At Bats',
    'At bats':'At Bats',
    'At Bats':'At Bats',
    'AB':'At Bats',

    'sb':'Stolen Bases',
    'stolen bases':'Stolen Bases',
    'Stolen bases':'Stolen Bases',
    'Stolen Bases':'Stolen Bases',
    'SB':'Stolen Bases',

    'rbi':'Runs Batted In',
    'run batted in':'Runs Batted In',
    'runs batted in':'Runs Batted In',
    'Rbi':'Runs Batted In',
    'Run batted in':'Runs Batted In',
    'Runs batted in':'Runs Batted In',
    'Run Batted In':'Runs Batted In',
    'Runs Batted In':'Runs Batted In',
    'RBI':'Runs Batted In',

    'lob':'Left On Base',
    'left on base':'Left On Base',
    'Left on base':'Left On Base',
    'Left On Base':'Left On Base',
    "LOB":'Left On Base'
    }
  
  return dates, stat[category], name[category]

def pg2019(playername,category, year):
  
  with open(str(year)+"/"+playername+".txt", "r") as FILE:
    content = FILE.read()
    content_dict = eval( content )
    index = content_dict[playername][year]['hitting']['per_game']
    ID = content_dict[playername]["ID"]
    dates=content_dict[playername][year]['hitting']['dates']
    ab=index['ab']
    k=index['strikeouts']
    h=index['hits']
    bb=index['walks']
    r=index['runs']
    rbi=index['rbi']
    sb=index['sb']
    lob=index['lob']
    double=index['doubles']
    triple=index['triples']
    hr=index['homeruns']

  stat={

    'r':r,
    'run':r,
    'runs':r,
    'Run':r,
    'Runs':r,
    'R':r,

    'double':double,
    'doubles':double,
    'Double':double,
    'Doubles':double,
    'DOUBLES':double,

    'triple':triple,
    'triples':triple,
    'Triple':triple,
    'Triples':triple,
    'TRIPLES':triple,

    'hr':hr,
    'hrs':hr,
    'homer':hr,
    'homers':hr,
    'homerun':hr,
    'homeruns':hr,
    'home run':hr,
    'home runs':hr,
    'Homer':hr,
    'Homers':hr,
    'Home runs':hr,
    'Home run':hr,
    'Home Run':hr,
    'Home Runs': hr,

    'k':k,
    'strikeouts':k,
    'Strikeouts':k,
    'K':k,

    'bb':bb,
    'base on ball':bb,
    'base on balls':bb,
    'walks':bb,
    'Base on ball':bb,
    'Base on balls':bb,
    'Base On Balls':bb,
    'Walks':bb,
    'BB':bb,

    'h':h,
    'hit':h,
    'hits':h,
    'Hit':h,
    'Hits':h,
    'H':h,

    'ab':ab,
    'at bats':ab,
    'At bats':ab,
    'At Bats':ab,
    'AB':ab,

    'sb':sb,
    'stolen bases':sb,
    'Stolen bases':sb,
    'Stolen Bases':sb,
    'SB':sb,

    'rbi':rbi,
    'run batted in':rbi,
    'runs batted in':rbi,
    'Rbi':rbi,
    'Run batted in':rbi,
    'Runs batted in':rbi,
    'Run Batted In':rbi,
    'Runs Batted In':rbi,
    'RBI':rbi,

    'lob':lob,
    'left on base':lob,
    'Left on base':lob,
    'Left On Base':lob,
    "LOB":lob
    }

  name={
    'avg':'Averages',
    'average':'Averages',
    'averages':'Averages',
    'Avg':'Averages',
    'Average':'Averages',
    'Averages':'Averages',
    'AVG':'Averages',

    'obp':'On Base Percentages',
    'on base percentage':'On Base Percentages',
    'on base percentages':'On Base Percentages',
    'Obp':'On Base Percentages',
    'On base percentage':'On Base Percentages',
    'On base percentages':'On Base Percentages',
    'On Base Percentage':'On Base Percentages',
    'On Base Percentages':'On Base Percentages',
    'OBP':'On Base Percentages',

    'slg':'Slugging Percentage',
    'slugging':'Slugging Percentage',
    'Slugging':'Slugging Percentage',
    'SLG':'Slugging Percentage',

    'ops':'On Base Plus Slugging Percentage',
    'on base plus slugging':'On Base Plus Slugging Percentage',
    'On base plus slugging':'On Base Plus Slugging Percentage',
    'OPS':'On Base Plus Slugging Percentage',

    'r':'Runs',
    'run':'Runs',
    'runs':'Runs',
    'Run':'Runs',
    'Runs':'Runs',
    'R':'Runs',

    'double':'Doubles',
    'doubles':'Doubles',
    'Double':'Doubles',
    'Doubles':'Doubles',
    'DOUBLES':'Doubles',

    'triple':'Triples',
    'triples':'Triples',
    'Triple':'Triples',
    'Triples':'Triples',
    'TRIPLES':'Triples',

    'hr':'Home Runs',
    'hrs':'Home Runs',
    'homer':'Home Runs',
    'homers':'Home Runs',
    'homerun':'Home Runs',
    'homeruns':'Home Runs',
    'home run':'Home Runs',
    'home runs':'Home Runs',
    'Homer':'Home Runs',
    'Homers':'Home Runs',
    'Home runs':'Home Runs',
    'Home run':'Home Runs',
    'Home Run':'Home Runs',
    'Home Runs':'Home Runs',

    'k':'Strikeouts',
    'strikeouts':'Strikeouts',
    'Strikeouts':'Strikeouts',
    'K':'Strikeouts',

    'bb':'Walks',
    'base on ball':'Walks',
    'base on balls':'Walks',
    'walks':'Walks',
    'Base on ball':'Walks',
    'Base on balls':'Walks',
    'Base On Balls':'Walks',
    'Walks':'Walks',
    'BB':'Walks',

    'h':'Hits',
    'hit':'Hits',
    'hits':'Hits',
    'Hit':'Hits',
    'Hits':'Hits',
    'H':'Hits',

    'ab':'At Bats',
    'at bats':'At Bats',
    'At bats':'At Bats',
    'At Bats':'At Bats',
    'AB':'At Bats',

    'sb':'Stolen Bases',
    'stolen bases':'Stolen Bases',
    'Stolen bases':'Stolen Bases',
    'Stolen Bases':'Stolen Bases',
    'SB':'Stolen Bases',

    'rbi':'Runs Batted In',
    'run batted in':'Runs Batted In',
    'runs batted in':'Runs Batted In',
    'Rbi':'Runs Batted In',
    'Run batted in':'Runs Batted In',
    'Runs batted in':'Runs Batted In',
    'Run Batted In':'Runs Batted In',
    'Runs Batted In':'Runs Batted In',
    'RBI':'Runs Batted In',

    'lob':'Left On Base',
    'left on base':'Left On Base',
    'Left on base':'Left On Base',
    'Left On Base':'Left On Base',
    "LOB":'Left On Base'
    }
  
  return dates, stat[category], name[category]