def is_triple(arr):
    return arr[0] == arr[1] and arr[1] == arr[2]


def is_run(arr):
    return arr[0] == arr[1] - 1 and arr[1] == arr[2] - 1

def check_bg(i,len_arr, arr, is_bg):
    global bg
    if i == len_arr:
        # print(arr)
        arr_front = arr[:3]
        arr_rear = arr[3:]
        # print(*arr_front, "     ",*arr_rear)
        if (is_triple(arr_front) or is_run(arr_front)) and (is_triple(arr_rear) or is_run(arr_rear)):
            is_bg = True
            bg = is_bg
            return bg
        else:
            is_bg = False
        # print(is_bg)
            bg = is_bg

    else:
        for j in range(i, len_arr):
            arr[i], arr[j] = arr[j], arr[i]
            check_bg(i + 1,len_arr, arr, is_bg)
            arr[i], arr[j] = arr[j], arr[i]
            # return bg/


def babygin():
    global bg
    bg = False
    for tc in range(1, int(input()) + 1):
        arr = list(map(int, input()))
        len_arr = len(arr)
        is_bg = True
        bg = check_bg(0, len_arr, arr, is_bg)
        print(bg)

if __name__ == "__main__":
    babygin()
