# import sys
# sys.stdin = open("./refs/input_swea_1209_hw.txt")

def swea1209_hw():
    T = 10
    N = 100
    _ = input()
    for tc in range(1, T + 1):
        arr = list(list(map(int, input().split())) for _ in range(N))

        # arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
        result = 0
        # print(arr)
        for i in range(N):
            sum_values = 0
            for j in range(N):
                sum_values += arr[i][j]
            if result < sum_values:
                result = sum_values
        for j in range(N):
            sum_values = 0
            for i in range(N):
                sum_values += arr[i][j]
            if result < sum_values:
                result = sum_values
        sum_values = 0
        for j in range(N):
            sum_values += arr[j][j]
        if result < sum_values:
            result = sum_values
        sum_values = 0
        for j in range(N):
            sum_values += arr[N - j - 1][j]
        if result < sum_values:
            result = sum_values
        print(f"#{tc} {result}")
    pass

if __name__ == "__main__":
    swea1209_hw()