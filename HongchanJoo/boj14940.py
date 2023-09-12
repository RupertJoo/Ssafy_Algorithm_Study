"""
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
"""
import sys
from collections import deque
input = sys.stdin.readline

def in_arr(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

def bfs(arr, r_start, c_start, n, m):
    q = deque()
    move = ((1, 0), (-1, 0), (0, -1), (0, 1))
    visited = [[-1] * m for _ in range(n)]

    rc_now = (r_start, c_start)
    q.append(rc_now)
    visited[rc_now[0]][rc_now[1]] = 0
    while q:
        r_now, c_now = q.popleft()
        for dr, dc in move:
            r_nxt = r_now + dr
            c_nxt = c_now + dc
            if in_arr(r_nxt, c_nxt, n, m) and visited[r_nxt][c_nxt] == -1 and arr[r_nxt][c_nxt]:
                # print(q)
                q.append((r_nxt, c_nxt))
                visited[r_nxt][c_nxt] = visited[r_now][c_now] + 1
    # print(arr[13][12])
    for r in range(n):
        for c in range(m):
            if not arr[r][c]:
                visited[r][c] = 0
            # print(c)
    return visited


def boj14940():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    is_break = False
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 2:
                is_break = True
                break
        if is_break:
            break
    # print(r, c)
    visited = bfs(arr, r, c, n, m)
    for a in visited:
        print(*a)


if __name__ == "__main__":
    boj14940()





