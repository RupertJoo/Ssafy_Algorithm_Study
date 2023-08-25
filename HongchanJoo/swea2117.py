import sys
sys.stdin = open("./refs/sample_input_2117.txt", "r")
'''
def countHouse(r_now, c_now, i):
    global n
    global m
    global arr
    global list_cost
    global list_house
    global arr_visited
    global move
    global coord_rc

    if i == n:
        pass
    else:
        for dr, dc in move:
            r_new = r_now + dr
            c_new = c_now + dc
            if 0 <= r_new < n and 0 <= c_new < n and (not arr_visited[r_new][c_new]):
                coord_rc.append([r_new, c_new])
                list_house[i + 1] += arr[r_new][c_new]
                arr_visited[r_new][c_new] = 1
                countHouse(r_new, c_new, i + 1)


def swea2117():
    global n
    global m
    global arr
    global list_cost
    global list_house
    global arr_visited
    global move
    global coord_rc

    move = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    for tc in range(1, int(input()) + 1):
    # for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]
        list_cost = list(map(lambda x: x ** 2 + (x - 1) * (x - 1), range(0, n + 1)))

        # for a in arr:
        #     print(*a)

        for r in range(n):
            for c in range(n):
                arr_visited = [[0] * n for _ in range(n)]
                list_house = [0] * (n + 1)
                arr_visited[r][c] = 1
                list_house[1] += arr[r][c]
                coord_rc = []
                coord_rc.append([r,c])
                countHouse(r, c, 1)

                print(f"{tc} r={r},c={c}{list_house}")
                print(f"{tc} r={r},c={c}{coord_rc}")

        # for house in list_house[::-1]:
        #     if house >= 0:
        #         break
        # print(f"{tc} {house}")



if __name__ == "__main__":
    swea2117()
'''
cost = [k * k + (k - 1) * (k - 1) for k in range(40)]

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_count = 0
    home_lst = []
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1:
                home_lst.append((r, c))
    for r in range(n):
        for c in range(n):
            dist = [0] * 40  # 거리가 k일 때 포함되는 점의 갯수
            for hr, hc in home_lst:
                # 거리 계산
                k = abs(r - hr) +abs(c - hc) + 1
                dist[k] += 1
            for k in range(1, 40):
                dist[k] += dist[k - 1]
                # 손해가 아니기만 하면 된다!
                if cost[k] <= dist[k] * m:
                    max_count = max(max_count, dist[k])
    print(f"#{tc} {max_count}")