import sys
input = sys.stdin.readline
print = sys.stdout.write


def boj5430():
    for tc in range(1, int(input()) + 1):
        cmd = input().rstrip()
        n = int(input())

        lst = list(map(int, input().rstrip()[1: -1].split(",")))
        d = 1
        i_start = 0
        i_end = n - 1
        is_valid = True
        for c in cmd:
            print("{} \n".format(c))
            if c == "R":
                d = d ^ 1
            else:
                if i_start == i_end:
                    print("error \n")
                    is_valid = False
                    break
                if d:
                    i_end -= 1
                else:
                    i_start += 1
        if is_valid:
            if d:
                print("{} \n".format(lst[i_start: i_end + 1]))
            else:
                print("{} \n".format(lst[i_end: i_end - 1:-1]))


if __name__ == "__main__":
    boj5430()