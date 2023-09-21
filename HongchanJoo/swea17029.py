from collections import deque
from heapq import heappush
from heapq import heappop
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dijkstra():
    q = deque()
    fuel[0][0]= 0

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    fuel = [[float("inf")] * n for _ in range(n)]