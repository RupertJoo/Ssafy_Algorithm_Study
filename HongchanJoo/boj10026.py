import sys
from collections import deque
input = sys.stdin.readline

def bfs(r_now, c_now, n, arr, visited, move):
    clr = arr[r_now][c_now]
    q = deque()
    visited[r_now][c_now] = 1
    q.append((r_now, c_now))


    while q:
        r_now, c_now = q.popleft()
        for dr, dc in move:
            r_nxt, c_nxt = r_now + dr, c_now + dc
            if 0 <= r_nxt < n and 0 <= c_nxt < n and not visited[r_nxt][c_nxt] and clr == arr[r_nxt][c_nxt]:
                visited[r_nxt][c_nxt] = 1
                q.append((r_nxt, c_nxt))
        # print(q)
    return visited


def bfs_cb(r_now, c_now, n, arr, visited_cb, move):
    clr = arr[r_now][c_now]
    is_cb = False
    if clr in "RG":
        is_cb = True
    q = deque()
    visited_cb[r_now][c_now] = 1
    q.append((r_now, c_now))


    while q:
        r_now, c_now = q.popleft()
        for dr, dc in move:
            r_nxt, c_nxt = r_now + dr, c_now + dc
            if not is_cb:
                if 0 <= r_nxt < n and 0 <= c_nxt < n and not visited_cb[r_nxt][c_nxt] and clr == arr[r_nxt][c_nxt]:
                    visited_cb[r_nxt][c_nxt] = 1
                    q.append((r_nxt, c_nxt))
            else:
                if 0 <= r_nxt < n and 0 <= c_nxt < n and not visited_cb[r_nxt][c_nxt] and arr[r_nxt][c_nxt] in "RG":
                    visited_cb[r_nxt][c_nxt] = 1
                    q.append((r_nxt, c_nxt))
        # print(q)
    return visited_cb



def boj10026():
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n = int(input().rstrip())
    arr = [input().rstrip() for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited_cb = [[0] * n for _ in range(n)]

    cnt = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                visited = bfs(r, c, n, arr, visited, move)
                cnt += 1
    cnt_cb = 0
    for r in range(n):
        for c in range(n):
            if not visited_cb[r][c]:
                visited_cb = bfs_cb(r, c, n, arr, visited_cb, move)
                cnt_cb += 1

    print(cnt, cnt_cb)


if __name__ == "__main__":
    boj10026()
