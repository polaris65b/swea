T = int(input())

for test_case in range(1, T + 1):
    mean = 0
    numbers = list(map(int, input().split()))

    for num in numbers:
        mean += num
    mean = round(mean/10)
    print(f"#{test_case} {mean}")