def swea1234():
    t = 10
    for tc in range(1, t + 1):
        n, text = input().split()
        n = int(n)
        stack = []
        stack.append(text[0])

        for c in text[1:]:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        ans = ''.join(stack)

        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1234()