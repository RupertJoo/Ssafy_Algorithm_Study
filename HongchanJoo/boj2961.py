def boj2961():
    n = int(input())
    sours = [0] * n
    bitters = [0] * n
    ans = float("inf")
    for i in range(n):
        s, b = map(int, input().split())
        sours[i] = s
        bitters[i] = b
    sours_multi = [1] * ((1 << n) - 1)
    bitters_sum = [0] * ((1 << n) - 1)
    for i in range(1, 1 << n):
        for j in range(n):
            if i & 1 << j:
                sours_multi[i - 1] *= sours[j]
                bitters_sum[i - 1] += bitters[j]
        ans_temp = abs(sours_multi[i - 1] - bitters_sum[i - 1])
        if ans > ans_temp:
            ans = ans_temp
    print(ans)


if __name__ == "__main__":
    boj2961()



