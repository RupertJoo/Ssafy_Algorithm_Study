icp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 3}
isp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 0}


def get_postfix(expression, len_expression):
    postfix = ""
    stack = []
    for i in range(len_expression):
        if expression[i] not in ["(", "+", "-", "/", "*", ")"]:
            postfix += expression[i]
        else:
            if expression[i] == ")":
                while stack:
                    temp = stack.pop()
                    if temp == "(":
                        break
                    expression += temp
            else:
                while stack and isp[stack[-1]] >= icp[expression[i]]:
                    postfix += stack.pop()
                stack.append(expression[i])
    while stack:
        postfix += stack.pop()
    return postfix


def get_result(postfix):
    stack = []
    for c in postfix:
        if c not in ["(", "+", "-", "/", "*", ")"]:
            stack.append(int(c))
        else:
            operand_r = stack.pop()
            operand_l = stack.pop()
            if c == "+":
                result = operand_l + operand_r
            elif c == "-":
                result = operand_l - operand_r
            elif c == "/":
                result = operand_l / operand_r
            elif c == "*":
                result = operand_l * operand_r
            stack.append(result)
    return stack.pop()


def swea1222():
    t = 10
    for tc in range(1, t + 1):
        len_expression = int(input())
        expression = input()
        postfix = get_postfix(expression, len_expression)
        result = get_result(postfix)
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea1222()