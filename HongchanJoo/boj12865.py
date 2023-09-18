import sys


input = sys.stdin.readline
K_MAX = int(1e5)


def boj12865():
    n, k = map(int, input().split())  # n: 물건의 갯수, k: 최대 적재중량
    wv = [list(map(int, input().split())) for _ in range(n)]  # w: 물건의 무게 순서로 입력, v: 물건의 가치
    dp = [[0] * (K_MAX + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j < wv[i - 1][0]:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = max(dp[i - 1][j], wv[i - 1][1] + dp[i - 1][j - wv[i - 1][0]])
    print(dp[n][k])


if __name__ == "__main__":
    boj12865()