# import sys
# sys.stdin = open("./refs/input_swea_2001.txt")

def swea2001():
    # for tc in range(1, int(sys.stdin.readline()) + 1):
    for tc in range(1, int(input()) + 1):
        N, M = map(int, input().split())
        arr = list(list(map(int, input().split())) for _ in range(N))
        result = 0
        for i in range(N):
            for j in range(N):
                value_sum = 0
                lim_r = N
                lim_c = N
                if i + M < N:
                    lim_r = i + M
                if j + M < N:
                    lim_c = j + M
                for ii in range(i, lim_r):
                    for jj in range(j, lim_c):
                        value_sum += arr[ii][jj]
                if result < value_sum:
                    result = value_sum
        print(f"#{tc} {result}")

if __name__ == "__main__":
    swea2001()