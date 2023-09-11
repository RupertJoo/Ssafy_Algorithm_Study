def boj1038():
    n = int(input())
    arr = []

    def backtracking(lst, i, m):
        if i == m:
            return
        else:
            arr.append(int("".join(map(str, lst))))
            if not range(lst[i] - 1, -1, -1):
                return
            for ii in range(lst[i] - 1, -1, -1):
                lst.append(ii)
                backtracking(lst, i + 1, m)
                lst.pop()

    for j in range(0, 10):
        backtracking([j], 0, 10)
    arr.sort()
    if n < len(arr):
        print(arr[n])
    else:
        print(-1)


if __name__ == "__main__":
    boj1038()
