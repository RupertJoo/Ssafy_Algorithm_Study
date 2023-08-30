def dfs(n, v, list_adj):
    visited = [0] * (n + 1)
    stack = []
    visited[v] = 1
    print(v, end=" ")

    while True:
        for v_nxt in list_adj[v]:
            if not visited[v_nxt]:
                stack.append(v)
                v = v_nxt
                print(v, end=" ")
                visited[v] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                print()
                break

def dfs1(list_adj, v, visited_dfs):
    # global visited_dfs

    visited_dfs[v] = True
    print(v, end=" ")
    for i in list_adj[v]:
        if not visited_dfs[i]:
            dfs1(list_adj, i, visited_dfs)

def bfs(n, v, list_adj):

    visited = [0] * (n + 1)
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for v_nxt in list_adj[v]:
            if not visited[v_nxt]:
                queue.append(v_nxt)
                visited[v_nxt] = visited[v] + 1
    print()

def boj1260():
    # global visited_dfs
    n, m, v = map(int, input().split())
    list_adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        node_start, node_end = map(int, input().split())
        list_adj[node_start].append(node_end)
        list_adj[node_end].append(node_start)
    for l in list_adj:
        l.sort()
    visited_dfs = [False] * (n + 1)
    dfs1(list_adj, v, visited_dfs)
    print()
    # dfs(n, v, list_adj)
    bfs(n, v, list_adj)

if __name__ == "__main__":
    boj1260()


