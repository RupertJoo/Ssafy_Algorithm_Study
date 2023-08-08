def swea3143():
    for tc in range(1, int(input()) + 1):
        text, ptn = input().split()
        n, m = len(text), len(ptn)
        result = 0

        i, j = 0, 0
        while j < m and i < n: # 쇼트서킷 때문에 판별순서가 중요하다!!
            if text[i] != ptn[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1
            if j == m:
                result += 1
                j = 0
        x = n - (m - 1) * result
        print(f"#{tc} {x}")


if __name__ == "__main__":
    swea3143()
