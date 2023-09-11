import sys
from collections import deque
input = sys.stdin.readline


def find_parent(x, n, lst_adj):
    q = deque()
    visited = [0] * (n + 1)
    parents = [0] * (n + 1)
    q.append(x)
    visited[x] = 1
    while q:
        node_now = q.popleft()
        for node_nxt in lst_adj[node_now]:
            if not visited[node_nxt]:
                q.append(node_nxt)
                visited[node_nxt] = 1
                parents[node_nxt] = node_now
    return parents


def boj11725():
    n = int(input())

    lst_adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        node_s, node_e = map(int, input().split())
        lst_adj[node_s].append(node_e)
        lst_adj[node_e].append(node_s)
        # print(lst_adj)
    parents = find_parent(1, n, lst_adj)
    for p in parents[2:]:
        sys.stdout.write(str(p) + "\n")


if __name__ == "__main__":
    boj11725()
