def swea16786():
    for tc in range(1, int(input()) + 1):
        n, text_hex = input().split()
        print(f"#{tc}", end=" ")
        for t in text_hex:
            t10 = int(t, 16)
            ii = 3
            while ii >= 0:
                if t10 & (1 << ii):
                    print(1, end="")
                else:
                    print(0, end="")
                ii -= 1
        print()


if __name__ == "__main__":
    swea16786()