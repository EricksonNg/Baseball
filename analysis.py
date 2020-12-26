stats = [1,1,1,1,1,6,6,7,8,10]

def spikeList(stats):
    start = 0
    next = 1
    spikes = [stats[start] - 0]

    while next != len(stats):
        change = stats[next] - stats[start]
        spikes.append(change)
        start += 1
        next += 1

    return spikes

def consecutive(stats):
    spikes = spikeList(stats)
    first = 0
    second = 1
    consect = 0

    while second!= len(spikes):
        if (spikes[first]==0) and (spikes[second]==0):
            consect+=1
        first+=1
        second+=1

    return consect

#not done
def streak(stats):
    spikes = spikeList(stats)
    start = 0
    next = 1
    streaks = []
    number = 0

    while next != len(spikes):
        if (spikes[start]>0) and (spikes[next]>0):
            number+=1
        elif (spikes[start]==0) and (spikes[next]>0):
            streaks.append(number)
            number=0
        elif ((spikes[start]>0) and (spikes[next]==0)):
            number+=1
            streaks.append(number)
            number = 0
        elif ((spikes[start]==0) and (spikes[next]==0)):
            streaks.append(number)
            number = 0
        else:
            print("Problem",spikes[start],spikes[next])
        start+=1
        next+=1
    # The loop stops before being able to analyze the last item in the spikes list, so the code below accounts for any streak involving the last item
    if spikes[-1]>0:
        number+=1 # If last item is over 1, then 1 has to be added to number before appending to make sure that the streak number is correct (not adding 1 if the last item is over 1 results in the streak to be unaccounted for)
    streaks.append(number) #Regardless if the last number of spike list is greater than 1, whatever number is has to be appended or else the streak could be unaccounted for)

    return streaks

print(spikeList(stats))
print(streak(stats))
largest = 0
for i in streak(stats):
    if i >= largest:
        largest = i
