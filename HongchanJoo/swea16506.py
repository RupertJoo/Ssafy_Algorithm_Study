def dfs(s, node, g):
    visited = [0] * (node + 1)
    stack = []
    i = s
    visited[i] = 1

    while True:
        for j in adj_l[i]:
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

    pass

def swea16506():
    global adj_l
    for tc in range(1, int(input()) + 1):
        node, edge = map(int, input().split())  # node: 노드의 갯수, edge: 간선의 갯수
        adj_l = [[] for _ in range(node + 1)]  # 0 ~ v 까지의 연결리스트 생성
        for _ in range(edge):
            node_start, node_end = map(int, input().split())
            adj_l[node_start].append(node_end)
        # print(f"#{tc}")
        # for i in adj_l:
        #     print(i)
        s, g = map(int, input().split())
        print(f"#{tc} {dfs(s, node, g)}")


if __name__ == "__main__":
    swea16506()