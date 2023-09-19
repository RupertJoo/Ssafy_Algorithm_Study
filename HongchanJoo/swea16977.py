import sys
global min_charge
input = sys.stdin.readline


def getCharge(i_start, i_end, stations, charge):
    global min_charge

    if i_start >= i_end:
        if min_charge > charge:
            min_charge = charge
        return
    elif charge >= min_charge:
        return
    for ii in range(1, stations[i_start] + 1):
        getCharge(i_start + ii, i_end, stations, charge + 1)


def swea16977():
    for tc in range(1, int(input()) + 1):
        global min_charge
        stations = list(map(int, input().split()))
        n = min_charge = stations[0]

        getCharge(1, n, stations, -1)
        print(f"#{tc} {min_charge}")


if __name__ == "__main__":
    swea16977()
