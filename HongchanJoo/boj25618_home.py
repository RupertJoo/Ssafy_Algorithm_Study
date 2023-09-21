from sys import stdin
from sys import stdout
from collections import deque

input = stdin.readline
pprint = stdout.write


def count_bit(x):
    q = deque()
    start = 0
    end = 100_000
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if (1 << mid) - 1 == x:
            break
        elif (1 << mid) - 1 > x:
            end = mid - 1
        else:
            start = mid + 1
    for i in range(mid + 1, -1, -1):
        if x & 1 << i:
            cnt += 1
            q.append(i)
    q = list(q)
    return cnt, q


def boj25618():
    n = int(input())
    classified = {i: 0 for i in range(1, 18)}
    powers = [0] * (n + 1)
    roasters = [0] * (n + 1)
    for i in range(1, n + 1):
        n_roaster = list(map(int, input().split()))
        classified[n_roaster[0]] += 1 << i
        for ii in n_roaster[1:]:
            roasters[i] += 1 << ii
    for k, v in classified.items():
        if v:
            cnt, lst = count_bit(v)
            roaster_c = [[] for _ in range(cnt)]
            for ii in range(cnt):
                roaster_c[ii] = [lst[ii], roasters[lst[ii]]]
            roaster_c.sort(key=lambda x: x[1])
            # pprint("{} \n".format(roaster_c))
            powers[roaster_c[0][0]] = 1
            idx_same = 0
            cnt_same = 1
            triggered = False
            for ii in range(1, cnt):
                if roasters[roaster_c[ii][0]] == roasters[roaster_c[ii-1][0]]:
                    triggered = True
                    cnt_same += 1
                else:
                    if triggered:
                        for ix in range(idx_same, idx_same + cnt_same):
                            powers[roaster_c[ix][0]] = cnt_same
                        triggered = False
                    idx_same = ii
                    cnt_same = 1
                    idx_ii, power_ii = roaster_c[ii]
                    rii = count_bit(power_ii)[1]
                    iii = ii - 1
                    while iii >= 0:
                        idx_iii, power_iii = roaster_c[iii]
                        riii = count_bit(power_iii)[1]
                        if k == sum(list(map(lambda x, y: x >= y, rii, riii))):
                            powers[idx_ii] = powers[idx_iii]
                            break
                        iii -= 1
                    powers[idx_ii] += 1
            if triggered:
                for ix in range(idx_same, idx_same + cnt_same):
                    powers[roaster_c[ix][0]] = cnt_same
                triggered = False
    print(*powers[1:])


if __name__ == "__main__":
    boj25618()