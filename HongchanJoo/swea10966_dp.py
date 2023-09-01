def swea10966_dp():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        dp = [list(input()) for _ in range(n)]
        limit = 2000
        ans = 0

        for r in range(n):
            for c in range(m):
                if dp[r][c] == "W":
                    dp[r][c] = 0
                else:
                    up = dp[r - 1][c] if r > 0 else limit
                    left = dp[r][c - 1] if c > 0 else limit
                    dp[r][c] = min(up, left) + 1

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if dp[r][c] == "W":
                    dp[r][c] = 0
                else:
                    down = dp[r + 1][c] if r < n - 1 else limit
                    right = dp[r][c + 1] if c < m - 1 else limit
                    dp[r][c] = min(dp[r][c], min(down, right) + 1)
                    ans += dp[r][c]
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea10966_dp()
