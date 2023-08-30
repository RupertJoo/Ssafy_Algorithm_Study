def fibo(n):
    global list_fibo

    if n > 1 and list_fibo[n] == 0:
        list_fibo[n] = fibo(n - 1) + fibo(n - 2)
    return list_fibo[n]



def boj1003():
    global list_fibo

    list_fibo = [0] * 41
    list_fibo[0] = 0
    list_fibo[1] = 1
    for tc in range(1, int(input()) + 1):
        n = int(input())
        num_0 = 1
        num_1 = 0
        fibo_n = fibo(n)

        if n == 0:
            print(f"{num_0} {num_1}")
        else:
            print(f"{list_fibo[n-1]} {list_fibo[n]}")


if __name__ == "__main__":
    boj1003()