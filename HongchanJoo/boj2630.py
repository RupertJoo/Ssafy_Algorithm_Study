import sys
input = sys.stdin.readline
def boj2630():
    global cnt_white
    global cnt_blue

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt_white = 0
    cnt_blue = 0

    def splitPaper(arr, r_start, c_start, r_end, c_end):
        global cnt_white
        global cnt_blue
        if range(r_start, r_end) and range(c_start, c_end):
            # print(r_start, c_start, r_end, c_end)
            area_paper = (r_end - r_start) * (c_end - c_start)
            c_w = 0
            c_b = 0
            for r in range(r_start, r_end):
                for c in range(c_start, c_end):
                    if not arr[r][c]:
                        c_w += 1
                    else:
                        c_b += 1
            if c_w == area_paper:
                cnt_white += 1
            elif c_b == area_paper:
                cnt_blue += 1
            else:
                splitPaper(arr, r_start, c_start,  (r_start + r_end) // 2, (c_start + c_end) // 2)
                splitPaper(arr, r_start, (c_start + c_end) // 2, (r_start + r_end) // 2, c_end)
                splitPaper(arr, (r_start + r_end) // 2, c_start, r_end, (c_start + c_end) // 2)
                splitPaper(arr, (r_start + r_end) // 2, (c_start + c_end) // 2, r_end, c_end)
        else:
            return
    splitPaper(arr, 0, 0, n, n)
    print(cnt_white)
    print(cnt_blue)


if __name__ == "__main__":
    boj2630()