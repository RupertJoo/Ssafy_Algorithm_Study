import sys
from collections import deque

input = sys.stdin.readline

def boj4949():
    while True:
        text = input().rstrip()
        if text == ".":
            return
        else:
            # print(text, bool(text == "."))
            stack = deque()
            ans = "yes"
            for t in text:
                if t in "([":
                    stack.append(t)
                elif t in "])":
                    if not stack:
                        ans = "no"
                        break
                    x = stack.pop()
                    if x == "(" and t == "]" or x == "[" and t == ")":
                        ans = "no"
                        break
            if stack:
                ans = "no"
            print(ans)


if __name__ == "__main__":
    boj4949()