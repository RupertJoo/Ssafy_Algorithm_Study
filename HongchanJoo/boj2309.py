def countsort(arr):
    len_arr = len(arr)
    MAX = 100
    arr_sorted = [None] * len_arr
    count = [0] * (MAX + 1)

    for i in range(len_arr):
        count[arr[i]] += 1
    for i in range(1, MAX):
        count[i] += count[i - 1]
    for i in range(len_arr - 1, -1, -1):
        count[arr[i]] -= 1
        arr_sorted[count[arr[i]]] = arr[i]
    return arr_sorted


def boj2309():
    dwarf = list(int(input()) for _ in range(9))
    x_men = []

    for i in range(8):
        for j in range(i + 1, 9):
            x_men.append([i, j])

    for i, j in x_men:
        arr_dwarf = []
        for k in range(9):
            if k == i or k == j:
                continue
            else:
                arr_dwarf.append(dwarf[k])
        sum_dwarf = 0
        for k in arr_dwarf:
            sum_dwarf += k
        if sum_dwarf == 100:
            arr_dwarf_sorted = countsort(arr_dwarf)
            for k in arr_dwarf_sorted:
                print(k)
            break


if __name__ == "__main__":
    boj2309()