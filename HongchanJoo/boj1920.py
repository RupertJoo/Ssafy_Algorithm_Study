import sys
input = sys.stdin.readline


def binarySearch(x, lst):
    idx_start = 0
    idx_end = len(lst) - 1
    idx_middle = (idx_start + idx_end) // 2
    while idx_start <= idx_end:
        if lst[idx_middle] == x:
            return "1"
        elif lst[idx_middle] > x:
            idx_end = idx_middle - 1
            idx_middle = (idx_start + idx_end) // 2
        else:
            idx_start = idx_middle + 1
            idx_middle = (idx_start + idx_end) // 2
    return "0"


def boj1920():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    m = int(input())
    lst_input = list(map(int, input().split()))
    for x in lst_input:
        sys.stdout.write(binarySearch(x, lst) + "\n")


if __name__ == "__main__":
    boj1920()