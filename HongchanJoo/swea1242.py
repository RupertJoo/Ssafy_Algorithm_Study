import sys
sys.stdin = open("./refs/input_swea_1242_1.txt")

def swea1242():
    dict_code = {
                "211": 0,
                "221": 1,
                "122": 2,
                "411": 3,
                "132": 4,
                "231": 5,
                "114": 6,
                "312": 7,
                "213": 8,
                "112": 9
                }

    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        arr = [input() for _ in range(n)]
        for i in arr:
            if int(i, 16):
                bin_str_i = bin(int(i, 16))[2:]
                str_now = "1"
                count_ii = 1
                count_3 = 0
                lst_count = [None] * 3
                for ii in bin_str_i:
                    if ii == str_now:
                        count_ii += 1
                    else:
                        str_now = ii
                        count_ii = 1
                        count_3 += 1
                    if count_3 == 3:



if __name__ == "__main__":
    swea1242()