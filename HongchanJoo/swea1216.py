def cal_len_palin(arr, n, r, c, k, max_len):
    if k == 0:
        palin = ""
        if r + 1 < max_len:
            return 0
        else:
            for i in range(r, -1, -1):
                palin += arr[i][c]
            len_palin = len(palin)
            while palin != palin[::-1]:
                len_palin -= 1
                palin = palin[:len_palin]
    elif k == 1:
        if n - r < max_len:
            return 0
        else:
            palin = ""
            for i in range(r, n, 1):
                palin += arr[i][c]
            len_palin = len(palin)
            while palin != palin[::-1]:
                len_palin -= 1
                palin = palin[:len_palin]
    elif k == 2:
        if c + 1 < max_len:
            return 0
        else:
            palin = ""
            for j in range(c, -1, -1):
                palin += arr[r][j]
            len_palin = len(palin)
            while palin != palin[::-1]:
                len_palin -= 1
                palin = palin[:len_palin]
    elif k == 3:
        if n - c < max_len:
            return 0
        else:
            palin = ""
            for j in range(c, n, 1):
                palin += arr[r][j]
            len_palin = len(palin)
            while palin != palin[::-1]:
                len_palin -= 1
                palin = palin[:len_palin]
    return len_palin
def swea1216():
    t = 10
    n = 100
    for tc in range(1, t + 1):
        _ = input()
        arr = list(list(input()) for _ in range(n))
        max_len = 0
        for r in range(n):
            for c in range(n):
                max_element = 0
                for k in range(4):
                    len_palin = cal_len_palin(arr, n, r, c, k, max_len)
                    if max_element < len_palin:
                        max_element = len_palin
                    # print(f"r={r}, c={c}, {max_element}")
                if max_len < max_element:
                    max_len = max_element
        print(f"#{tc} {max_len}")



if __name__ == "__main__":
    swea1216()

