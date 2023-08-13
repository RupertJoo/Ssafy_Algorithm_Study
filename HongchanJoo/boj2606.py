def cal_edge(list_adj, node, start):
    visited = [0] * (node + 1)
    stack = []
    now = start
    visited[now] = 1
    num_edge = 0
    while True:
        for nxt in list_adj[now]:
            if not visited[nxt]:
                stack.append(now)
                now = nxt
                visited[now] = 1
                num_edge += 1
                break
        else:
            if stack:
                now = stack.pop()
            else:
                return num_edge

def boj2606():
    global list_adj
    node = int(input())
    list_adj = [[] for _ in range(node + 1)]
    for _ in range(int(input())):
        s, e = map(int, input().split())
        list_adj[s].append(e)
        list_adj[e].append(s)
    # for i in list_adj:
    #     print(i)
    num_edge = cal_edge(list_adj, node, 1)
    print(num_edge)

if __name__ == "__main__":
    boj2606()