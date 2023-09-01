#  정식이의 은행업무
for tc in range(1, int(input()) + 1):
    bi = input()
    tri = list(map(int, input()))

    n = len(bi)
    m = len(tri)
    ans = 0
    binary = int(bi, 2)
    list_bin = [0] * n
    for i in range(n):
        list_bin[i] = binary ^ (1 << i)

    for i in range(m):
        num1 = 0
        num2 = 0
        for j in range(m):
            if i != j:
                num1 = num1 * 3 + tri[j]
                num2 = num2 * 3 + tri[j]
            else:
                num1 = num1 * 3 + (tri[j] + 1) % 3
                num2 = num2 * 3 + (tri[j] + 2) % 3
        if num1 in list_bin:
            ans = num1
            break
        if num2 in list_bin:
            ans = num2
            break
    print(f"#{tc} {ans}")
