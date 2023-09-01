def swap(cnt, times, numbers, memo):
    global reward

    # 중복되면 종료
    temp = int(''.join(numbers))
    if (cnt, temp) in memo:
        return

    # 유일하면 추가
    memo.append((cnt,temp))

    # cnt == times 일 때 비교 후 함수 종료
    if cnt == times:
        temp =  int("".join(numbers))
        # print(temp)
        reward = max(reward, temp)
        return

    # cnt < times일 때 재귀
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            swap(cnt + 1, times, numbers, memo)
            numbers[i], numbers[j] = numbers[j], numbers[i]


def swea1244():
    global reward

    for tc in range(1, int(input()) + 1):
        numbers, times = map(int, input().split())
        numbers = list(str(numbers))
        cnt = 0
        memo = []
        reward = 0
        swap(cnt, times, numbers, memo)
        print(f"#{tc} {reward}")


if __name__ == "__main__":
    swea1244()
