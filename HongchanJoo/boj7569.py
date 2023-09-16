from collections import deque
import sys
input = sys.stdin.readline


def boj7569():
    m, n, h = map(int, input().rstrip().split())
    box = [[] for _ in range(h)]
    for l in range(h):
        box[l] = [list(map(int, input().rstrip().split())) for _ in range(n)]
    visited = [[] for _ in range(h)]
    for l in range(h):
        visited[l] = [[-1] * m for _ in range(n)]
    cnt = 0
    cnt_empty = 0
    tomato = deque()
    for l in range(h):
        for r in range(n):
            for c in range(m):
                if box[l][r][c] == 1:
                    tomato.append((l, r, c))
                    visited[l][r][c] = 0
                    cnt += 1
                elif box[l][r][c] == -1:
                    cnt_empty += 1
    num_tomato = n * m * h - cnt_empty
    move = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
    is_bfs = False
    while tomato:
        l_now, r_now, c_now = tomato.popleft()
        for dl, dr, dc in move:
            l_nxt, r_nxt, c_nxt = l_now + dl, r_now + dr, c_now + dc
            if 0 <= l_nxt < h and 0 <= r_nxt < n and 0 <= c_nxt < m:
                if not box[l_nxt][r_nxt][c_nxt] and visited[l_nxt][r_nxt][c_nxt] == -1:
                    is_bfs = True
                    box[l_nxt][r_nxt][c_nxt] = 1
                    visited[l_nxt][r_nxt][c_nxt] = visited[l_now][r_now][c_now] + 1
                    cnt += 1
                    tomato.append((l_nxt, r_nxt, c_nxt))
    if cnt == num_tomato:
        if is_bfs:
            print(visited[l_now][r_now][c_now])
        else:
            print(0)
    else:
        print(-1)


if __name__ == "__main__":
    boj7569()