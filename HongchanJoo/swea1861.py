for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_count = 0
    max_start = 0
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for p in range(n):
        for q in range(n):
            i, j = p, q
            cnt = 1
            start = [i][j]
            while True:
                for di, dj in move:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < n and arr[i][j] +1 == arr[ni][nj]:



