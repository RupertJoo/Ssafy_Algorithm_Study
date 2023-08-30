"""
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

"""
def is_run(arr):
    return arr[1] == arr[0] + 1 and arr[2] == arr[1] + 1


def is_triplet(arr):
    return arr[0] == arr[1] and arr[1] == arr[2]


def swea16905():
    for tc in range(1, int(input()) + 1):
        deck = list(map(int, input().split()))
        deck_1 = [deck[0], deck[2], deck[4]]
        deck_2 = [deck[1], deck[3], deck[5]]
        for i in range(6, 12, 2):
            deck_1.sort()
            for j in range(7, 1 << (len(deck_1))):
                cnt = 0
                deck_1_3 = []
                for k in range(len(deck_1)):
                    if j & (1 << (len(deck_1) - 1 - k)):
                        cnt += 1
                        deck_1_3.append(deck_1[k])
                if cnt == 3:
                    if is_run(deck_1_3) or is_triplet(deck_1_3):
                        is_bg_1 = True


            deck_2.sort()

            deck_1.append(deck[i])
            deck_2.append(deck[i + 1])
            print(deck_1)
            print(deck_2)


if __name__ == "__main__":
    swea16905()