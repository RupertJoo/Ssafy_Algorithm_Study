def boj1991_1():
    def print_preorder(m):
        if m:
            print(str_alphabet[m], end="")
            print_preorder(child_left[m])
            print_preorder(child_right[m])

    def print_inorder(m):
        if m:
            print_inorder(child_left[m])
            print(str_alphabet[m], end="")
            print_inorder(child_right[m])

    def print_postorder(m):
        if m:
            print_postorder(child_left[m])
            print_postorder(child_right[m])
            print(str_alphabet[m], end="")

    dict_alphabet = {chr(i): i - 64 for i in range(65, 91)}
    str_alphabet = ''.join(["0"] + [chr(i) for i in range(65, 91)])
    child_left = [0] * 27
    child_right = [0] * 27
    n = int(input())
    for _ in range(n):
        v, l, r = input().split()
        if l != ".":
            child_left[dict_alphabet[v]] = dict_alphabet[l]
        if r != ".":
            child_right[dict_alphabet[v]] = dict_alphabet[r]

    print_preorder(1)
    print()
    print_inorder(1)
    print()
    print_postorder(1)
    print()


if __name__ == "__main__":
    boj1991_1()