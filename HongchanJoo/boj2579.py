def boj2579():
    n = int(input())
    stair = [int(input()) for _ in range(n)]
    score = [0] * n
    count_1 = [0] * n
    if n > 2:
        score[0] = stair[0]
        score[1] = score[0] + stair[1]
        for i in range(2, n):
            score[i] = max(score[i - 3] + stair[i - 1] + stair[i], score[i - 2] + stair[i])
        print(score[n - 1])
    else:
        print(sum(stair))


if __name__ == "__main__":
    boj2579()