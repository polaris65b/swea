def gen_max_kill_fly(n, m, matrix_fly):
    max_kill = 0
    for x in range(n - m + 1):
        for y in range(n - m + 1):
            kill_num = 0
            for tx in range(x, x + m):
                for ty in range(y, y+m):
                    kill_num += matrix_fly[tx][ty]
            if max_kill < kill_num:
                max_kill = kill_num
    return max_kill

def input_matrix_fly(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def main():
    t = int(input())
    for case in range(t):
        n, m = list(map(int, input().split()))
        matrix_fly = input_matrix_fly(n)
        print(f"#{case + 1} {gen_max_kill_fly(n, m, matrix_fly)}")

if __name__ == "__main__":
    main()