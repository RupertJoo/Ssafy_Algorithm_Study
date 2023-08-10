dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 0: 이동 가능한 칸
# 1: 벽
# 3: 도착점

arr = [[0, 0, 0, 0, 1, 3],
       [1, 0, 1, 0, 1, 3],
       [0, 0, 0, 0, 1, 3],
       [0, 1, 0, 0, 1, 0],
       [0, 1, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0]]

# r: 행 번호
# c: 열 번호
# n: 한 변의 길이

def dfs(r, c, n):
    visited = [[0] * n for _ in range(n)]
    stack = []
    visited[r][c] = 1

    while True:
        # 현재 위치가 도착점인지 확인
        if arr[r][c] == 3:
            print("도착")
            break
        # 현재 위치 (r, c)에서 다음 위치로 이동 가능한가?
        # 이동 가능하다면 간다.
        for i in range(4):
            # 다음위치 계산
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and not arr[nr][nc]:
                # 위치 확인 후 돌아올 위치(현재 위치)를 스택에 저장
                stack.append((r, c))
                # 방문 체크
                visited[nr][nc] = 1
                r, c = nr, nc
                break
            #  4 방향 중 어느곳도 갈 수 없다면?
            else:
                # 내가 저장해둔 최근 위치로 돌아가기
                r, c = stack.pop()
                else

