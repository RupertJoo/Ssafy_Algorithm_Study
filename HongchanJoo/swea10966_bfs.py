from collections import deque
def is_valid(r,c,n,m):
    return 0 <= r < n and 0 <= c < m


def swea10966_bfs():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())

        water = deque()
        arr_dist = [[-1] * m for _ in range(n)]
        for r in range(n):
            row = input()
            for c in range(m):
                if row[c] == "W":
                    water.append((r, c))
                    arr_dist[r][c] = 0

        sum_dist = 0
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while water:
            r_now, c_now = water.popleft()
            for dr, dc in move:
                r_nxt, c_nxt = r_now + dr, c_now + dc
                if is_valid(r_nxt, c_nxt, n, m) and arr_dist[r_nxt][c_nxt] == -1:
                    arr_dist[r_nxt][c_nxt] = arr_dist[r_now][c_now] + 1
                    water.append((r_nxt, c_nxt))
                    sum_dist += arr_dist[r_nxt][c_nxt]

        print("#{} {}".format(tc, sum_dist))


if __name__ == "__main__":
    swea10966_bfs()