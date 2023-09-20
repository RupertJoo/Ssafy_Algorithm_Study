from collections import deque


def bfs(n, m):
    visited = [-1] * 1_000_001
    visited[n] = 0
    q = deque()
    q.append(n)
    while q:
        n_now = q.popleft()
        if n_now == m:
            return visited[n_now]
        for n_nxt in (n_now + 1, n_now - 1, n_now * 2, n_now - 10):
            if 0 < n_nxt <= 1_000_000 and visited[n_nxt] == -1:
                visited[n_nxt] = visited[n_now] + 1
                q.append(n_nxt)


def swea17014():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        cnt = bfs(n, m)
        print(f"#{tc} {cnt}")


if __name__ == "__main__":
    swea17014()
