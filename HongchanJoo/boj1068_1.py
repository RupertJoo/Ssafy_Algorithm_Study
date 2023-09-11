import sys
input = sys.stdin.readline


def boj1068_1():
    n = int(input())
    parents = list(map(int, input().split()))
    node_erase = int(input())
    cnt_leaf = 0

    def eraseTree(ne):
        parents[ne] = -2
        for i in range(n):
            if ne == parents[i]:
                eraseTree(i)

    eraseTree(node_erase)

    for i in range(n):
        if parents[i] != -2 and i not in parents:
            cnt_leaf += 1
    print(cnt_leaf)


if __name__ == "__main__":
    boj1068_1()