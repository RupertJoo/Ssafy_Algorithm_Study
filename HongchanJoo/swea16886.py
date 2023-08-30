def getUsage(v, i, n, arr, selected, usage):
    global usage_min

    if i == n - 1:
        usage += arr[v][0]
        usage_min = min(usage_min, usage)
    else:
        for j in range(n):
            if not selected[j]:
                selected[j] = 1
                getUsage(j, i + 1, n, arr, selected, usage + arr[v][j])
                selected[j] = 0


def swea16886():
    global usage_min

    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        selected = [0] * n
        usage_min = 1_000_000
        selected[0] = 1
        getUsage(0, 0, n, arr, selected, 0)
        print(f"#{tc} {usage_min}")


if __name__ == "__main__":
    swea16886()

