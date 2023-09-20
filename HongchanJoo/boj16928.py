from collections import deque


def bfs(ladders, snakes):
    q = deque()
    visited = 1 << 1
    q.append(1)
    counts = [0] * 101
    while q:
        now = q.popleft()
        if now == 100:
            return counts[now]
        for i in range(1, 7):
            nxt = now + i
            if nxt <= 100 and not visited & 1 << nxt:
                # if nxt in ladders.keys():
                if ladders.get(nxt, 0):
                    nxt = ladders[nxt]
                # if nxt in snakes.keys():
                if snakes.get(nxt, 0):
                    nxt = snakes[nxt]
                if not visited & 1 << nxt:
                    visited += 1 << nxt
                    counts[nxt] = counts[now] + 1
                    q.append(nxt)


def boj16928():
    n, m = map(int, input().split())
    ls = [[] for _ in range(101)]
    ladders = {}
    snakes = {}
    for _ in range(n):
        x, y = map(int, input().split())
        ladders[x] = y
    for _ in range(m):
        u, v = map(int, input().split())
        snakes[u] = v

    cnt_min = bfs(ladders, snakes)
    print(cnt_min)


if __name__ == "__main__":
    boj16928()

