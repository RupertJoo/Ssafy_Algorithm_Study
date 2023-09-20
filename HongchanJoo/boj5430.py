import sys
input = sys.stdin.readline
print = sys.stdout.write


def boj5430():
    for tc in range(1, int(input()) + 1):
        cmd = input().rstrip()
        n = int(input())
        if not n:
            _ = input()
            lst = []
        elif n == 1:
            item = int(input().rstrip()[1: -1])
            lst = [item]
        else:
            lst = list(map(int, input().rstrip()[1: -1].split(",")))
        d = 1
        i_start = 0
        i_end = n - 1
        is_valid = True
        for c in cmd:
            if c == "R":
                d = d ^ 1
            else:
                if n == 0 or i_start > i_end:
                    is_valid = False
                    break
                if d:
                    i_start += 1
                else:
                    i_end -= 1
        if is_valid:
            if n == 0 or i_start - i_end == 1:
                print("[] \n")
            else:
                if d:
                    print("[")
                    for i in range(i_start, i_end):
                        print("{},".format(lst[i]))
                    print("{}] \n".format(lst[i_end]))
                else:
                    print("[")
                    for i in range(i_end, i_start, -1):
                        print("{},".format(lst[i]))
                    print("{}] \n".format(lst[i_start]))
        else:
            print("error \n")


if __name__ == "__main__":
    boj5430()