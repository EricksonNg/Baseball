import statsapi
import operator
import datetime

# team = statsapi.get('team', {'teamId': 137})
# print(team)
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
first = {}
second = {}
wildcard = {}
standings = statsapi.get('standings', {'leagueId': 104})
sched = statsapi.schedule(start_date=today)
sched2 = statsapi.schedule(start_date=tomorrow)
# print(standings)
percentages = []
test = []
extra = 0
for e in range(len(standings['records'])):
    for i in range(len(standings['records'][0]['teamRecords'])):
        found = 'False'
        division_rank = int(standings['records'][e]['teamRecords'][i]['divisionRank'])
        league_rank = int(standings['records'][e]['teamRecords'][i]['leagueRank'])
        name = standings['records'][e]['teamRecords'][i]['team']['name']
        wins = standings['records'][e]['teamRecords'][i]['leagueRecord']['wins']
        losses = standings['records'][e]['teamRecords'][i]['leagueRecord']['losses']
        after_win = round((wins + 1) / ((wins + 1) + losses), 3)
        after_loss = round(wins / (wins + (losses + 1)), 3)
        percentage = float(standings['records'][e]['teamRecords'][i]['leagueRecord']['pct'])
        while found == 'False':
            for i in range (len(sched)):
                home_team = sched[i]['home_name']
                away_team = sched[i]['away_name']
                if home_team == name or away_team==name:
                    summary = sched[i]['summary']
                    found = 'True'
            if found!='True':
                for i in range(len(sched2)):
                    home_team = sched2[i]['home_name']
                    away_team = sched2[i]['away_name']
                    if home_team == name or away_team == name:
                        summary = sched2[i]['summary']
                        found = 'True'
        output = name+"("+str(wins)+"-"+str(losses)+"/"+str(percentage)+")"+"(After Win: "+str(after_win)+"/After Loss: "+str(after_loss)+")("+summary+")"
        if division_rank==1:
            percentages.append(percentage)
            first[output]=league_rank
        if division_rank==2:
            if percentage == percentages[-1]:
                first[output]=league_rank
            percentages.append(percentage)
            second[output]=league_rank
        if division_rank>2:
            if percentage == percentages[-1]:
                second[output]=league_rank
            test.append(percentage)
            test.sort(reverse=True)
            wildcard[output]=league_rank
if test[2]==test[1]:
    extra = 1
elif test[3]==test[1]:
    extra = 2
sorted_first = sorted(first.items(), key=operator.itemgetter(1))
sorted_second = sorted(second.items(), key=operator.itemgetter(1))
sorted_wildcard = sorted(wildcard.items(), key=operator.itemgetter(1))
# print(sorted_first)
# print(sorted_second)
# print(sorted_wildcard)

print("============1st============")
for i in range(len(sorted_first)):
    print(sorted_first[i][0])

print("============2nd============")
for i in range(len(sorted_second)):
    print(sorted_second[i][0])

print("============Wildcard============")
for i in range(len(sorted_wildcard)):
    if i==2+extra:
        print("============Almost===========")
    print(sorted_wildcard[i][0])

# print("")
# print("==========#1 vs #8==========")
# print(sorted_r[0][0],"vs",sorted_r[7][0])
# print("")
# print("==========#2 vs #7==========")
# print(sorted_r[1][0],"vs",sorted_r[6][0])
# print("")
# print("==========#3 vs #6==========")
# print(sorted_r[2][0],"vs",sorted_r[5][0])
# print("")
# print("===========#4 vs #5==========")
# print(sorted_r[3][0],"vs",sorted_r[4][0])

