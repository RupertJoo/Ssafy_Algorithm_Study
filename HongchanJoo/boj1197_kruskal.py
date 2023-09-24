from sys import stdin
input = stdin.readline


def find_set(x, parents):
    if parents[x] == x:
        return parents[x]
    return find_set(parents[x], parents)


def union(x, y, parents):
    px = find_set(x, parents)
    py = find_set(y, parents)
    if px == py:
        return parents
    if px < py:
        parents[py] = px
    else:
        parents[px] = py
    return parents


def boj1197():
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(v + 1)]

    cnt = 0
    sum_weight = 0
    for f, t, w in edges:
        if find_set(f, parents) != find_set(t, parents):
            cnt += 1
            sum_weight += w
            parents = union(f, t, parents)
            if cnt == v:
                break
    print(sum_weight)



if __name__ == "__main__":
    boj1197()

