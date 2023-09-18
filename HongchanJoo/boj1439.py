import sys
input = sys.stdin.readline

def boj1439():
    text = input().rstrip()
    cnt_0 = 0
    cnt_1 = 0
    x = int(text[0])
    if x:
        cnt_0 -= 1
    else:
        cnt_1 -= 1

    for i in range(len(text)-1):
        int_t = int(text[i])
        if int_t ^ int(text[i + 1]):
            if int_t:
                cnt_1 += 1
            else:
                cnt_0 += 1
    print(max(cnt_0, cnt_1))


if __name__ == "__main__":
    boj1439()




