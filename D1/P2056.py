T = int(input())

for t in range(T):
    isDay = input()

    Year = int(isDay[:4])
    Month = int(isDay[4:6])
    Day = int(isDay[6:])

    days_in_month ={
        1:31, 2: 28, 3:31, 4:30, 5:31, 6:30,
        7:31, 8:31, 9:30, 10:31, 11:30, 12:31
    }

    if Month < 1 or Month > 12 or Day < 1 or Day > days_in_month.get(Month, 0):
        print(f"#{t+1} -1")
    else:
        print(f"#{t + 1} {isDay[:4]}/{isDay[4:6]}/{isDay[6:]}")