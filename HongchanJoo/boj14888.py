from collections import deque


def bf(i, n, numbers, operators, orders, abcd):
    global q
    if i == n:
        ans = numbers[0]
        for num, order in zip(numbers[1:], orders):
            if order == "+":
                ans += num
            elif order == "-":
                ans -= num
            elif order == "*":
                ans *= num
            else:
                if ans >= 0:
                    ans //= num
                else:
                    ans = -1 * (-ans // num)
        q.append(ans)
        return
    for ii in range(4):
        if operators[ii] > 0:
            operators[ii] -= 1
            orders.append(abcd[ii])
            bf(i + 1, n, numbers, operators, orders, abcd)
            operators[ii] += 1
            orders.pop()

def boj14888():
    global q
    q = deque()
    abcd ="+-*/"
    n = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    bf(1, n, numbers, operators, [], abcd)
    q = sorted(q)
    print(q[-1])
    print(q[0])

if __name__ == "__main__":
    boj14888()
