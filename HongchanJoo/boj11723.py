import sys
input = sys.stdin.readline
print = sys.stdout.write


def boj11723():
    s = set()
    for _ in range(int(input())):
        cmdn = input().rstrip()
        if cmdn == "all":
            s = set(range(1, 21))
        elif cmdn == "empty":
            s = set()
        else:
            cmd, n = cmdn.split()
            n = int(n)
            if cmd == "add":
                s.add(n)
            elif cmd == "remove":
                s.discard(n)
            elif cmd == "check":
                print("{} \n".format(int(s.__contains__(n))))
            elif cmd == "toggle":
                if s.__contains__(n):
                    s.discard(n)
                else:
                    s.add(n)


if __name__ == "__main__":
    boj11723()