def getListAns(n):
    global list_ans

    if n > 3 and list_ans[n] == 0:
        list_ans[n] = getListAns(n - 1) + getListAns(n - 2) + getListAns(n - 3)
    return list_ans[n]


def boj9095():
    global list_ans
    list_ans = [0] * 11
    list_ans[1] = 1
    list_ans[2] = 2
    list_ans[3] = 4

    for tc in range(1, int(input()) + 1):
        n = int(input())
        ans = getListAns(n)
        print(ans)

if __name__ == "__main__":
    boj9095()