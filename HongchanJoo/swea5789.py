def swea5789():
    for tc in range(1, int(input()) + 1):
        n, q = map(int, input().split())
        arr = [0] * (n + 1)
        arr_il = list(list(map(int, input().split())) for _ in range(q))
        for ii in range(q):
            i, l = arr_il[ii]
            for iii in range(i, l + 1):
                arr[iii] = (ii + 1)
            pass
        print(f"#{tc}", *arr[1:])
    pass


if __name__ == "__main__":
    swea5789()
