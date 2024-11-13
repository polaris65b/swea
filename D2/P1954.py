def generate_snail_matrix(n):
    matrix = [[0]*n for _ in range(n)]

    x, y = 0, 0
    num = 1

    direction = [(0,1), (1,0), (0,-1), (-1,0)]
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
        print(f"#{case + 1}")
        snail_matrix = generate_snail_matrix(n)
        for row in snail_matrix:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()