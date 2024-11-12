T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    share = a // b
    remain = a % b
    print(f"#{t+1} {share} {remain}")