def bfs(now, adj_lst, num_people):
    visited = [0] * (num_people + 1)
    len_q = 100
    q = [0] * len_q
    front = rear = 0

    rear = (rear + 1) % len_q
    q[rear] = now
    visited[now] = 1

    while front != rear:
        front = (front + 1) % len_q
        now = q[front]
        for nxt in adj_lst[now]:
            if not visited[nxt]:
                rear = (rear + 1) % len_q
                q[rear] = nxt
                visited[nxt] = visited[now] + 1
    ans = 0
    ans_i = None
    for i in range(num_people + 1):
        if ans <= visited[i]:
            ans = visited[i]
            ans_i = i
    return ans_i

import sys
sys.stdin = open("./refs/input_swea_1238.txt")

def swea1238():
    num_people = 100
    for tc in range(1, 10 + 1):
        len_data, start = map(int, input().split())
        data = list(map(int, input().split()))
        adj_lst = [set() for _ in range(num_people + 1)]

        for i in range(len_data // 2):
            adj_lst[data[2 * i]].add(data[2 * i + 1])
        ans = bfs(start, adj_lst, num_people)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1238()