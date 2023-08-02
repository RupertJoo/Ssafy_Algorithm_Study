def solve2068():
    n = int(input())
    for i in range(1, n + 1):
        numbers = list(map(int, input().split(' ')))
        numbers.sort()
        print("#" + str(i) + " " + str(numbers[-1]))

if __name__ == "__main__":
    solve2068()