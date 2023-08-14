def swea16530():
    for tc in range(1, int(input()) + 1):
        expression = list(input().split())
        # print(expression)
        stack = []
        for i in expression:
            if i in ["+", "-", "*", "/"]:
                if len(stack) < 2:
                    # print(f"len_stack: {len(stack)}")
                    result = "error"
                    break
                else:
                    # print(f"len_stack: {len(stack)}")
                    operand_right = stack.pop()
                    operand_left = stack.pop()
                    if i == "+":
                        stack.append(operand_left + operand_right)
                    elif i == "-":
                        stack.append(operand_left - operand_right)
                    elif i == "*":
                        stack.append(operand_left * operand_right)
                    elif i == "/":
                        if operand_right == 0:
                            result = "error"
                            break
                        else:
                            stack.append(operand_left // operand_right)
            elif i == ".":
                break
            else:
                stack.append(int(i))
            pass
        if i != "." or len(stack) != 1:
            result = "error"
        else:
            result = stack[0]
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16530()
