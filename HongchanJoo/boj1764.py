import sys
input = sys.stdin.readline
print = sys.stdout.write

def boj1764():
    n, m = map(int, input().rstrip().split())
    cnt = 0
    ans = ["0"] * m
    names = dict()
    for _ in range(n):
        name = input().rstrip()
        names[name] = 1
    for _ in range(m):
        name2 = input().rstrip()
        if names.setdefault(name2, 0):
            ans[cnt] = name2
            cnt += 1
    print("{} \n".format(cnt))
    ans.sort()
    for a in ans:
        if a[0] != "0":
            print("{} \n".format(a))


if __name__ == "__main__":
    boj1764()

