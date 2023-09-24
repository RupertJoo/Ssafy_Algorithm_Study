class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find_set(self, x):
        if self.parents[x] == x:
            return x
        return self.find_set(self.parents[x])

    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x != root_y:
            if self.ranks[root_x] < self.ranks[root_y]:
                self.parents[root_x] = root_y
            elif self.ranks[root_x] > self.ranks[root_y]:
                self.parents[root_y] = root_x
            else:
                self.parents[root_y] = root_x
                self.ranks[root_x] += 1

n = int(input())
djset = DisjointSet(n)
while True:
    cmt_num = input().split()
    if not cmt_num:
        print("볼장 다봤으니 끄겠다구")
        break
    if cmt_num[0] == "find":
        print(f"find {int(cmt_num[1])}")
        djset.find_set(int(cmt_num[1]))
        print(djset.parents)
        print(djset.ranks)
    elif cmt_num[0] == "union":
        print(f"union {int(cmt_num[1])} {int(cmt_num[2])}")
        djset.union(int(cmt_num[1]), int(cmt_num[2]))
        print(djset.parents)
        print(djset.ranks)
