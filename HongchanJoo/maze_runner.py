def bfs(maze, r_start, c_start, n):
    visited = [[0] * n for _ in range(n)]  # visited 생성
    q = []  # 큐 생성
    q.append((r_start, c_start))  # 시점 enqueue
    visited[r_start][c_start] = 1  #  시점 방문표시
    while q:
        r_now, c_now = q.pop(0)  # dequeue
        if maze[r_now][c_now] == 3:
            return visited[r_now][c_now] - 2  # 종점에 도달하기까지 지나온 칸 수
        for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            r_new, c_new = r_now + dr, c_now + dc
            if 0 <= r_new < n and 0 <= c_new < n and maze[r_new][c_new] != 1 and visited[r_new][c_new] == 0:
                q.append((r_new, c_new))
                visited[r_new][c_new] = visited[r_now][c_now] + 1
    return 0  # 탐색을 마칠 때 까지 종점에 도달할 수 없을 경우


def find_start(n, maze):
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                return r, c


def maze_runner():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        maze = [list(map(int, input())) for _ in range(n)]
        r_start, c_start = find_start(n, maze)
        ans = bfs(maze, r_start, c_start, n)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    maze_runner()
