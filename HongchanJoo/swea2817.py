#  부분 수열의 합
#  백트래킹으로도 풀어보자!!
def f(i, n, s, k):
    global cnt
    if i == n:
        if s == k:
            cnt += 1
    else:
        f(i + 1, n, s + arr[i], k)
        f(i + 1, n, s, k)


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1 << n):
        s = 0
        for j in range(n):
            if i & (1 << j):
                s += arr[j]
                if s > k:
                    break
        if s == k:
            cnt += 1

    print(f"#{tc} {cnt}")

