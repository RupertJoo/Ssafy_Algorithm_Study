def boj7568():
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    entry = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j and arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
                entry[i] += 1

    print(*entry)


if __name__ == "__main__":
    boj7568()

