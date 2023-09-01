from collections import deque


def is_valid(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

def bfs(n, m, arr):
    move = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    days = 0
    tomato = 0
    empty = 0
    dq = deque()
    visited = [[-1] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                dq.append((r,c))
                tomato += 1
                visited[r][c] = 0
            if arr[r][c] == -1:
                empty += 1
    while dq:
        if tomato == n * m - empty:
            break
        r_now, c_now = dq.popleft()
        for dr, dc in move:
            r_nxt, c_nxt = r_now + dr, c_now + dc
            if is_valid(r_nxt, c_nxt, n, m) and not arr[r_nxt][c_nxt] and visited[r_nxt][c_nxt] == -1:
                arr[r_nxt][c_nxt] += 1
                dq.append((r_nxt, c_nxt))
                visited[r_nxt][c_nxt] = visited[r_now][c_now] + 1
                days = max(days, visited[r_nxt][c_nxt])
                tomato += 1

    days = days if tomato == n * m - empty else -1
    return days


def boj7576():
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    days = bfs(n, m, arr)
    print(days)


if __name__ == "__main__":
    boj7576()