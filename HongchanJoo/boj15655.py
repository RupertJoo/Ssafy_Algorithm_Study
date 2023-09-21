from itertools import combinations


def boj15655():
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    combi = combinations(lst, m)
    for c in combi:
        print(*c)


if __name__ == "__main__":
    boj15655()