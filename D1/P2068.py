T = int(input())

for i in range(T):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f"#{i} {numbers[-1]}")