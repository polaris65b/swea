def is_right_sdq(matrix_sdq):
    result = 0
    for x in range(9):
        for y in range(9):
            
    return result

def gen_sdq():
    matrix_sdq = []
    for _ in range(9):
        row = list(map(int, input().split()))
        matrix_sdq.append(row)
    return matrix_sdq

def main():
    t = int(input())
    for case in range(t):
        matrix_sdq = gen_sdq()
        print(f"#{case + 1} {is_right_sdq(matrix_sdq)}")

if __name__ == "__main__":
    main()