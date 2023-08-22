def calTree(i):
    global n
    global tree
    global ans

    if i <= n:
        calTree(2 * i)
        calTree(2 * i + 1)
        if 2 * i <= n:
            if tree[i][0] in ["+", "-", "*", "/"]:
                oper_left = tree[tree[i][1]]
                oper_right = tree[tree[i][2]]
                print(oper_left)
                print(oper_right)
                if tree[i][0] == "+":
                    tree[i] = oper_left + oper_right
                elif tree[i][0] == "-":
                    tree[i] = oper_left - oper_right
                elif tree[i][0] == "*":
                    tree[i] = oper_left * oper_right
                elif tree[i][0] == "/":
                    tree[i] = oper_left // oper_right
    # print(*tree)


def swea1232():
    global n
    global tree
    global ans

    t = 10
    for tc in range(1, t + 1):
        n = int(input())
        tree = [0] * (n + 1)
        for _ in range(n):
            arr = list(input().split())
            len_arr = len(arr)
            if len_arr == 4:
                tree[int(arr[0])] = [arr[1], int(arr[2]), int(arr[3])]
            else:
                tree[int(arr[0])] = int(arr[1])
        ans = 0
        calTree(1)
        print(f"#{tc} {tree[1]}")


if __name__ == "__main__":
    swea1232()
