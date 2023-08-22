def swea1289():
    for tc in range(1, int(input()) + 1):
        bitbit = input()
        ans = int(bitbit[0])
        bb = bitbit[0]
        for b in bitbit[1:]:
            if bb != b:
                ans += 1
                bb = b

        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1289()
