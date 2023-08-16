def arr_permuation(i, n, sum_sub):
    global arr
    global arr_n
    global selected
    global min_sum

    if min_sum < sum_sub:  # 이 경우는 더 볼 것도 없다.
        return
    if i == n:
        if min_sum > sum_sub:  # 더 작은 배열 최소 합이 나온다면 갱신한다.
            min_sum = sum_sub
            return
    else:
        for j in range(n):
            if not selected[j]:  # 전역변수 selected는 재귀호출 될때마다 1이 채워지므로 중복을 막는다.
                selected[j] = 1
                arr_permuation(i + 1, n, sum_sub + arr[i][j])
                selected[j] = 0


def swea16586():
    for tc in range(1, int(input()) + 1):
        global arr
        global arr_n
        global selected
        global min_sum

        n = int(input())
        min_sum = 10 * n
        arr_n = list(range(n))
        selected = [0] * n
        arr = [list(map(int, input().split())) for _ in range(n)]
        arr_permuation(0, n, 0)
        print(f"#{tc} {min_sum}")


if __name__ == "__main__":
    swea16586()