from collections import deque
def boj2178_1():
    n, m = map(int, input().split())
    maze = [list(map(int, input()[:m])) for _ in range(n)]
    q = deque([(0, 0)])
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while q:
        r_now, c_now = q.popleft()
        for dr, dc in move:
            r_nxt = r_now + dr
            c_nxt = c_now + dc
            if 0 <= r_nxt < n and 0 <= c_nxt < m and maze[r_nxt][c_nxt] == 1:
                q.append((r_nxt, c_nxt))
                maze[r_nxt][c_nxt] = maze[r_now][c_now] + 1
    print(maze[n - 1][m - 1])

if __name__ == "__main__":
    boj2178_1()
