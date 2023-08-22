# def inorder(t):
#     global child_left
#     global child_right
#     global lst_chr
#
#     if t:
#         # 왼쪽
#         inorder(child_left[t])
#         print(lst_chr[t], end="")
#         inorder(child_right[t])
#         # t에서 방문처리
#
#
# def swea1231():
#     global child_left
#     global child_right
#     global lst_chr
#     t = 10
#     for tc in range(1, t + 1):
#         n = int(input())
#         lst_chr = [0] * (n + 1)
#         child_left = [0] * (n + 1)
#         child_right = [0] * (n + 1)
#         for i in range(1, n + 1):
#
#             lst_i = list(input().split())
#             lst_chr[int(lst_i[0])] = lst_i[1]
#             if len(lst_i) == 4:
#                 child_left[int(lst_i[0])] = int(lst_i[2])
#                 child_right[int(lst_i[0])] = int(lst_i[3])
#             elif len(lst_i) == 3:
#                 child_left[int(lst_i[0])] = int(lst_i[2])
#         ans = ""
#         print(f"#{tc}", end=" ")
#         inorder(1)
#         print()
#
#
# if __name__ == "__main__":
#     swea1231()

def inorder(p, n):
    global tree
    if p <= n:
        inorder(p * 2, n)
        print(tree[p], end='')
        inorder(p * 2 + 1, n)

def swea1231_1():
    global tree
    t = 10
    for tc in range(1, t + 1):
        n = int(input())
        tree = [0] * (n + 1)
        for _ in range(n):
            arr = list(input().split())
            tree[int(arr[0])] = arr[1]
        print(f"#{tc} ", end="")
        inorder(1, n)
        print()


if __name__ == "__main__":
    swea1231_1()

