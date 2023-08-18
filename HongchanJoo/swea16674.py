import sys
sys.stdin = open("./refs/input_swea_16674.txt")

def maze_runner(r_now, c_now, maze, n, value_goal):
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0] * n for _ in range(n)]

    len_q = 100
    q = [[] for _ in range(len_q)]
    front = rear = 0

    rear = (rear + 1) % len_q
    q[rear] = [r_now, c_now]
    visited[r_now][c_now] = 1

    while front != rear:
        front = (front + 1) % len_q
        r_now, c_now = q[front]
        if maze[r_now][c_now] == value_goal:
            return visited[r_now][c_now] - 2
        else:
            for dr, dc in move:
                r_nxt = r_now + dr
                c_nxt = c_now + dc
                if 0 <= r_nxt < n and 0 <= c_nxt < n and maze[r_nxt][c_nxt] != 1 and not visited[r_nxt][c_nxt]:
                    rear = (rear + 1) % len_q
                    # print(f"rear = {rear}")
                    q[rear] = [r_nxt, c_nxt]
                    visited[r_nxt][c_nxt] = visited[r_now][c_now] + 1
    return 0




def find_start(arr, n, value_start):
    for r in range(n):
        for c in range(n):
            if arr[r][c] == value_start:
                return r, c

def swea16674():
    value_start = 2
    value_goal = 3
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = [list(map(int, input())) for _ in range(n)]
        # for i in arr:
        #     print(*i)
        r_start, c_start = find_start(arr, n, value_start)
        ans = maze_runner(r_start,c_start, arr, n, value_goal)
        print(f"#{tc} {ans}")



if __name__ == "__main__":
    swea16674()