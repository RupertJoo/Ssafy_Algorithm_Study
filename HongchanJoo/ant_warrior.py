def ant_warrior():
    n = int(input())
    arr = list(map(int, input().split()))

    next = 0
    if arr[0] > arr[1]:
        idx = 0
    else:
        idx = 1
    food = arr[idx]
    while idx < n - 2:
        if idx < n - 3:
            if arr[idx + 2] > arr[idx + 3]:
                idx += 2
            else:
                idx += 3
        else:
            idx += 2
        food += arr[idx]
    print(food)



if __name__ == "__main__":
    ant_warrior()