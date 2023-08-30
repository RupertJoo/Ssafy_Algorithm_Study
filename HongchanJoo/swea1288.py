def swea1288():
    for tc in range(1, int(input()) + 1):
        list_count = [0] * 10
        n = int(input())
        ans = 0
        while 0 in list_count:
            ans += 1
            str_mul = str(n * ans)
            for s in str_mul:
                list_count[int(s)] = 1
        print(f"#{tc} {str_mul}")


if __name__ == "__main__":
    swea1288()