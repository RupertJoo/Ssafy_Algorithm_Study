def boj1436():
    n = int(input())
    ans = 666
    cnt = 0
    is_break = False
    while cnt < n:
        lst = list(map(int, str(ans)))
        for i in range(len(lst) - 2):
            if lst[i] == 6 and lst[i + 1] == 6 and lst[i + 2] == 6:
                cnt += 1
                break
        ans += 1
    print(ans-1)

if __name__ == "__main__":
    boj1436()

