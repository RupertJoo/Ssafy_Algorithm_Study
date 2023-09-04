import sys
from collections import deque
input = sys.stdin.readline

def boj10733():
    stack = deque()
    k = int(input())
    for _ in range(k):
        if x:= int(input()):
            stack.append(x)
        else:
            stack.pop()
    print(sum(stack))


if __name__ == "__main__":
    boj10733()