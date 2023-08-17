def backtracking(i, n, k, weight):
    global count
    global selected
    global exersize

    if weight < 500:  # 무게 500 미만일 경우 유망하지 않으므로 백트래킹을 마친다.
        return
    if i == n: # n 일 동안 무게 500 이상을 유지할 경우 count에 1 가산.
        count += 1
        return
    else:
        for j in range(n):  # 순열 만들기, 윤형이 코드 참고
            if not selected[j]:
                selected[j] = 1
                backtracking(i + 1, n, k, weight - k + exersize[j])  # 운동에 의한 근합성량 - 자연 근손실량
                selected[j] = 0


def boj18429():  # 전역변수 사용 시에는 늘 신중하자!
    global count
    global selected
    global exersize

    count = 0
    weight = 500

    n, k = map(int, input().split())  # 날짜와 일당 근손실량
    exersize = list(map(int, input().split()))  # 운동에 의한 근합성량
    selected = [0] * n  # 운동 선택 여부 확인용
    backtracking(0, n, k, weight)  # 백트래킹을 통해 count 산출
    print(count)


if __name__ == "__main__":
    boj18429()