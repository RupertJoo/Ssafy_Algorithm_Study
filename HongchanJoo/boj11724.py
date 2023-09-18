import sys
from collections import deque
input = sys.stdin.readline


def bfs(v, visited, lst_adj):
    q = deque()
    visited[v] = 1
    q.append(v)
    while q:
        v_now = q.pop()
        for v_nxt in lst_adj[v_now]:
            if not visited[v_nxt]:
                visited[v_nxt] = 1
                q.append(v_nxt)
    return visited


def boj11724():
    n, m = map(int, input().split())
    lst_adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        v_start, v_end = map(int, input().split())
        lst_adj[v_start].append(v_end)
        lst_adj[v_end].append(v_start)
    visited = [0] * (n + 1)
    cnt = 0
    for v in range(1, n + 1):
        if not visited[v]:
            visited = bfs(v, visited, lst_adj)
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    boj11724()