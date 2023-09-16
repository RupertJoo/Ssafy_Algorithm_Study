from collections import deque

def boj1697():
    n, m = map(int, input().split())
    q = deque()
    set_n = set()
    cnt = 0
    q.append((n, cnt))
    set_n.add(n)
    while q:
        n_now = q.popleft()
        if n_now[0] == m:
            break
        else:
            for n_nxt0 in (n_now[0] - 1, n_now[0] + 1, 2 * n_now[0]):
                if not set_n.__contains__(n_nxt0):
                    q.append((n_nxt0, n_now[1] + 1))
        print(q)
    print(n_now[1])


if __name__ == "__main__":
    boj1697()
