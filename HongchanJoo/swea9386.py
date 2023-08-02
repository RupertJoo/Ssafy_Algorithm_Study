import sys
# sys.stdin = open("./refs/input_swea_9386.txt")

def swea9386():
    # for tc in range(1, int(sys.stdin.readline()) + 1):
    for tc in range(1, int(input()) + 1):
        N = int(input())
        binary = list(map(int, list(input())))
        # print(binary)
        result = 0
        for i in range(N):
            num_1 = 0
            for j in range(i, N):
                if binary[j] == 1:
                    num_1 += 1
                else:
                    break
            if result < num_1:
                result = num_1
        print(f"#{tc} {result}")

if __name__ == "__main__":
    swea9386()