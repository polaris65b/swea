P, K = map(int, input().split())

count = 1

while P != K:
    if K == 999:
        K = 0
    else:
        K = K + 1
    count = count + 1

print(count)