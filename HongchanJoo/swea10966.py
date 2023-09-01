# 물놀이를 가자

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    dp = [list(input()) for _ in range(n)]
    ans = 0
    limit = 2000  # 최소값 비교 대상, 특정 방향에 물이 없는 경우를 감안해서..
    # 오른쪽 아래로 순회하며 min(왼쪽, 위쪽)
    for r in range(n):
        for c in range(c):
            if dp[r][c] == "W":
                dp[r][c] =0
            else:
                up = dp[r - 1][c] if r > 0 else limit
                left = dp[r][c - 1] if c > 0 else limit
                dp[r][c] = min(up, left) + 1

    # 왼쪽 위로 순회하며 min(오른쪽, 아래쪽)
    print(f"{tc}")