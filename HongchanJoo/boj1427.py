def countsort_rev(arr):
    MAX = 9
    len_arr = len(arr)
    count = [0] * (MAX + 1)
    arr_sorted = [None] * len_arr

    for i in range(len_arr):
        count[arr[i]] += 1
    for i in range(1, MAX +1):
        count[i] += count[i - 1]
    for i in range(len_arr - 1, -1, -1):
        count[arr[i]] -= 1
        arr_sorted[count[arr[i]]] = arr[i]
    arr_sorted_rev = arr_sorted[::-1]
    arr_sorted_rev = list(map(str, arr_sorted_rev))
    return arr_sorted_rev
def boj1427():
    arr = list(map(int, list(input())))
    # print(*arr)
    arr_sorted_rev = countsort_rev(arr)
    print(''.join(arr_sorted_rev))

if __name__ == "__main__":
    boj1427()