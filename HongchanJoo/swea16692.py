def bst(i):
    global n
    global tree
    global last

    if i <= n:
        bst(2 * i)
        if i // 2 <= n:
            last += 1
            tree[i] = last
        # print(*tree)
        bst(2 * i + 1)


def swea16692():
    global n
    global tree
    global last
    for tc in range(1, int(input()) + 1):
        n = int(input())
        tree = [0] * (n + 1)
        last = 0
        bst(1)
        print(f"#{tc} {tree[1]} {tree[n // 2]}")


if __name__ == "__main__":
    swea16692()