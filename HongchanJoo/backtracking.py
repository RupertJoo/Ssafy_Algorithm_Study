def bk(n, i_start, arr, lst, selected, sum_lst):
    if sum_lst == 10:
        print(*lst)
        return
    if sum_lst > 10:
        return
    for ii in range(i_start, 10):
        if not selected[ii]:
            selected[ii] = 1
            lst.append(arr[ii])
            bk(n, ii + 1, arr, lst, selected, sum_lst + arr[ii])
            selected[ii] = 0
            lst.pop()


def backtracking():
    arr = list(range(1, 10 + 1))
    selected = [0] * 10
    bk(10, 0, arr, [], selected, 0)


if __name__ == "__main__":
    backtracking()