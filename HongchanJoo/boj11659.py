import sys
input = sys.stdin.readline
print = sys.stdout.write

def boj11659():
    n, m = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    arr_stack = arr[:]
    for i in range(1, n):
        arr_stack[i] += arr_stack[i - 1]
    for _ in range(m):
        i_start, i_end = map(int, input().rstrip().split())
        if i_start < 2:
            x = 0
        else:
            x = arr_stack[i_start - 2]
        ans = arr_stack[i_end - 1] - x
        print("{} \n".format(ans))


if __name__ == "__main__":
    boj11659()