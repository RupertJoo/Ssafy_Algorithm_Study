import sys
input = sys.stdin.readline


def boj11399():
    n = int(input(5))
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(1, n):
        arr[i] += arr[i - 1]
    print(sum(arr))


if __name__ == "__main__":
    boj11399()