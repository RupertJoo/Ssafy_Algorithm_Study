import sys
print = sys.stdout.write


def recursive(r_start, c_start, tri, arr):
    if tri == 1:
        arr[r_start][c_start] = "*"
        return
    tri //= 3
    for r in range(3):
        for c in range(3):
            if r == 1 and c == 1:
                continue
            recursive(r_start + r * tri, c_start + c * tri, tri, arr)


def boj2447():
    n = int(input())
    arr = [[" "] * n for _ in range(n)]
    recursive(0, 0, n, arr)
    for i in range(n):
        for j in range(n):
            print("{}".format(arr[i][j]))
        print("\n")


if __name__ == "__main__":
    boj2447()

