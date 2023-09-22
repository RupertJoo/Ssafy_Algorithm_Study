from sys import stdin


def boj25618_2try():
    # n = int(input())
    n = int(stdin.readline())
    # trainers[3] = [3, 5, 218]: 3번째 트레이너는 5마리의 포켓몬(1,3,4,6,7) 보유중, (int("11011010",2) = 218)
    trainers = [[0, 0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        lst_i = list(map(int, stdin.readline().split()))
        trainers[i][0], trainers[i][1] = i, lst_i[0]
        for r in lst_i[1:]:
            trainers[i][2] += 1 << r
    trainers.sort(key=lambda x: (x[1], x[2]))
    # print(*trainers[1:])
    powers = [0] * (n + 1)
    counts_back = [0] * (n + 1)

    i_start = 0
    cnt_same = 1
    triggered = False
    for i in range(1, n + 1):
        if trainers[i - 1][1] != trainers[i][1]:  # 가지고 있는 포켓몬의 수가 달라지는 시점에서 파워지수는 자기 자신만 있으므로 1
            counts_back[i] = cnt_same
            i_start = i
            # powers[i] = 1
            powers[trainers[i][0]] = 1
            continue
        if trainers[i - 1][2] == trainers[i][2]: # 두 트레이너의 포켓몬 로스터가 같다면
            triggered = True
            cnt_same += 1
        else:  # 두 트레이너의 포켓몬 로스터가 달라지는 시점에서 앞서 같은 로스터일때의 powers, counts_back을 입력한다.
            if triggered:
                for ii in range(i_start, i_start + cnt_same):
                    # powers[ii] = cnt_same
                    powers[trainers[ii][0]] = cnt_same
                    counts_back[ii] = cnt_same
                # cnt_same = 1
                triggered = False
                # continue

            i_start = i
            # counts_back[i] = cnt_same
            counts_back[i] = 1
            cnt_same = 1
            # 포켓몬의 수, i-1번째 트레이너의 비트로스터, i번째 트레이너의 비트로스터를 인수로 하는 함수
            def is_prior(left, right):
                idx_left = idx_right = 17
                while idx_left > 0 and idx_right > 0:
                    if bool(left & 1 << idx_left) == bool(right & 1 << idx_right):
                        idx_left -= 1
                        idx_right -= 1
                    else:
                        if left & 1 << idx_left:
                            idx_right -= 1
                        elif right & 1 << idx_right:
                            idx_left -= 1
                return True if idx_left <= idx_right else False

            if is_prior(trainers[i - 1][2], trainers[i][2]): #  상위호환이라면 파워지수는 i-1 번째 파워지수 + 1
                # powers[i] = powers[i - 1] + 1
                powers[trainers[i][0]] = powers[trainers[i - 1][0]] + 1
            else:  # 상위호환이 아닐 경우 상위호환이 되는 ii 번째 파워지수를 찾고 +1
                i_temp = None
                for i_temp in range(i - 1, i_start - 1, -1):
                    if is_prior(trainers[i_temp][2], trainers[i][2]):
                        break


                powers[trainers[i][0]] = powers[trainers[i_temp][0]] + 1 if i_temp else 1
    if triggered:
        for ii in range(i_start, i_start + cnt_same):
            # powers[ii] = cnt_same
            powers[trainers[ii][0]] = cnt_same
            counts_back[ii] = cnt_same
        # cnt_same = 1
        triggered = False
        # continue
    print(*powers[1:])

if __name__ == "__main__":
    boj25618_2try()

