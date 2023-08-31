from itertools import product

def boj15649():
    n, m = map(int, input().split())
    for i in list(product(list(range(1, n + 1)), repeat=m)):
        print(*i)


if __name__ == "__main__":
    boj15649()