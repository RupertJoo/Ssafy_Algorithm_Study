def swea16348():
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        arr_str = list(input() for _ in range(n))
        result = None
        half_m = m // 2
        is_break = False

        for i in range(n):
            for j in range(n - m + 1):
                str_part = ''
                for k in range(m):
                    str_part += arr_str[i][j + k]
                is_palin = True
                for k in range(half_m):
                    if str_part[k] != str_part[m - k - 1]:
                        is_palin = False
                        break
                if is_palin:
                    result = str_part
                    is_break = True
                    break
            if is_break:
                break

        if not is_palin:
            is_palin = True
            for j in range(n):
                for i in range(n - m + 1):
                    str_part = ''
                    for k in range(m):
                        str_part += arr_str[i + k][j]
                        is_palin = True
                    for k in range(half_m):
                        if str_part[k] != str_part[m - k - 1]:
                            is_palin = False
                            break
                    if is_palin:
                        result = str_part
                        is_break = True
                        break
                if is_break:
                    break

        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16348()