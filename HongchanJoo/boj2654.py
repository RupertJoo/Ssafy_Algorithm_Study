def calDist(n, m, azi_i, dist_i, azi, dist):
    move_ccw = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    dist_min_ccw = 0
    move_cw = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dist_min_cw = 0

    if azi == 1:
        r, c = 0, dist
    elif azi == 2:
        r, c = dist, 0
    elif azi == 3:
        r, c = m - 1, dist
    elif azi == 4:
        r, c = dist, n - 1

    azi_ccw = azi
    is_break = False

    if (azi_ccw % 4) == (azi_i % 4) and dist == dist_i:
        pass
    else:
        for _ in range(4):
            r_nxt = r + move_ccw[azi_ccw % 4][0]
            c_nxt = c + move_ccw[azi_ccw % 4][1]
            while 0 <= r_nxt < m and 0 <= c_nxt < n:
                if ((azi_ccw % 4) % 2) == 0:
                    if r_nxt == dist_i:
                        is_break = True
                        break
                else:
                    if c_nxt == dist_i:
                        is_break = True
                        break
                r = r_nxt
                c = c_nxt
                r_nxt = r + move_ccw[azi_ccw % 4][0]
                c_nxt = c + move_ccw[azi_ccw % 4][1]
                dist_min_ccw += 1
            if is_break:
                 break
            azi_ccw = (azi_ccw + 1) % 4
            continue


    azi_cw = azi
    is_break = False

    if (azi_cw % 4) == (azi_i % 4) and dist == dist_i:
        pass
    else:
        for _ in range(4):
            r_nxt = r + move_ccw[azi_cw % 4][0]
            c_nxt = c + move_ccw[azi_cw % 4][1]
            while 0 <= r_nxt < m and 0 <= c_nxt < n:
                if ((azi_cw % 4) % 2) == 0:
                    if r_nxt == dist_i:
                        is_break = True
                        break
                else:
                    if c_nxt == dist_i:
                        is_break = True
                        break
                r = r_nxt
                c = c_nxt
                r_nxt = r + move_ccw[azi_cw % 4][0]
                c_nxt = c + move_ccw[azi_cw % 4][1]
                dist_min_ccw += 1
            if is_break:
                 break
            azi_cw = (azi_cw - 1) % 4
            continue

    if dist_min_cw > dist_min_ccw:
        dist_min = dist_min_ccw
    else:
        dist_min = dist_min_cw

    return dist_min_ccw


def boj2654():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(int(input()))]
    azi, dist = map(int, input().split())

    # print(arr)
    # print(azi, dist)

    ans = 0
    for azi_i, dist_i in arr:
        x = calDist(n, m, azi_i, dist_i, azi, dist)
        print(x)
        ans += x

        # print(azi_i, dist_i)
    print(ans)

if __name__ == "__main__":
    boj2654()


