def score_count(score):
    tmp = (0,0)
    score_map = set(score)
    for i in score_map:
        cnt = score.count(i)
        if cnt > tmp[0]:
            tmp = (cnt, i)
    return tmp[1]

def main():
    t = int(input())
    for _ in range(t):
        case = int(input())
        score = list(map(int, input().split()))
        m_score = score_count(score)
        print(f"#{case} {m_score}")

if __name__=="__main__":
    main()