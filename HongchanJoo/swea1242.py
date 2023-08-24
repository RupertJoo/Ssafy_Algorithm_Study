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
        set_value = set()
        for i in arr:
            if int(i, 16):
                bin_str_i = bin(int(i, 16))[:]
                print(f"ddd = {bin_str_i}")
                str_now = "1"
                count_ii = 1
                count_3 = 0
                lst_count = []
                lst_code = []
                for ii in bin_str_i:
                    if ii == str_now:
                        count_ii += 1
                    else:
                        lst_count.append(count_ii)
                        str_now = ii
                        count_ii = 1
                        count_3 += 1
                # print(lst_count)
                # for ii in range(0, len(lst_count), 3):
                #     lst_count_3 = lst_count[ii:ii + 3]
                #     print(lst_count_3)
                #     str_count = ''.join([str(i // min(lst_count_3)) for i in lst_count_3])
                #     print(str_count)
                #     if str_count not in dict_code.keys():
                #         break
                #     else:
                #         print("sex")
                #         lst_code.append(dict_code[str_count])
                #
                # num_even = 0
                # num_odd = 0
                # for ii in range(8):
                #     if ii % 2 == 0:
                #         num_even += lst_code[ii]
                #     else:
                #         num_odd += lst_code[ii]
                #
                # if (num_even + num_odd * 3) % 10 == 0:
                #     set_value.add(sum(dict_code))
                print(lst_count)
        ans = 0
        # for i in set_value:
        #     ans += i
        print(f"{tc} {ans}")







if __name__ == "__main__":
    swea1242()