def maze(arr, n, r_now, c_now, r_goal, c_goal):
    stack = []
    visited = [[0] * n for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    # if not visited[r_start][c_start]:
    #     visited[r_now][c_now] = 1
    while True:
        if r_now == r_goal and c_now == c_goal:
            return 1
        else:
            if not visited[r_now][c_now]:
                visited[r_now][c_now] = 1
        for i in range(4):
            r_nxt = r_now + dr[i]
            c_nxt = c_now + dc[i]
            if 0 <= r_nxt < n and 0 <= c_nxt < n and arr[r_nxt][c_nxt] != 1 and not visited[r_nxt][c_nxt]:
                stack.append([r_now, c_now])
                visited[r_nxt][c_nxt] = 1
                r_now = r_nxt
                c_now = c_nxt
                break
        else:
            if stack:
                r_now, c_now = stack.pop()
            else:
                return 0
    return 0


def swea16532():
    for tc in range(1, int(input()) + 1):
        result = None
        n = int(input())
        arr = [list(map(int, input())) for _ in range(n)]

        # for i in arr:
        #     print(*i)
        for r in range(n):
            for c in range(n):
                if arr[r][c] == 2:
                    r_start, c_start = r, c
                elif arr[r][c] == 3:
                    r_goal, c_goal = r, c
                else:
                    continue
        result = maze(arr, n, r_start, c_start, r_goal, c_goal)
        # print(f"start r: {r_start},c: {c_start} // goal r: {r_goal}, c: {c_goal}")
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16532()