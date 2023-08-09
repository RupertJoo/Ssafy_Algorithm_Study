def swea2005():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list([1] + [0] * i for i in range(n))
        for i in range(1, n):
            for j in range(1, i):
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
            arr[i][-1] = 1

        print(f"#{tc}")
        for i in arr:
            print(*i)


if __name__ == "__main__":
    swea2005()