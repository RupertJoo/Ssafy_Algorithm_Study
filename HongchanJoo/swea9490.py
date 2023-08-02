# import sys
# sys.stdin = open("./refs/input_swea_9490.txt")
def swea9490():
    # for tc in range(1, int(sys.stdin.readline()) + 1):
    for tc in range(1, int(input()) + 1):
        N, M = map(int, input().split())
        arr = list(list(map(int, input().split())) for _ in range(N))
        list_dr = [-1, 1, 0, 0]
        list_dc = [0, 0, -1, 1]
        result = 0
        for i in range(N):
            for j in range(M):
                value_sum = arr[i][j]
                for k in range(1, value_sum + 1): # 반복문의 순서에 따라 전혀 다른 답이 나오는걸 유념하자!
                    for dr, dc in zip(list_dr, list_dc):
                        nr = i + k * dr
                        nc = j + k * dc
                        if 0 <= nr < N and 0 <= nc < M:
                            value_sum += arr[nr][nc]
                # print(f"{i}행, {j}열 sum {value_sum}")
                if result < value_sum:
                    result = value_sum
        print(f"#{tc} {result}")
        pass
if __name__ == "__main__":
    swea9490()