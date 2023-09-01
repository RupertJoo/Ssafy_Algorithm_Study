def swap(cnt, times, num, memo):
    global max_value

    num_memo = int(''.join(map(str, num)))
    if (num_memo, cnt) in memo:
        return

    memo.append((num_memo, cnt))

    if cnt == times:
        n = int("".join(num))
        max_value = max(max_value, n)
        return

    for i in range(0, len(num) - 1):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            swap(cnt + 1, times, num, memo)
            num[i], num[j] = num[j], num[i]


def swea1244():
    global max_value

    for tc in range(1, int(input()) + 1):
        num, times = map(int, input().split())
        num = list(str(num))

        cnt = 0
        max_value = 0
        memo = []
        swap(cnt, times, num, memo)

        print(f"#{tc} {max_value}")


if __name__ == "__main__":
    swea1244()

