import sys
input = sys.stdin.readline


def boj29791():
    n_nova, n_origin = map(int, input().split())
    nova = sorted(list(map(int, input().split())))
    origin = sorted(list(map(int, input().split())))

    immune_nova = nova[0] + 90
    cool_nova = nova[0] + 100
    cnt_nova = 1

    immune_origin = origin[0] + 90
    cool_origin = origin[0] + 360
    cnt_origin = 1

    for n in nova[1:]:
        if immune_nova <= n and cool_nova <= n:
            immune_nova = n + 90
            cool_nova = n + 100
            cnt_nova += 1

    for o in origin[1:]:
        if immune_origin <= o and cool_origin <= o:
            immune_origin = o + 90
            cool_origin = o + 360
            cnt_origin += 1

    print(cnt_nova, cnt_origin)


if __name__ == "__main__":
    boj29791()