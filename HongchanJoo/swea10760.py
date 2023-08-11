def swea10760():
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        arr = list(list(map(int, input().split())) for _ in range(n))
        count_candidate = 0
        for r in range(n):
            for c in range(m):
                height = arr[r][c]
                count_mesh = 0
                for k in range(8):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] < height:
                        count_mesh += 1
                if count_mesh >= 4:
                    count_candidate += 1
        print(f"{tc} {count_candidate}")


if __name__ == "__main__":
    swea10760()