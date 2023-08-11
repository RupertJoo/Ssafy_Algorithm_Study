def swea9489():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        arr = list(list(map(int, input().split())) for _ in range(n))
        # for i in arr:
        #     print(*i)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        max_len_total = 0
        for r in range(n):
            for c in range(m):
                # max_len = 0
                for k in range(4):
                    if arr[r][c] == 1:
                        rr = r
                        cc = c
                        max_len = 0
                        i = 1
                        nr = rr + dr[k]
                        nc = cc + dc[k]
                        while 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                            i += 1
                            rr = nr
                            cc = nc
                            nr = rr + dr[k]
                            nc = cc + dc[k]
                        if max_len < i:
                            max_len = i
                        if max_len_total < max_len:
                            max_len_total = max_len
        print(f"#{tc} {max_len_total}")


if __name__ == "__main__":
    swea9489()