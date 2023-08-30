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
        list_code = []
        ans = 0
        for code_hex in arr:
            str_bin = ""
            for hx in code_hex:
                hx_to_dec = int(hx, 16)
                for j in range(3, -1, -1):
                    str_bin += "1" if hx_to_dec & (1 << j) else "0"  # 16진수 문자열를 이진수 문자열로 변환
            if not int(str_bin, 2):  # 변화를 마친 전체 문자열이 0으로만 이루어져 있을 때 다음 행으로 순회한다.
                continue
            else:
                str_bin = str_bin.rstrip("0")  # 문자열 끝의 "1"부터 읽기에 오른쪽"0"을 전부 지운다.
                ratio = [0] * 4
                code = []
                for j in range(len(str_bin) - 1, -1, -1):
                    if str_bin[j] == "1" and ratio[2] == 0:
                        ratio[3] += 1
                    elif str_bin[j] == "0" and ratio[1] == 0:
                        ratio[2] += 1
                    elif str_bin[j] == "1" and ratio[0] == 0:
                        ratio[1] += 1
                    elif str_bin[j] == "0" and str_bin[j - 1] == "1":
                        num = dict_code.get(tuple((b // min(ratio[1:])) for b in ratio[1:]))
                        ratio = [0] * 4
                        code.append(num)
                        if len(code) == 8:
                            code_reversed = code[::-1]
                            odd = code_reversed[0] + code_reversed[2] + code_reversed[4] + code_reversed[6]
                            even = code_reversed[1] + code_reversed[3] + code_reversed[5] + code_reversed[7]
                            if (odd * 3 + even) % 10 == 0 and code not in list_code:
                                ans += odd + even
                                list_code.append(code)
                            code = []
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1242_alter()


