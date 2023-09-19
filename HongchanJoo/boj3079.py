import sys
input = sys.stdin.readline


def boj3079():
    n, m = map(int, input().split())
    delays = [int(input()) for _ in range(n)]
    min_time = min(delays)
    ans = max_time = max(delays) * m
    # print(delays)
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        cnt = 0
        for d in delays:
            cnt += mid_time // d
            if cnt >= m:
                break
        if cnt >= m:
            max_time = mid_time - 1
            ans = min(ans, mid_time)
        else:
            min_time = mid_time + 1
    print(ans)


if __name__ == "__main__":
    boj3079()

