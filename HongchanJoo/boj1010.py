def facto(n):
    global list_facto
    if n >= 2 and list_facto[n] == 0:
        list_facto[n] = n * facto(n - 1)
    return list_facto[n]


def boj1010():
    global list_facto
    list_facto = [0] * 31
    list_facto[0] = list_facto[1] = 1
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        ans = facto(m) // (facto(n) * (facto(m - n)))
        print(ans)


if __name__ == "__main__":
    boj1010()