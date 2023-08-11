def swea2805():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list(list(map(int, input())) for _ in range(n))
        # for i in arr:
        #     print(*i)
        arr_visited = list([0] * n for _ in range(n))
        result = 0
        for r in range(n):
            if r <= n // 2:
                del_abs = r
            else:
                del_abs = n - r - 1
            for c in range(n//2 - del_abs, n// 2 + del_abs + 1):
                result += arr[r][c]
        print(f"#{tc} {result}")
        # for i in arr_visited:
        #     print(*i)


if __name__ == "__main__":
    swea2805()