from heapq import heappush
from heapq import heappop
from sys import stdin
input = stdin.readline


def get_mst(graph):
    heap = []
    mst = 0
    heappush(heap, [0, 1])
    sum_weight = 0

    while heap:
        weight, v_now = heappop(heap)
        if mst & 1 << v_now:
            continue
        mst += 1 << v_now
        sum_weight += weight
        for v_nxt in graph[v_now].keys():
            if not graph[v_now].get(v_nxt, 0) or 1 & 1 << v_nxt:
                continue
            heappush(heap, [graph[v_now][v_nxt], v_nxt])
    return sum_weight


def boj1197():
    v, e = map(int, input().split())
    graph = [{} for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    ans = get_mst(graph)
    print(ans)


if __name__ == "__main__":
    boj1197()

