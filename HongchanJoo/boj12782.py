import sys
input = sys.stdin.readline

def boj12782():
    for tc in range(int(input())):
        a, b = input().split()
        len_a = len(a)

        int_a = int("0b" + a, 2)
        int_b = int("0b" + b, 2)
        int_or = int_a | int_b

        one_a = 0
        one_b = 0
        one_or = 0
        for i in range(len_a):
            if int_a & 1 << i:
                one_a += 1
            if int_b & 1 << i:
                one_b += 1
            if int_or & 1 << i:
                one_or += 1
        ans2 = one_or - min(one_a, one_b)
        print(ans2)


if __name__ == "__main__":
    boj12782()