from itertools import product
import sys

def boj15652():
    n, m = map(int, input().split())
    for i in product(range(1,n + 1), repeat=m):
        isValid = True
        for j in range(1, m):
            if i[j - 1] > i[j]:
                isValid = False
                break
        if isValid:
            for j in i:
                sys.stdout.write(str(j) + " ")
            sys.stdout.write("\n")


if __name__ == "__main__":
    boj15652()

