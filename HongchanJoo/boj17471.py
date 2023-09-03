def dividable(v, visited, villages, list_adj):
    q = [v]
    while q:
        v_now = q.pop(0)
        for v_nxt in list_adj[v_now]:
            if v_nxt not in visited and v_nxt in villages:
                visited.append(v_nxt)
                q.append(v_nxt)
    return True if len(visited) == len(villages) else False


def boj17471():
    n = int(input())
    list_population = [0] + list(map(int, input().split()))
    list_adj = [[] for _ in range(n + 1)]
    ans = 1000
    for s in range(1, n + 1):
        se = list(map(int, input().split()))
        for i_e in range(1, se[0] + 1):
            e = se[i_e]
            list_adj[s].append(e)
    for i in range(1, (1 << n) - 1):
        a = []
        village_all = set(range(1, n + 1))
        for j in range(n):
            if i & (1 << j):
                a.append(j + 1)
        b = list(village_all.difference(set(a)))
        if dividable(a[0], [a[0]], a, list_adj) and dividable(b[0], [b[0]], b, list_adj):
            sum_a = 0
            for aa in a:
                sum_a += list_population[aa]
            sum_b = 0
            for bb in b:
                sum_b += list_population[bb]
            ans = min(ans, abs(sum_a - sum_b))
    print(ans if ans != 1000 else -1)


if __name__ == "__main__":
    boj17471()