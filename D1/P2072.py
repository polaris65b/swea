T = int(input())

for t in range(T):
    oddSum = 0
    numbers = list(map(int, input().split()))

    for num in numbers:
        if((num%2)==1):
            oddSum += num

    print(f"#{t+1} {oddSum}")