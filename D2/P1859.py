def do_buy(day, price):
    money = 0
    max_price = 0
    for i in range(day-1, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
        else:
            money += max_price - price[i]
    return money

def main():
    t = int(input())

    for case in range(t):
        day = int(input())
        price = list(map(int, input().split()))
        money = do_buy(day, price)
        print(f"#{case+1} {money}")

if __name__ == "__main__":
    main()