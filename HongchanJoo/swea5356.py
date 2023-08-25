import sys
sys.stdin = open("./refs/input_swea_5356.txt", "r")

def swea5356():
    for tc in range(1, int(input()) + 1):
        arr_string = [input() for _ in range(5)]
        max_len = 0
        print(f"#{tc} ", end="")
        for i in arr_string:
            len_i = len(i)
            if max_len < len_i:
                max_len = len_i

        for j in range(max_len):
            for k in range(5):
                if len(arr_string[k]) > j:
                    print(arr_string[k][j], end="")
                else:
                    pass
        print()


if __name__ == "__main__":
    swea5356()