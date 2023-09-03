import sys
input = sys.stdin.readline


def boj1920_1():
    n = int(input())
    set_a = set(map(int, input().split()))
    m = int(input())
    lst_input = list(map(int, input().split()))
    lst_ans = [0] * m
    idx = 0
    for x in lst_input:
        if x in set_a:
            lst_ans[idx] = 1
        idx += 1
    for ans in lst_ans:
        sys.stdout.write(str(ans) + "\n")


if __name__ == "__main__":
    boj1920_1()