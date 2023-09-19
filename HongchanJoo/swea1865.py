global prop_max


def cal_prop(i, n, prop, arr, selected):
    global prop_max
    if i == n:
        if prop_max < prop:
            prop_max = prop
        return
    if prop_max >= prop:
        return
    for j in range(n):
        if not selected[j]:
            selected[j] = 1
            cal_prop(i + 1, n, prop * 0.01 * arr[i][j], arr, selected)
            selected[j] = 0


def swea1865():
    for tc in range(1, int(input()) + 1):
        global prop_max
        prop_max = 0

        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        selected = [0] * n
        cal_prop(0, n, 1, arr, selected)
        prop_max *= 100
        print(f"#{tc} {prop_max:.6f}")


if __name__ == "__main__":
    swea1865()