def dfs(s, node, g):
    visited = [0] * (node + 1)
    stack = []
    i = s
    visited[i] = 1

    while True:
        for j in list_adj[i]:
            if j == g:
                return 1
            else:
                if not visited[j]:
                    stack.append(i)
                    i = j
                    visited[j] = 1
                    break
        else:
            if stack:
                i = stack.pop()
            else:
                return 0
                break

def swea1219():
    global list_adj
    while True:
        try:
            tc, edge = map(int, input().split())
            list_adj = [[] for _ in range(100)]
            arr_nodes = list(map(int, input().split()))
            for i in range(edge):
                node_start, node_end = arr_nodes[2 * i], arr_nodes[2 * i + 1]
                list_adj[node_start].append(node_end)
            s, g = 0, 99
            print(f"#{tc} {dfs(s,99, g)}")
        except:
            break


if __name__ == "__main__":
    swea1219()
