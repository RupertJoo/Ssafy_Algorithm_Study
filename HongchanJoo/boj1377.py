import sys
input = sys.stdin.readline
def boj1377():
    n = int(input())
    arr = list(int(input()) for _ in range(n))
    count_bubblesort = 0
    is_sorted = False
    for i in range(n - 1, 0, -1):
        count_bubblesort += 1
        for ii in range(n - 1):
            if arr[ii] > arr[ii + 1]:
                is_sorted = False
                break
            else:
                is_sorted = True
        if is_sorted:
            break
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # print(arr)
    print(count_bubblesort)


if __name__ == "__main__":
    boj1377()
