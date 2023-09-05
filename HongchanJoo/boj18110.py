import sys
from collections import deque
input = sys.stdin.readline

def roundNum(n, m):
    return int((n * 10 ** m + 0.5) / (10 ** m))


def boj18110():
    n = int(input())
    if n:
        dq = deque()
        for _ in range(n):
            dq.append(int(input()))
        dq = sorted(dq)
        n_trc = roundNum(0.15 * n, 0)
        n_sum = sum(dq[n_trc: n - n_trc])
        ans = roundNum(n_sum / (n - 2 * n_trc), 0)
    else:
        ans = 0
    print(ans)


if __name__ == "__main__":
    boj18110()
