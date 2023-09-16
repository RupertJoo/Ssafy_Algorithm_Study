from collections import deque

def boj1697():
    n, m = map(int, input().split())
    cnt = 0

    set_n = set()
    set_n.add(n)

    q = deque()
    q.append((n, cnt))

    while q:
        nc_now = q.popleft()
        n_now, c = nc_now[0], nc_now[1]

        if n_now == m:
            print(c)
            break
        else:
            for n_nxt in (n_now - 1, n_now + 1, 2 * n_now):
                if 0 <= n_nxt <= 1e5 and not set_n.__contains__(n_nxt):
                    q.append((n_nxt, c + 1))
                    set_n.add(n_nxt)
        print(q)




if __name__ == "__main__":
    boj1697()
