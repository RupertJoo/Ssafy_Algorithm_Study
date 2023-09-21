from collections import deque


def bfs(a, b):
    q = deque([a])
    visited = {a: 1}
    while q:
        a_now = q.popleft()
        if a_now == b:
            return visited[a_now]
        for a_nxt in (a_now * 2, a_now * 10 + 1):
            if a_nxt <= b and not visited.get(a_nxt, 0):
                visited[a_nxt] = visited[a_now] + 1
                q.append(a_nxt)
    return -1


def boj16953():
    a, b = map(int, input().split())
    print(bfs(a, b))


if __name__ == "__main__":
    boj16953()