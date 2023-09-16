import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

def boj1011():
    for _ in range(int(input())):
        x, y = map(int, input().rstrip().split())
        cnt = 0
        dist = 0
        while dist < y - x:
            dist += (cnt // 2) + 1
            cnt += 1
        print("{} \n".format(cnt))


if __name__ == "__main__":
    boj1011()
