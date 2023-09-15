import sys
input = sys.stdin.readline
print = sys.stdout.write

def boj18870():
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    arr_sort = arr[:]
    arr_sort.sort()
    dict_num = dict()

    num_min = int(-1e9)
    cnt_diff = 0
    for a in arr_sort:
        if num_min < a:
            num_min = a
            dict_num[a] = cnt_diff
            cnt_diff += 1


    for a in arr:
        print("{} ".format(dict_num[a]))
    print("\n")


if __name__ == "__main__":
    boj18870()