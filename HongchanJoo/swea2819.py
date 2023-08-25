import sys
sys.stdin = open("./refs/sample_input_2819.txt", "r")

def getValue(r_now, c_now, i, n, sum_rc):
    global size
    global arr
    global size
    global set_rc
    global move

    if i == n:  # 종료조건
        # print(sum_rc)
        set_rc.add(sum_rc)
    else:  # 재귀호출
        for dr, dc in move:
            r_new = r_now + dr
            c_new = c_now + dc
            if 0 <= r_new < size and 0 <= c_new < size:
                getValue(r_new, c_new, i + 1, n, sum_rc + str(arr[r_new][c_new]))



def swea2819():
    global size
    global arr
    global size
    global set_rc
    global move

    move = [[1, 0], [-1, 0], [0, -1], [0, 1]]
    size = 4
    for tc in range(1, int(input()) + 1):
        arr = [list(map(int, input().split())) for _ in range(size)]
        set_value = set()
        set_rc = set()
        for r in range(size):
            for c in range(size):
                getValue(r, c, 0, 6, str(arr[r][c]))

        ans = len(set_rc)
        # print(set_rc)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea2819()