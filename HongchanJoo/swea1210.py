import sys

sys.stdin = open("./refs/input_swea_1210.txt")


def solve1210():
    t = 10
    n = 100
    for tc in range(1, t + 1):
        _ = input()
        # arr = list(list(map(int, input().split())) for _ in range(n))
        arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
        """
        move = [[1, 0], [0, -1], [0, 1]]

        print(f"#{tc}")
        for i in arr:
            print(*i)
        for result in range(n):
            r = 0
            c = result
            iter = 0
            while r < n:
                if arr[r][c] == 1:
                    r_left = r + move[1][0]
                    c_left = c + move[1][1]
                    r_right = r + move[2][0]
                    c_right = c + move[2][1]
                    r_down = r + move[0][0]
                    c_down = c + move[0][1]
                    # print(iter)
                    print(f"row = {r}, column = {c}")
                    if arr[r][c] == 2:
                        break
                    elif 0 <= r_left < n and 0 <= c_left < n and arr[r_left][r_left] == 1:
                        r = r_left
                        c = c_left
                        print(f"left, {r}, {c}")
                    elif 0 <= r_right < n and 0 <= c_right < n and arr[r_right][r_right] == 1:
                        r = r_right
                        c = c_right
                        print(f"right, {r}, {c}")
                    elif 0 <= r_down < n and 0 <= c_down < n and arr[r_down][c_down] == 1:
                        r = r_down
                        c = c_down
                        print(f"down, {r}, {c}")
                    else:
                        iter += 1
                        break
                else:
                    break

        """
        c_goal = None  # 목표의 열 선언
        for j in range(n):  # 목표의 열 찾기
            if arr[n - 1][j] == 2:
                c_goal = j
        r, c = n - 1, c_goal  # 시작점의 행과 열
        arr_visited = list([0] * n for _ in range(n))  # 방문확인 배열
        while r > 0:  # r == 0 이 될 때 while 문이 종료되도록
            arr_visited[r][c] = 1
            if c - 1 >= 0 and arr[r][c - 1] and arr_visited[r][c - 1] == 0:  # 좌측이동조건: 범위 내에 방문기록이 없다.
                c -= 1
            elif c + 1 < n and arr[r][c + 1] and arr_visited[r][c + 1] == 0:  # 우측이동조건: 범위 내에 방문기록이 없다.
                c += 1
            else:  # 상측이동은 좌우측 이동보다 나중에 판별되어야 한다.
                r -= 1
        result = c
        print(f"#{tc} {result}")


# if __name__ == "__main__":
#     solve1210()


# 행 번호 99(= 100 - 1)
# 열 번호 ?
# 열 번호 찾기

def solve1210_1():
    t = 10
    n = 100
    for tc in range(1, t + 1):
        _ = input()
        # arr = list(list(map(int, input().split())) for _ in range(n))
        arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

        r, c = 100 - 1, None
        for j in range(n):
            if arr[-1][j] == 2:
                c = j
                break
        # 좌우이동이 상이동보다 우선한다.
        #    좌, 우, 위 순서
        dr = [0, 0, -1]
        dc = [-1, 1, 0]

        while r > 0:
            for d in range(3):
                # 다음위치 계산
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1:
                    r = nr
                    c = nc
                    arr[r][c] = 0
                    break
        print(f"#{tc} {c}")


# if __name__ == "__main__":
    # solve1210_1()


def solve1210_2():
    t = 10
    n = 100
    for tc in range(1, t + 1):
        _ = input()
        # arr = list(list(map(int, input().split())) for _ in range(n))
        arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
        r, c = n - 1, 0
        for j in arr[-1]:
            if j == 2:
                break
            c += 1
        # print(c)
        while r >= 0:
            if 0 < c < n and arr[r][c - 1] == 1:
                c -= 1
                while c - 1 > 0 and arr[r][c - 1] == 1:
                    c -= 1
            elif 0 <= c < n - 1 and arr[r][c + 1] == 1:
                c += 1
                while c + 1 < n and arr[r][c + 1] == 1:
                    c += 1
            r -= 1
        print(f"#{tc} {c}")


if __name__ == "__main__":
    solve1210_2()