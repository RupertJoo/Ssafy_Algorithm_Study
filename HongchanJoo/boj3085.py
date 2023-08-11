import sys
'''
def count_candy(arr, n):
    global arr_num
    for r in range(n):
        for c in range(n):
            color = arr[r][c]

            num_up = [0, 0, 0, 0]
            for k in range(r, -1, -1):
                if arr[k][c] == color:
                    num_up[0] += 1
                else:
                    break
            for k in range(r, n):
                if arr[k][c] == color:
                    num_up[1] += 1
                else:
                    break
            for k in range(c, -1, -1):
                if arr[r][k] == color:
                    num_up[2] += 1
                else:
                    break
            for k in range(c, n):
                if arr[r][k] == color:
                    num_up[3] += 1
                else:
                    break
            max_candy = 0
            for k in num_up:
                if max_candy < k:
                    max_candy = k
            if arr_num[r][c] < max_candy:
                arr_num[r][c] = max_candy
'''


def count_candy(arr, rc, n):
    global arr_num
    r = rc[0]
    c = rc[1]
    if 0 <= r < n and 0 <= c < n:
        color = arr[r][c]
        num_up = [0, 0, 0, 0]
        for k in range(r, -1, -1):
            if arr[k][c] == color:
                num_up[0] += 1
            else:
                break
        for k in range(r, n):
            if arr[k][c] == color:
                num_up[1] += 1
            else:
                break
        for k in range(c, -1, -1):
            if arr[r][k] == color:
                num_up[2] += 1
            else:
                break
        for k in range(c, n):
            if arr[r][k] == color:
                num_up[3] += 1
            else:
                break
        max_candy = 0
        for k in num_up:
            if max_candy < k:
                max_candy = k
        if arr_num[r][c] < max_candy:
            arr_num[r][c] = max_candy

def boj3085():
    global arr_num
    n = int(sys.stdin.readline())
    arr = list(list(sys.stdin.readline()) for _ in range(n))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    arr_num = list([0] * n for _ in range(n))

    for r in range(n):
        for c in range(n):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < n and 0 <= nc < n and arr[r][c] != arr[nr][nc]:
                    rc = (r, c)
                    arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                    count_candy(arr, rc, n)
                    arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
    max_arr = 0
    for r in range(n):
        for c in range(n):
            if max_arr < arr_num[r][c]:
                max_arr = arr_num[r][c]
    for i in arr_num:
         print(*i)
    sys.stdout.write(str(max_arr))


if __name__ == "__main__":
    boj3085()