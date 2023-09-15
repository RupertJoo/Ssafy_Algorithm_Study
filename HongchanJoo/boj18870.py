import sys
input = sys.stdin.readline
print = sys.stdout.write

def boj18870():
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    arr_2 = [[0,0,0] for _ in range(n)]

    for i, a in enumerate(arr):
        arr_2[i][0], arr_2[i][1] = i, a

    arr_2.sort(key=lambda x: x[1])

    cnt_diff = 0
    for i in range(1,n):
        if arr_2[i][1] != arr_2[i - 1][1]:
            cnt_diff += 1
        arr_2[i][2] = cnt_diff

    arr_2.sort(key=lambda x: x[0])

    for a in arr_2:
        print("{} ".format(a[2]))
    print("\n")


if __name__ == "__main__":
    boj18870()