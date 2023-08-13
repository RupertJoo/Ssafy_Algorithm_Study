import sys

n, m = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, n + 1)]
arr_selected = []

for i in range(1 << n):
    element = []
    for j in range(n):
        if i & (1 << j):
            element.append(arr[j])
    if len(element) == m:
        arr_selected.append(element)

for i in range(len(arr_selected) - 1, 0, -1):
    for j in range(0, i):
        if str(arr_selected[j]) > str(arr_selected[j + 1]):
            arr_selected[j], arr_selected[j + 1] = arr_selected[j + 1], arr_selected[j]
for i in arr_selected:
    print(*i)