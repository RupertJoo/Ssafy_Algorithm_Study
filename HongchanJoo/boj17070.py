def isDiagonal(arr, r, c):
    return arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0

def boj17070():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # horisontal, vertical, diagonal 순서로 저장
    dp = [[[0,0,0]  for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1
    for r in range(n):
        for c in range(1, n):  # 파이프의 열 번호는 항상 0보다 크기 때문
            if r < n and c + 1 < n and arr[r][c + 1] == 0:
                dp[r][c + 1][0] += dp[r][c][0] + dp[r][c][2]
            if r  + 1 < n and c < n and arr[r + 1][c] == 0:
                dp[r + 1][c][1] += dp[r][c][1] + dp[r][c][2]
            if r + 1 < n and c + 1 < n and isDiagonal(arr, r, c):
                dp[r + 1][c + 1][2] += dp[r][c][0] + dp[r][c][1] + dp[r][c][2]

    print(sum(dp[-1][-1]))


if __name__ == "__main__":
    boj17070()