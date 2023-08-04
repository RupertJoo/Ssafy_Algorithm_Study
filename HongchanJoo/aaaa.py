import sys
sys.stdin = open("./refs/input_swea_1210.txt.txt")
for iii in range(10):
    tc = iii + 1
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착점 먼저 찾기(서칭 시작점 선정)
    # 배열 마지막 라인에서 2를 찾는다
    for c in range(100):
        if ladder[99][c] == 2:
            sc = c
    dr = [0, 0, -1] # d[0]좌 d[1]우 d[2]상
    dc = [-1, 1, 0]

    # 시작점 : ladder[99][sc] tc 1의 경우 [99][57]
    r, c = 99, sc  # 시작점 설정

    # 출발점을 찾아 올라간다
    # 1. 올라가다가 2-1. 좌,우의 값이 1이 발견되는 경우 좌, 우로 이동 2-2. 없을경우 위로.
    while r > 0: # row = 0이 될 때 break. 그전엔 계속 반복
        for d in range(2): # 주변 좌, 우 체크
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 100 and 0<= nc < 100:
                if ladder[nr][nc] == 1: # 1. 좌, 우 중 하나가 1인 경우--> 해당 방향으로 이동
                    while True: # 해당 방향으로 계속 이동
                        nr = r + dr[d]
                        nc = c + dc[d]
                        r, c = nr, nc
                        # print(f" nr = {nr} nc = {nc} / {ladder[nr][nc]}")
                        if d == 0 and ladder[nr][nc] == 0: # 좌측으로 이동하다 0을 만난 경우
                            c += 1
                            nr = r + dr[2]
                            nc = c + dc[2]
                            r, c = nr, nc
                            # print(f" nr = {nr} nc = {nc} / {ladder[nr][nc]}")
                            break
                        elif d == 1 and ladder[nr][nc] == 0: # 우측으로 이동하다 0을 만난 경우
                            c -= 1
                            nr = r + dr[2]
                            nc = c + dc[2]
                            r, c = nr, nc
                            # print(f" nr = {nr} nc = {nc} / {ladder[nr][nc]}")
                            break
                else: # 2. 좌, 우 값이 0인 경우 --> 위로 이동. d[2]
                        nr = r + dr[2]
                        nc = c + dc[2]
                        r, c = nr, nc
                        # print(f" nr = {nr} nc = {nc} / {ladder[nr][nc]}")
    print(f"#{tc} {nc}")