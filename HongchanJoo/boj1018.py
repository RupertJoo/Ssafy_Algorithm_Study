def boj1018():
    n, m = map(int, input().split())
    arr = list(list(input()) for _ in range(n))
    result = 50 * 50
    bw = ["BWBWBWBW", "WBWBWBWB"]
    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            arr_board = []
            for ii in range(8):
                arr_board.append(arr[i + ii][j:j + 8])
            num_arr_board_bw = 0
            num_arr_board_wb = 0
            for k in range(8):
                for b in range(8):
                    if bw[(k + 1) % 2][b] != arr_board[k][b]:
                        num_arr_board_bw += 1
                    if bw[k % 2][b] != arr_board[k][b]:
                        num_arr_board_wb += 1
            if num_arr_board_wb >= num_arr_board_bw:
                min_board = num_arr_board_bw
            else:
                min_board = num_arr_board_wb
            if result > min_board:
                result = min_board
    print(result)


if __name__ == "__main__":
    boj1018()
