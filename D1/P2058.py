N = int(input())

sum = 0

while(N > 0):
    sum += N % 10
    N = int(N/10)

print(sum)