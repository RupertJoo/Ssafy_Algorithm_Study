# import sys
# sys.stdin = open("./refs/intput_swea_11092.txt")

def swea11092():
    # for tc in range(1, int(sys.stdin.readline()) + 1):
    for tc in range(1, int(input()) + 1):
        N = int(input())
        values = list(map(int, input().split()))
        v_min = 11
        v_max = 0
        i_min = 0
        i_max = 0
        for i in range(N):
            if v_min > values[i]:
                v_min = values[i]
                i_min = i
        for i in range(N - 1, -1, -1):
            if v_max < values[i]:
                v_max = values[i]
                i_max = i
        result = i_max - i_min
        if result < 0: result *= -1
        print(f"#{tc} {result}")
    pass

if __name__ == "__main__":
    swea11092()