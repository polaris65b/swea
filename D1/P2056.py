T = int(input())

for t in range(T):
    isDay = int(input())

    Day = isDay % 100
    Month = (isDay//100) % 100

    if (Day > 31):
        print(-1)
        continue
    elif (Day == 30):
        if Month not in [4, 6, 9, 11]:
            print(-1)
            continue
    elif(Day == 28):
        if(Month != 2):
            print(-1)
            continue
    elif(Day < 28):
        print(-1)
        continue

    if(Month > 12):
        print(-1)
        continue

    print(f"#{t} {isDay}")