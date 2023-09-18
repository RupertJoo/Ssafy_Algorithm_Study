import sys


input = sys.stdin.readline
K_MAX = int(1e5)


def boj12865():
    n, k = map(int, input().split())  # n: 물건의 갯수, k: 최대 적재중량
    vw = [list(map(int, input().split())) for _ in range(n)]  # v: 물건의 가치, w: 물건의 무게 순서로 입력
    dp = [[0] * (K_MAX + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(vw[i - 1][0] + 1, k + 1):
            # print(i, j)
            # print(max(0, j - vw[i - 1][1]))
            dp[i][j] = max(dp[i - 1][j], vw[i - 1][0] + dp[i - 1][max(0, j - vw[i - 1][1])])
            # dp[i][j] = dp[i - 1][j]
    for i in dp:
        print(i[:20])

if __name__ == "__main__":
    boj12865()