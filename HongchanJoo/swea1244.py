def swea1244():
    for tc in range(1, int(input()) + 1):
        str_num, n = input().split()
        numbers = list(map(int, str_num))
        numbers_rev = sorted(numbers, reverse=True)
        n = int(n)
        cnt = 0
        is_break = False

        for i in range(len(numbers) - 1):
            if numbers[i] == numbers_rev[i]:
                continue
            else:
                cnt += 1
                for j in range(len(numbers) - i -1, i, -1):
                    if numbers_rev[i] == numbers[j]:
                        numbers[i], numbers[j] = numbers[j], numbers[i]
                        print(numbers)
                        if cnt == n:
                            is_break = True
                        break
                    else:
                        continue

            if is_break:
                break
        # print(cnt)
        # if n - cnt > 0 and (n - cnt) // 2:
        #     numbers[-2], numbers[-1] = numbers[-1], numbers[-2]
        ans = ''.join(map(str, numbers))
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1244()