
from collections import deque


def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left, right = li[:mid], li[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global cnt
    left, right = deque(left), deque(right)
    result = deque()

    if left[-1] > right[-1]:
        cnt += 1
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif left:
            result.append(left.popleft())
        elif right:
            result.append(right.popleft())

    return result


def solve():
    global cnt
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list(map(int, input().split()))
        cnt = 0
        arr = merge_sort(arr)

        print(f"#{tc} {arr[n // 2]} {cnt}")


if __name__ == "__main__":
    solve()