import copy
global min_cord
global max_cntt
def design(cord, cnt, n, arr, mexynos, move, cntt):
    global min_cord
    global max_cntt

    if min_cord < cord:
        return
    if cntt == n:
        print(f"cnt:{cnt} cntt:{cntt}")
        if max_cntt < cnt:
            max_cntt = cnt
            min_cord = cord
        elif min_cord > cord:
            min_cord = cord
        return


    for dr, dc in move:
        r_now, c_now = mexynos[cnt]
        arr_copy = copy.deepcopy(arr)
        arr_copy1 = copy.deepcopy(arr)
        cord_copy = cord
        r_nxt, c_nxt = r_now + dr, c_now + dc
        is_bt = True
        while 0 <= r_nxt < n and 0 <= c_nxt < n:
            if not arr_copy[r_nxt][c_nxt]:
                arr_copy[r_nxt][c_nxt] = 2
                cord_copy += 1
            else:
                is_bt = False
                break
            r_now, c_now = r_nxt, c_nxt
            r_nxt, c_nxt = r_now + dr, c_now + dc
        if is_bt:
            design(cord_copy, cnt + 1, n, arr_copy, mexynos, move, cntt + 1)
        if is_bt:
            design(cord_copy, cnt, n, arr_copy1, mexynos, move, cntt + 1)


def swea1767():
    global min_cord
    global max_cntt
    max_cntt = 0
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        mexynos = []
        for r in range(n):
            for c in range(n):
                if arr[r][c]:
                    mexynos.append([r, c])
        min_cord = 144
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        design(0, 0, n, arr, mexynos, move, 0)
        print(f"#{tc} {min_cord}")


if __name__ == "__main__":
    swea1767()