def exitMaze(rc_now, rc_goal, size_maze, maze):
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n, m = size_maze
    visited = [[0] * m for _ in range(n)]
    len_q = 10_000
    q = [[] for _ in range(len_q)]
    front = rear = 0

    rear = (rear + 1) % len_q
    q[rear] = rc_now
    visited[rc_now[0]][rc_now[1]] = 1

    while front != rear:
        front = (front + 1) % len_q
        r_now, c_now = q[front]
        if [r_now,c_now] == rc_goal:
            return visited[r_now][c_now]
        else:
            for dr, dc in move:
                r_nxt = r_now + dr
                c_nxt = c_now + dc
                if 0 <= r_nxt < n and 0 <= c_nxt < m and maze[r_nxt][c_nxt] == 1 and not visited[r_nxt][c_nxt]:
                    rear = (rear + 1) % len_q
                    q[rear] = [r_nxt, c_nxt]
                    visited[r_nxt][c_nxt] = visited[r_now][c_now] + 1


def boj2178():
    n, m = map(int, input().split())
    maze = [list(map(int, input()[:m])) for _ in range(n)]
    size_maze = [n, m]
    rc_now = [0, 0]
    rc_goal = [n - 1, m - 1]
    ans = exitMaze(rc_now, rc_goal, size_maze, maze)
    print(ans)


if __name__ == "__main__":
    boj2178()
