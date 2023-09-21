from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write


def get_postfix(expression):
    isp = {"+": "1", "-": "1", "*": "2", "/": "2", "(": "0"}
    icp = {"+": "1", "-": "1", "*": "2", "/": "2", "(": "3"}
    post = ""
    stack = deque()
    for e in expression:
        if e not in "(+-*/)":
            post += e
        else:
            if e == ")":
                while stack and stack[-1] != "(":
                    post += stack.pop()
                stack.pop()
            else:
                while stack and isp[stack[-1]] >= icp[e]:
                    post += stack.pop()
                stack.append(e)
    while stack:
        post += stack.pop()
    return post


def boj1918():
    expression = input().rstrip()
    expression_post = get_postfix(expression)
    print("{} \n".format(expression_post))


if __name__ == "__main__":
    boj1918()