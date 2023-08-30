def calScore(r, c, n, arr, arr_v):
        if r == n - 1 and c == n - 1:
            return
        else:
            move = [[1, 0], [0, 1]]
            for dr, dc in move:
                r_nxt = r + dr
                c_nxt = c + dc
                if 0 <= r_nxt < n and 0 <= c_nxt < n:
                    arr_v[r_nxt][c_nxt] = min(arr_v[r_nxt][c_nxt], arr_v[r][c] + arr[r_nxt][c_nxt])
                    calScore(r_nxt, c_nxt, n, arr, arr_v)



def swea16883():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        arr_v = [[250] * n for _ in range(n)]
        arr_v[0][0] = arr[0][0]
        # for a  in arr:
        #     print(*a)
        calScore(0, 0, n, arr, arr_v)
        print(f"#{tc} {arr_v[n - 1][n - 1]}")


if __name__ == "__main__":
    swea16883()