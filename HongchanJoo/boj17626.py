def boj17626():
    dp = [0] * 50001
    dp[1] = 1
    n = int(input())
    for x in range(1, n + 1):
        cnt = 0
        i = x
        while i:
            square_min = int(i ** 0.5) ** 2
            i -= square_min
            cnt += 1
        dp[x] = cnt

        for j in range(1, int(x ** 0.5) + 1):
            dp[x] = min(dp[x], dp[j ** 2] + dp[x - j ** 2])
    print(dp[n])


if __name__ == "__main__":
    boj17626()
