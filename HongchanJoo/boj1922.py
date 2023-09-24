from sys import stdin
input = stdin.readline


def find_set(x,parents):
    if x == parents[x]:
        return parents[x]
    return find_set(parents[x], parents)


def union (x, y, parents):
    px = find_set(x, parents)
    py = find_set(y, parents)
    if px == py:
        return parents
    if px < py:
        parents[py] = px
    else:
        parents[px] = py
    return parents


def boj1922():
    n = int(input())
    m = int(input())
    parents = [i for i in range(n + 1)]
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x:x[2])

    cnt = 0
    cost = 0
    for f, t, w in edges:
        if find_set(f, parents) != find_set(t, parents):
            cnt += 1
            cost += w
            parents = union(f, t, parents)
            if cnt == n:
                break
    print(cost)


if __name__ == "__main__":
    boj1922()