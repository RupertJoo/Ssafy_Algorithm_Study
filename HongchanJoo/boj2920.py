def boj2920():
    lst = list(map(int, input().split()))

    is_ascending = True
    for i in range(1, len(lst)):
        if lst[i - 1] >= lst[i]:
            is_ascending = False
            break
    is_descending = True
    for i in range(1, len(lst)):
        if lst[i - 1] <= lst[i]:
            is_descending = False
            break
    if is_ascending:
        print("ascending")
    elif is_descending:
        print("descending")
    else:
        print("mixed")


if __name__ == "__main__":
    boj2920()

