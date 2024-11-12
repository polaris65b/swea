N = int(input())

for factor in range(1, N + 1):
    if (N % factor) == 0:
        print(factor, end = " ")