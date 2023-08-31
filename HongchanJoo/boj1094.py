def boj1094():
    n = int(input())
    i = 0
    ans = 0
    while True:
        if n <= (1 << i):
            break
        i += 1
    if n == 1 << i:
        ans = 1
    else:
        for j in range(i):
            if n & (1 << i - j - 1):
                ans += 1
    print(ans)


if __name__ == "__main__":
    boj1094()