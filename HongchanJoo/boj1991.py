def print_preorder(tree, tree_rev, c):
    print(tree_rev.get(tree.get(c, 0)), end="")
    if tree_rev.get(2 * tree.get(c, 0), 0):
        print_preorder(tree, tree_rev, tree_rev.get(2 * tree.get(c, 0), 0))
    if tree_rev.get(2 * tree.get(c, 0) + 1, 0):
        print_preorder(tree, tree_rev, tree_rev.get(2 * tree.get(c, 0) + 1, 0))


def print_inorder(tree, tree_rev, c):
    if tree_rev.get(2 * tree.get(c, 0), 0):
        print_inorder(tree, tree_rev, tree_rev.get(2 * tree.get(c, 0), 0))
    # if tree.get(c, 0):
    print(tree_rev.get(tree.get(c, 0)), end="")
    if tree_rev.get(2 * tree.get(c, 0) + 1, 0):
        print_inorder(tree, tree_rev, tree_rev.get(2 * tree.get(c, 0) + 1, 0))


def print_postorder(tree, tree_rev, c):
    if tree_rev.get(2 * tree.get(c, 0), 0):
        print_postorder(tree, tree_rev, tree_rev.get(2 * tree.get(c, 0), 0))
    if tree_rev.get(2 * tree.get(c, 0) + 1, 0):
        print_postorder(tree, tree_rev, tree_rev.get(2 * tree.get(c, 0) + 1, 0))
    # if tree.get(c, 0):
    print(tree_rev.get(tree.get(c, 0)), end="")


def boj1991():
    n = int(input())
    tree = dict()
    i = 1
    for _ in range(n):
        v, l, r = input().split()
        if tree.get(v, 1):
            i = tree.get(v, 1)
            tree.setdefault(v, i)
            if l != ".":
                i_left = 2 * i
                tree.setdefault(l, i_left)
            if r != ".":
                i_right = 2 * i + 1
                tree.setdefault(r, i_right)
    tree_rev = {val : key for key, val in tree.items()}
    # print(tree)
    # print(tree_rev)

    print_preorder(tree, tree_rev, "A")
    print()
    print_inorder(tree, tree_rev, "A")
    print()
    print_postorder(tree, tree_rev, "A")
    print()


if __name__ == "__main__":
    boj1991()


