import sys
input = sys.stdin.readline


def boj3079():
    n, m = map(int, input().split())
    delays = [0] * n
    for i in range(n):
        delays[i] = int(input())
    min_time = 0
    max_time = int(1e9)
    mid_time = (min_time + max_time) // 2
    cnt = 0
    dict_tc = dict()
    while min_time <= max_time:
        cnt = 0
        # print(f"{max_time}")

        for d in delays:
            cnt += max_time // d
        if cnt > m:
            max_time = max_time // 2 - 1
        if cnt < m:
            max_time = max_time // 2 + 1

        print(f"max_time: {max_time}cnt: {cnt}")
        if cnt == m:
            break
    #     mid_time = (min_time + max_time) // 2
    #     if cnt > m:
    #         max_time = mid_time - 1
    #     elif cnt < m:
    #         min_time = mid_time + 1
    #     print(min_time)
    #     print(cnt)
    print(mid_time)

if __name__ == "__main__":
    boj3079()

