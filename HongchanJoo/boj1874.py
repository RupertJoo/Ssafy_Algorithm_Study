import sys
from collections import deque
input = sys.stdin.readline


def boj1874():
    n = int(input())
    stack_num = deque()
    stack_ans = deque([])
    queue_num = deque(list(range(1, n + 1)))
    lst = [0] * n
    for i in range(n):
        lst[i] = int(input())
    i = 0
    is_sequence = True
    while i < n:
        num_ith = lst[i]
        if queue_num and queue_num[0] < num_ith:
            while queue_num[0] != num_ith:
                stack_num.append(queue_num.popleft())
                stack_ans.append("+")
        elif queue_num and queue_num[0] == num_ith:
            stack_ans.append("+")
            queue_num.popleft()
            stack_ans.append("-")
            i += 1
        else:
            if stack_num[-1] == num_ith:
                stack_num.pop()
                stack_ans.append("-")
                i += 1
            else:
                is_sequence = False
                break
    if is_sequence:
        for ans in stack_ans:
            sys.stdout.write(ans + "\n")
    else:
        print("NO")


if __name__ == "__main__":
    boj1874()

