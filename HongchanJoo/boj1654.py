import sys
input = sys.stdin.readline


def boj1654():
    k, n = map(int, input().split())
    cords = [int(input()) for _ in range(k)]
    len_min = 1
    len_max = max(cords)
    while len_min <= len_max:
        len_mid = (len_min + len_max) // 2
        num_cords = 0
        for c in cords:
            num_cords += c // len_mid
        if num_cords >= n:
            len_min = len_mid + 1
        else:
            len_max = len_mid - 1
    print(len_max)


if __name__ == "__main__":
    boj1654()


