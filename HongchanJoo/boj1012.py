def dfs_cabbage(cabbage, list_cabbage, m, n):
    worm = 0
    stack = []
    visited = [[0] * m for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r, c in list_cabbage:
        now_r, now_c = r, c
        if not visited[now_r][now_c]:
            worm += 1
            visited[now_r][now_c] = 1
            while True:
                for i in range(4):
                    nxt_r = now_r + dr[i]
                    nxt_c = now_c + dc[i]
                    if 0 <= nxt_r < n and 0 <= nxt_c < m and cabbage[nxt_r][nxt_c] == 1 and not visited[nxt_r][nxt_c]:
                        # print(f"next_r:{nxt_r}, next_c: {nxt_c}")
                        stack.append([now_r, now_c])
                        visited[nxt_r][nxt_c] = 1
                        now_r = nxt_r
                        now_c = nxt_c
                        break
                    else:
                        continue
                else:
                    if stack:
                        now_r, now_c = stack.pop()
                    else:
                        break
            # for i in visited:
            #     print(*i)
            # print("_" * 20)
            # print(list_cabbage)
    return worm


def boj1012():
    for tc in range(1, int(input()) + 1):
        m, n, k = map(int, input().split())
        cabbage = [[0] * m for _ in range(n)]
        list_cabbage = [[None, None] for _ in range(k)]
        for i in range(k):
            x_cabbage, y_cabbage = map(int, input().split())
            cabbage[y_cabbage][x_cabbage] = 1
            list_cabbage[i][0], list_cabbage[i][1] = y_cabbage, x_cabbage
        # for i in cabbage:
        #     print(*i)
        # print(list_cabbage)
        worm = dfs_cabbage(cabbage, list_cabbage, m, n)
        print(worm)


if __name__ == "__main__":
    boj1012()