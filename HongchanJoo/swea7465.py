from collections import deque

def bfs(v, visited, list_adj):
    q = deque()
    q.append(v)
    visited += 1 << v
    while q:
        v_now = q.popleft()
        for v_nxt in list_adj[v_now]:
            if not visited & 1 << v_nxt:
                visited += 1 << v_nxt
                q.append(v_nxt)
    return visited


def swea17015():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        # arr = list(map(int, input().split()))
        lst_adj = [[] for _ in range(n + 1)]
        # visited = [0] * (n + 1)
        visited = 0
        for i in range(m):
            v_start, v_end = map(int, input().split())
            lst_adj[v_start].append(v_end)
            lst_adj[v_end].append(v_start)

        cnt = 0
        for v in range(1, n + 1):
            if not visited & 1 << v:
                visited = bfs(v, visited, lst_adj)
                cnt += 1
        print(f"#{tc} {cnt}")


if __name__ == "__main__":
    swea17015()