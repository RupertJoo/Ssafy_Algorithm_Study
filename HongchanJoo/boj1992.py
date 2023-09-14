import sys
input = sys.stdin.readline
print = sys.stdout.write

def quad(arr, n, r_start, c_start, r_end, c_end):
    if n:
        cnt_b = 0
        cnt_w = 0
        for r in range(r_start, r_end):
            for c in range(c_start, c_end):
                if arr[r][c]:
                    cnt_b += 1
                else:
                    cnt_w += 1
        if (r_end - r_start) * (c_end - c_start) == cnt_b:
            print("1")
        elif (r_end - r_start) * (c_end - c_start) == cnt_w:
            print("0")
        else:
            r_mid = (r_start + r_end) // 2
            c_mid = (c_start + c_end) // 2
            print("(")
            quad(arr, n // 2, r_start, c_start, r_mid, c_mid)
            quad(arr, n // 2, r_start, c_mid, r_mid, c_end)
            quad(arr, n // 2, r_mid, c_start, r_end, c_mid)
            quad(arr, n // 2, r_mid, c_mid, r_end, c_end)
            print(")")



def boj1992():
    n = int(input())
    arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    quad(arr, n, 0, 0, n, n)
    print("\n")

if __name__ == "__main__":
    boj1992()