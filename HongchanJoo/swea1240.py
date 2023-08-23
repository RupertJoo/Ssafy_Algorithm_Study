# import sys
# sys.stdin = open("./refs/input_swea_1240.txt")


def swea1240():
    dict_cypher = {
                "0001101": 0,
                "0011001": 1,
                "0010011": 2,
                "0111101": 3,
                "0100011": 4,
                "0110001": 5,
                "0101111": 6,
                "0111011": 7,
                "0110111": 8,
                "0001011": 9
                }

    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        arr = [input() for _ in range(n)]

        is_break = False
        for r in range(n):
            for c in range(m - 1, -1, -1):
                if int(arr[r][c]):
                    r_start = r
                    c_start = c - 55
                    is_break = True
                    break
            if is_break:
                break

        sum_odd = 0
        sum_even = 0
        for c in range(8):
            str_temp = arr[r_start][c_start + c * 7: c_start + c * 7 + 7]
            if c % 2:
                sum_even += dict_cypher[str_temp]
            else:
                sum_odd += dict_cypher[str_temp]
        if (3 * sum_odd + sum_even) % 10:
            ans = 0
        else:
            ans = sum_odd + sum_even
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1240()