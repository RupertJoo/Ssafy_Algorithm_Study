def nodesum(i):
    global n
    global tree

    if i <= n:
        nodesum(2 * i)
        nodesum(2 * i + 1)
        if 2 * i <= n:
            tree[i] += tree[2 * i]
            if 2 * i + 1 <= n:
                tree[i] += tree[2 * i + 1]


def swea16720():
    global n
    global tree

    for tc in range(1, int(input()) + 1):
        n, m, l = map(int, input().split())
        tree = [0] * (n + 1)
        for _ in range(m):
            idx_leaf, leaf = map(int, input().split())
            tree[idx_leaf] = leaf
        nodesum(1)
        print(f"#{tc} {tree[l]}")


if __name__ == "__main__":
    swea16720()