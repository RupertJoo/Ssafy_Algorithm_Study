import sys
sys.stdin = open("./refs/input_swea_1242.txt")

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
        set_code = set()
        ans = 0
        for i in arr:
            if int(i, 16):
                bin_str_i = bin(int(i, 16))[2:]
                # print(bin_str_i)
                str_now = "1"
                count_ii = 0
                lst_count = []
                for ii in bin_str_i:
                    if ii == str_now:
                        count_ii += 1
                    else:
                        lst_count.append(count_ii)
                        str_now = ii
                        count_ii = 1
                # print(*lst_count)
                str_count = ''.join([str(ii // min(lst_count[:3])) for ii in lst_count])
                # print(str_count)

                arr_decode = []
                key_dict = str_count[:3]
                arr_decode.append(dict_code[key_dict])
                for ii in range(3, len(str_count), 4):
                    key_dict = str_count[ii+1:ii+4]
                    if key_dict not in dict_code.keys():
                        # print(key_dict)
                        break
                    else:
                        arr_decode.append(dict_code[key_dict])
                # print(*arr_decode)
                sum_even = 0
                sum_odd = 0
                sum_result = 0
                for ii in range(8):
                    if ii % 2 == 1:
                        sum_even += arr_decode[ii]
                    else:
                        sum_odd += arr_decode[ii]
                # print(sum_odd * 3 + sum_even)
                if (sum_odd * 3 + sum_even) % 10 == 0:
                    # sum_result += sum_odd + sum_even
                    set_code.add(''.join(map(str, arr_decode)))
        # print(set_code)
        for i in set_code:
            ans += sum(map(int, i))
        print(f"#{tc} {ans}")




if __name__ == "__main__":
    swea1242()