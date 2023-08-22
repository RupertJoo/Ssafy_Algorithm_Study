def calTree(i):
    global n
    global tree
    global child_left
    global child_right

    if i <= n and child_left[i]:
        calTree(child_left[i])
        if child_right[i]:
            calTree(child_right[i])

        if tree[i] in ["+", "-", "*", "/"]:
            oper_left = tree[child_left[i]]
            oper_right = tree[child_right[i]]
            if tree[i] == "+":
                tree[i] = oper_left + oper_right
            elif tree[i] == "-":
                tree[i] = oper_left - oper_right
            elif tree[i] == "*":
                tree[i] = oper_left * oper_right
            elif tree[i] == "/":
                tree[i] = oper_left // oper_right


def swea1232():
    global n
    global tree
    global child_left
    global child_right

    t = 10
    for tc in range(1, t + 1):
        n = int(input())
        tree = [0] * (n + 1)
        child_left = [0] * (n + 1)
        child_right = [0] * (n + 1)
        for _ in range(n):
            arr = list(input().split())
            len_arr = len(arr)
            if len_arr == 4:
                tree[int(arr[0])] = arr[1]
                child_left[int(arr[0])] = int(arr[2])
                child_right[int(arr[0])] = int(arr[3])
            else:
                tree[int(arr[0])] = int(arr[1])
        calTree(1)
        print(f"#{tc} {tree[1]}")


if __name__ == "__main__":
    swea1232()