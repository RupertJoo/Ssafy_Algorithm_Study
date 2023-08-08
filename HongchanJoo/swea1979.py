def swea1979():
    for tc in range(1, int(input()) + 1):
        n, kk = map(int, input().split())
        arr = list(list(map(int, input().split())) for _ in range(n))
        result = 0
        for i in range(n):
            for j in range(n - kk + 1):
                len_one = 0
                for k in range(kk):
                    if arr[i][j + k] == 0:
                        break
                    else:
                        len_one += 1
                if j + k < n - 1 and arr[i][j + k + 1] == 0 and len_one == kk:
                    result += 1
                elif j + k == n - 1 and len_one == kk:
                    result += 1


        for i in range(n - kk + 1):
            for j in range(n):
                len_one = 0
                for k in range(kk):
                    if arr[i + k][j] == 0:
                        break
                    else:
                        len_one += 1
                if i + k < n - 1 and arr[i + k + 1][j] == 0 and len_one == kk:
                    result += 1
                elif i + k == n - 1 and len_one == kk:
                    result += 1

        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea1979()