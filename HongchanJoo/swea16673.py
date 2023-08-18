def bfs(node, node_now, node_goal, adj_lst):
    visited = [0] * (node + 1)
    len_q = 100  # 원형큐의 크기
    q = [0] * len_q
    front = rear = 0  # 원형큐 초기 조건

    rear = (rear + 1) % len_q  # enqueue_circular
    q[rear] = node_now
    visited[node_now] = 1  # 방문처리
    while front != rear:  # 원형큐 공백 조건: front == rear
        front = (front + 1) % len_q  # dequeue_circular
        node_now = q[front]
        if node_now == node_goal:  # 목표에 도달하면
            return visited[node_now] - 1  # 최단경로를 반환.
        else:
            for node_nxt in adj_lst[node_now]:  # 다음 노드는 인접리스트의 현재노드 인덱스에
                if not visited[node_nxt]:  # 방문하지 않은 경우
                    rear = (rear + 1) % len_q  # enqueue_circular
                    q[rear] = node_nxt
                    visited[node_nxt] = visited[node_now] + 1  # 시작노드로부터 거리 + 1 값 저장
    return 0  # 경로를 찾을 수 없을 때 0을 반환.


def swea16673():
    for tc in range(1, int(input()) + 1):
        node, edge = map(int, input().split())
        adj_lst = [[] for _ in range(node + 1)]
        for _ in range(edge):  # 인접리스트 입력
            v, e = map(int, input().split())
            adj_lst[v].append(e)
            adj_lst[e].append(v)
        start, goal = map(int, input().split())
        ans = bfs(node, start, goal, adj_lst)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea16673()