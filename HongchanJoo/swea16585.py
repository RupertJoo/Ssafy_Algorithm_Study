scissor = 1
rock = 2
paper = 3


def duel(left, right):  # 승부 결과를 반환하는 함수
    global arr
    if arr[left] == 1:
        if arr[right] == 1 or arr[right] == 3:
            winner = left
        else:
            winner = right
    elif arr[left] == 2:
        if arr[right] == 1 or arr[right] == 2:
            winner = left
        else:
            winner = right
    elif arr[left] == 3:
        if arr[right] == 2 or arr[right] == 3:
            winner = left
        else:
            winner = right
    return winner


def tournament(i, j):  # 대진표를 짜는 함수
    # 종료조건: 더 이상 쪼갤 수 가 없을 때까지
    if i == j:
        return i
    else:
        mid = (i + j) // 2
        left = tournament(i, mid)
        right = tournament(mid + 1, j)
        # 승자를 고르고
        winner = duel(left, right)
        return winner


# 분할정복: 쪼갤 수 있을때까지 나누고 문제를 푼다
def swea16585():
    global arr
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        arr = list(map(int, input().split()))
        winner = tournament(0, n - 1)
        print(f"#{tc} {winner + 1}")  # 선수 번호는 1번부터 n번 까지


if __name__ == "__main__":
    swea16585()
