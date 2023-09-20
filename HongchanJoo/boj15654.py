from itertools import permutations
def boj15654():
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    perm = list(permutations(lst, m))
    for p in perm:
        print(*p)


if __name__ == "__main__":
    boj15654()
