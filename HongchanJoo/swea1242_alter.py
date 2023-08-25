import sys
sys.stdin = open("./refs/input_swea_1242.txt")

def swea1242_alter():
    dict_code = {
                (2, 1, 1): 0,
                (2, 2, 1): 1,
                (1, 2, 2): 2,
                (4, 1, 1): 3,
                (1, 3, 2): 4,
                (2, 3, 1): 5,
                (1, 1, 4): 6,
                (3, 1, 2): 7,
                (2, 1, 3): 8,
                (1, 1, 2): 9
                }

    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        arr = set([input()[:m] for _ in range(n)])
        set_code = set()
        ans = 0
        for code_hex in arr:
            hex_to_dec = int(code_hex, 16)
            if hex_to_dec:
                str_bin = ""
                for i in range(3, -1, -1):
                    str_bin += "1" if hex_to_dec & (1 << i) else "0"
                ratio = [0] * 4
                code = []
                for c_bin in range(len(str_bin) - 1, -1, -1):
                    if c_bin == "1" and ratio[2] == 0:
                        ratio[3] += 1
                    elif c_bin == "0" and ratio[1] == 0:
                        ratio[2] += 1
                    elif c_bin == "1" and ratio[0] == 0:
                        ratio[1] += 1
                    elif c_bin == "0" and str_bin[c_bin - 1] == "1":

                        key_decode = tuple((i // min(ratio)) for i in ratio[1:])
                        num_decode = dict_code.get(key_decode)
                        code.append(num_decode)

                        if len(code) == 8:
                            code_reversed = code[::-1]
                            odd = code_reversed[0] + code_reversed[2] + code_reversed[4] + code_reversed[6]
                            even = code_reversed[1] + code_reversed[3] + code_reversed[5] + code_reversed[7]
                            if (odd * 3 + even) % 10 == 0 and code not in set_code:
                                print(odd + even)
                                ans += odd + even
                                set_code.add(code)
        print(f"#{tc} {ans}")




if __name__ == "__main__":
    swea1242_alter()