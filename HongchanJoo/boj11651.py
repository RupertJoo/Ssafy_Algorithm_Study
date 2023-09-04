import sys
input = sys.stdin.readline

def boj11651():
    n = int(input())
    # arr = [[]] * n
    arr = [list(map(int, input().split())) for _ in range(n)]
    # arr = arr.sort(key=lambda x: x[0])
    arr = sorted(arr, key=lambda x: (x[1], x[0]))
    for i in arr:
        sys.stdout.write(str(i[0]) + " " + str(i[1]) + "\n")


if __name__ == "__main__":
    boj11651()
