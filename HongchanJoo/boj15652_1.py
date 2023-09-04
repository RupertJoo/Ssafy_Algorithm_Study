def recursive(lst, i, n, m):
    if i == m:
        print(*lst[1:])
    else:
        for j in range(lst[-1] , n + 1):
            recursive(lst+[j], i + 1, n, m)


def boj15652_1():
    n, m = map(int, input().split())
    recursive([1], 0, n, m)


if __name__ == "__main__":
    boj15652_1()