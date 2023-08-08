def swea1213():
    t = 10
    for tc in range(1, t + 1):
        _ =  input()
        ptn = input()
        text = input()
        m = len(ptn)
        n = len(text)

        i = 0
        j = 0
        result = 0
        while j < m and i < n:
            if text[i] != ptn[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1
            if j == m:
                result += 1
                j = 0

        # result = 0
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea1213()
