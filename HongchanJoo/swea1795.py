from collections import deque

def cal_distance(v_start, v_end, lst_adj):
    dist = float("inf")
    visited = 1 << v_start
    q = deque([[v_start, 0, visited]])
    while q:
        v_now, dist_now, visited = q.popleft()
        # print(v_now, dist_now, visited)
        if dist <= dist_now:
            continue
        if v_now == v_end:
            if dist > dist_now:
                dist = dist_now
            continue
        for v_nxt, d_nxt in lst_adj[v_now]:
            if v_nxt != v_start and not visited & 1 << v_nxt:
                # print(f"i ll push v_nxt{v_nxt}  d_nxt{d_nxt}")
                q.append([v_nxt, dist_now + d_nxt, visited + 1 << v_nxt])
    # print(f"dist = {dist}")
    return dist




def swea1795():
    for tc in range(1, int(input()) + 1):
        n, m, goal = map(int, input().split())
        lst_adj = [[] for _ in range(n + 1)]
        distances = [0] * (n + 1)
        for i in range(m):
            x, y, c = map(int, input().split())
            lst_adj[x].append([y, c])
        # print(*lst_adj)
        for i in range(1, n + 1):
            distances[i] = cal_distance(i,goal,lst_adj) + cal_distance(goal,i,lst_adj)
            # print(f"{i}th {distances[i]}")
        print(f"#{tc} {max(distances)}")
if __name__ == "__main__":
    swea1795()
