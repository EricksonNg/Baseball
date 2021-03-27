import statsapi

roster = statsapi.get('team_roster', {'teamId': 137})['roster']

players = {'Pitcher': [], 'Outfielder': [], 'Infielder': [], 'Catcher': []}

for player in roster:
    index = player['person']
    name = index['fullName']
    positionType = player['position']['type']
    players[positionType].append(name)

print(players)

