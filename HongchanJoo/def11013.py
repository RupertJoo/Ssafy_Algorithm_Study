def swea11013():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list(map(int, input().split()))
        arr_idx = []
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                for k in range(j + 1, n + 1):
                    arr_idx.append([i, j, k])
        ans = 1_000_000
        for i,j,k in arr_idx:
            sum_1st = sum(arr[:i])
            sum_2nd = sum(arr[i:j])
            sum_3rd = sum(arr[j:])

            if ans >max(sum_1st,sum_2nd,sum_3rd) - min(sum_1st,sum_2nd,sum_3rd):
                ans = max(sum_1st,sum_2nd,sum_3rd) - min(sum_1st,sum_2nd,sum_3rd)
        print(*arr_idx)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea11013()
