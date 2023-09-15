import sys
sys.setrecursionlimit(2000)


def boj11726():
    n = int(input())
    arr = [0] * (1000 + 1)

    def fibo(n):
        if n > 2 and not arr[n]:
            arr[n] = fibo(n - 1) + fibo(n - 2)
        return arr[n]
    arr[1] = 1
    arr[2] = 2
    print(fibo(n) % 10_007)


if __name__ == "__main__":
    boj11726()
