def swea11315():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list(list(input()) for _ in range(n))
        # for i in arr:
        #     print(*i)
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]
        ans = "NO"
        is_break = False
        for r in range(n):
            for c in range(n):
                for k in range(8):
                    if arr[r][c] == 'o':
                        rr = r
                        cc = c
                        nr = rr + dr[k]
                        nc = cc + dc[k]
                        i = 1
                        while 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 'o':
                            i += 1
                            rr = nr
                            cc = nc
                            nr = rr + dr[k]
                            nc = cc + dc[k]
                            # print(nr, nc)
                        if i >= 5:
                            ans = "YES"
                            is_break = True
                            break

                if is_break:
                    break
            if is_break:
                break
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea11315()