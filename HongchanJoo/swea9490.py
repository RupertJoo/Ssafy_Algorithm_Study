import sys

def swea9490():
    sys.stdin = open("./refs/input_swea_9490.txt")
    for tc in range(1, int(sys.stdin.readline()) + 1):
    # for tc in range(int(input()) + 1):
        N, M = map(int, input().split())
        arr = list(list(map(int, input().split())) for _ in range(N))


        print(f"#{tc} {arr}")
        pass
if __name__ == "__main__":
    swea9490()