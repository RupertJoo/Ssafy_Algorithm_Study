import sys
global min_cost
sys.stdin = open("./refs/input_swea_16979.txt")

def calCost(i, n, selected, arr, cost):
    global min_cost
    if i == n:
        if min_cost > cost:
            min_cost = cost
            return
    if cost > min_cost:
        return
    for j in range(n):
        if not selected[j]:
            selected[j] = 1
            calCost(i + 1, n, selected, arr, cost + arr[i][j])
            selected[j] = 0


def swea16979():
    for tc in range(1, int(input()) + 1):
        global min_cost
        n = int(input())
        arr= [list(map(int, input().split())) for _ in range(n)]
        # for a in arr:
        #     print(*a)
        min_cost = n * 99
        selected = [0] * n
        calCost(0, n, selected, arr, 0)
        print(f"#{tc} {min_cost}")

if __name__ == "__main__":
    swea16979()