def countBinarySearch(arr, len_arr, x):
    idx_start = 1
    idx_end = len_arr
    count = 0
    while idx_start <= idx_end:
        idx_middle = (arr[idx_start] + arr[idx_end]) // 2
        if arr[idx_middle] == x:
            return count
        elif arr[idx_middle] > x:
            idx_end = idx_middle - 1
        else:
            idx_start = idx_middle + 1
        count += 1
    return False


def swea16312():
    for tc in range(1, int(input()) + 1):
        p, a, b = map(int, input().split())
        arr_p = list(range(p + 1))
        count_a = countBinarySearch(arr_p, p, a)
        count_b = countBinarySearch(arr_p, p, b)
        if count_a < count_b:
            result = 'A'
        elif count_a > count_b:
            result = 'B'
        else:
            result = 0
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16312()
