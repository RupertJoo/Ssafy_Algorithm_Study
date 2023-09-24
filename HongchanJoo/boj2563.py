def boj2563():
    len_wp = 100
    len_cp = 10
    area = 0
    paper = [[0] * (len_wp + 1) for _ in range(len_wp + 1)]
    for _ in range(int(input())):
        r_start, c_start = map(int, input().split())
        for r in range(r_start, r_start + len_cp):
            for c in range(c_start, c_start + len_cp):
                if not paper[r][c]:
                    paper[r][c] = 1
                    area += 1
    print(area)


if __name__ == "__main__":
    boj2563()


