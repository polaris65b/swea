def start_clap(n):
    for i in range(1, n + 1):
        str_i = str(i)
        count = 0
        for test in str_i:
            if test == "3" or test == "6" or test == "9":
                count += 1
        if count > 0:
            print("-"*count, end = "")
        else:
            print(str_i, end = "")
        print(" ", end = "")

def main():
    n = int(input())
    start_clap(n)

if __name__ == "__main__":
    main()