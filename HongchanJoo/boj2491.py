def boj2491():
    n = int(input())
    arr = list(map(int, input().split()))

    max_ascend = 1
    count_ascend = 1
    i_ascend = 0

    max_descend = 1
    count_descend = 1
    i_descend = 0

    while i_ascend < n - 1:
        if arr[i_ascend] <= arr[i_ascend + 1]:
            count_ascend += 1
        else:
            count_ascend = 1
        if max_ascend <= count_ascend:
            max_ascend = count_ascend
        i_ascend += 1

    while i_descend < n - 1:
        if arr[i_descend] >= arr[i_descend + 1]:
            count_descend += 1
        else:
            count_descend = 1
        if max_descend <= count_descend:
            max_descend = count_descend
        i_descend += 1

    print(max(max_ascend, max_descend))


if __name__ == "__main__":
    boj2491()


