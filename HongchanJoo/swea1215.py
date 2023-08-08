def swea1215():
    t = 10
    n = 8
    for tc in range(1, t + 1):
        m = int(input())
        half_m = m // 2
        arr = list(input() for _ in range(n))
        result = 0

        for i in range(n):
            for j in range(n - m + 1):
                palin = ''
                for k in range(m):
                    palin += arr[i][j + k]
                is_palin = True
                for k in range(half_m):
                    if palin[k] != palin[m - k - 1]:
                        is_palin = False
                        break
                if is_palin:
                    result += 1
        if m > 1:
            for j in range(n):
                for i in range(n - m + 1):
                    palin = ''
                    for k in range(m):
                        palin += arr[i + k][j]
                    is_palin = True
                    for k in range(half_m):
                        if palin[k] != palin[m - k - 1]:
                            is_palin = False
                            break
                    if is_palin:
                        result += 1

        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea1215()