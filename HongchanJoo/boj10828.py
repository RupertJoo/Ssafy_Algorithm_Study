import sys
input = sys.stdin.readline

def boj10828():
    n = int(input())
    stack = []
    for i in range(n):
        cmd = list(input().split())
        if cmd[0] == "push":
            stack.append(int(cmd[1]))
        elif cmd[0] == "pop":
            if len(stack) < 1:
                print(-1)
            else:
                print(stack.pop())
        elif cmd[0] == "size":
            print(len(stack))
        elif cmd[0] == "empty":
            if len(stack) < 1:
                print(1)
            else:
                print(0)
        elif cmd[0] == "top":
            if len(stack) < 1:
                print(-1)
            else:
                print(stack[-1])


if __name__ == "__main__":
    boj10828()


