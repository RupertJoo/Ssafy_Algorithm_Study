from collections import deque


def rotateR(i, d):
    if 0 <= i + 1 < 4 and li[i][2] != li[i + 1][6]:
        rotateR(i + 1, -d)
    li[i].appendleft(li[i].pop())



def rotateL(i, d):
    if 0 <= i - 1 < 4 and li[i][6] != li[i - 1][2]:
        rotateL(i - 1, -d)
    li[i].appendleft(li[i].pop())



def rotate(i, d):
    if 0 <= i - 1 < 4 and li[i][6] != li[i - 1][2]:
        rotateL(i - 1, -d)
    if 0 <= i + 1 < 4 and li[i][2] != li[i + 1][6]:
        rotateR(i + 1, -d)
    li[i].appendleft(li[i].pop())


T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    li = [deque(map(int, input().split())) for i in range(4)]
    rotate_info = []
    for i in range(K):
        rotate_info.append(list(map(int, input().split())))
    for idx, d in rotate_info:
        rotate(idx - 1, d)

    sum_ = 0

    for k in range(4):
        sum_ += li[k][0] * (2 ** k)

    print(f'#{test_case} {sum_}')