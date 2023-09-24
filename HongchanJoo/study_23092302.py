class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n

    def find_set(self, x):
        if self.parents[x] == x:
            return self.parents[x]
        return self.find_set(self.parents[x])

    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)
        if root_x != root_y:
            if root_x < root_y:
                self.parents[root_x] = root_y
            elif root_x > root_y:
                self.parents[root_y] = root_x
            else:
                self.parents[root_y] = root_x
                self.ranks[root_x] += 1

