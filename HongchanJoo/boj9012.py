def boj9012():
    for tc in range(1, int(input()) + 1):
        bracket = input()
        stack = []
        ans = "YES"
        for i in range(len(bracket)):
            if bracket[i] == "(":
                stack.append(bracket[i])
            elif bracket[i] == ")":
                if not stack:
                    ans = "NO"
                    break
                else:
                    stack.pop()
        if stack:
            ans = "NO"
        print(ans)


if __name__ == "__main__":
    boj9012()