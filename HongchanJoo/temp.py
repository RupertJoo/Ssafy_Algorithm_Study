def swea16505():
    for tc in range(1, int(input()) + 1):
        n = int(input()) // 10
        result = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                result = result * 2 + 1
            else:
                result = result * 2 - 1
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16505()