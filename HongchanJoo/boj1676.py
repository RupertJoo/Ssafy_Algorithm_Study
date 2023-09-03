def boj1676():
    n = int(input())
    arr = [[0,0] for _ in range(n + 1)]
    for i in range(n, 0, -1):
        i2 = i
        n_2 = 0
        i5 = i
        n_5 = 0
        while not i2 % 2:
            i2 //= 2
            n_2 += 1
        while not i5 % 5:
            i5 //= 5
            n_5 += 1
        arr[i][0], arr[i][1] = n_2, n_5
    sum_n2, sum_n5 = 0, 0
    for n2, n5 in arr:
        sum_n2 += n2
        sum_n5 += n5
    print(min(sum_n2, sum_n5))

if __name__ == "__main__":
    boj1676()