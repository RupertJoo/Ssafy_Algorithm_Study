def count_leaf(node_now, n, lst_adj, visited):
    stack = []
    lst_cntpop = [0] * n
    visited[node_now] = 1
    while True:
        for node_nxt in lst_adj[node_now]:
            if not visited[node_nxt]:
                stack.append(node_now)
                node_now = node_nxt
                lst_cntpop[node_now] = 1
                visited[node_now] = 1
                break
        else:
            if stack:
                node_now = stack.pop()
                lst_cntpop[node_now] = 0
            else:
                break
    return sum(lst_cntpop)


def boj1068():
    n = int(input())
    visited = [0] * n
    lst = list(map(int, input().split()))
    lst_adj = [[] for _ in range(n)]
    for child, parent in enumerate(lst[1:]):
        lst_adj[child + 1].append(parent)
        lst_adj[parent].append(child + 1)
    node_erase = int(input())
    visited[node_erase] = 1
    ans = count_leaf(0, n, lst_adj, visited)
    if node_erase == 0:
        ans = 0
    print(ans)


if __name__ == "__main__":
    boj1068()

