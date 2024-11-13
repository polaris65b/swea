def do_many_score(score):
    count_score = 0
    many_score = 0
    set_score = set(score)
    for i in set_score:
        if score.count(i) > count_score:
            count_score = score.count(i)
            many_score = i
        elif score.count(i) == count_score and i > many_score:
            many_score = i
    return many_score

def main():
    t = int(input())
    for _ in range(t):
        case = int(input())
        score = list(map(int, input().split()))
        print(f"#{case} {do_many_score(score)}")

if __name__ == "__main__":
    main()