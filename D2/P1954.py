def gen_snail_matrix(n):
    matrix = [[0]*n for _ in range(n)]

    num = 1
    x, y = 0, 0

    direction = [(0, 1), (1, 0), (0, -1), (-1,0)]
    direction_index = 0

    while num <= n*n:
        matrix[x][y] = num
        num += 1

        nx = x + direction[direction_index][0]
        ny = y + direction[direction_index][1]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            direction_index = (direction_index + 1) % 4

            nx = x + direction[direction_index][0]
            ny = y + direction[direction_index][1]

        x, y = nx, ny

    return matrix

def main():
    t = int(input())
    for case in range(t):
        n = int(input())
        snail_matrix = gen_snail_matrix(n)
        print(f"#{case + 1}")
        for row in snail_matrix:
            for num in row:
                print(num, end = " ")
            print()

if __name__ == "__main__":
    main()