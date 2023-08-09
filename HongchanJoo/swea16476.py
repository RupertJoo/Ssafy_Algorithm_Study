def swea16476():
    for tc in range(1, int(input()) + 1):
        str_code = input()
        stack = []
        result = 1

        for i in str_code:
            if i in "{(":
                stack.append(i)
            elif i in ")}":
                if not stack:
                    result = 0
                    break
                p = stack.pop()
                if (p == '{' and i == ')') or (p == '(' and i == '}'):
                    result = 0
                    break
            else:
                continue

        if stack:
            result = 0

        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16476()
