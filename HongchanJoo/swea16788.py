def swea16788():
    for tc in range(1, int(input()) + 1):
        x = float(input())
        i = 0
        ans = ""
        while i < 13 and (x % 1):
            x *= 2
            if x >= 1:
                ans += "1"
                x -= 1
            else:
                ans += "0"
            i += 1
        ans = "overflow" if i == 13 else ans
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea16788()