import statsapi

# draft = statsapi.get('draft', {'year': 2020})
#
# for item in draft['drafts']['rounds']:
#     print(item)


print((statsapi.player_stat_data(573262)))