def count_factors(N, factor):
    count = 0
    while(N % factor) == 0:
        N //= factor
        count += 1
    return count

def main():
    T = int(input())

    for t in range(T):
        N = int(input())

        a2 = count_factors(N, 2)
        b3 = count_factors(N, 3)
        c5 = count_factors(N, 5)
        d7 = count_factors(N, 7)
        e11 = count_factors(N, 11)

        print(f"#{t+1} {a2} {b3} {c5} {d7} {e11}")


if __name__ == "__main__":
    main()