import sys
sys.stdin = open("./refs/sample_input_16905.txt", "r")

def is_run(arr):
    return arr[1] == arr[0] + 1 and arr[2] == arr[1] + 1


def is_triplet(arr):
    return arr[0] == arr[1] and arr[1] == arr[2]
def swea16905():
    for tc in range(1, int(input()) + 1):
        deck = list(map(int, input().split()))


        deck_1 = [deck[0], deck[2], deck[4]]
        for i_1 in range(6, len(deck) + 2, 2):
            is_break_1 = False
            deck_1.sort()
            for j in range(7, 1 << (len(deck_1))):
                cnt = 0
                deck_1_3 = []
                for k in range(len(deck_1)):
                    if j & (1 <<(len(deck_1) - 1 - k)):
                        cnt += 1
                        deck_1_3.append(deck_1[k])
                if cnt == 3:
                    if is_run(deck_1_3) or is_triplet(deck_1_3):
                        # print(deck_1_3)
                        is_break_1 = True
                        break
            if is_break_1:
                break
            if i_1 < len(deck):
                deck_1.append(deck[i_1])


        deck_2 = [deck[1], deck[3], deck[5]]
        for i_2 in range(7, len(deck) + 2, 2):
            is_break_2 = False
            deck_2.sort()
            for j in range(7, 1 << (len(deck_2))):
                cnt = 0
                deck_2_3 = []
                for k in range(len(deck_2)):
                    if j & (1 << (len(deck_2) - 1 - k)):
                        cnt += 1
                        deck_2_3.append(deck_2[k])
                if cnt == 3:
                    if is_run(deck_2_3) or is_triplet(deck_2_3):
                        # print(deck_2_3)
                        is_break_2 = True
                        break
            if is_break_2:
                break
            if i_2 < len(deck):
                deck_2.append(deck[i_2])
        print(f"#{tc} {is_break_1}{i_1} /// {is_break_2}{i_2 - 1}")

        if (is_break_1 and not is_break_2) or ((i_1) < (i_2 - 1)):
            ans = 1
        elif (not is_break_1 and is_break_2) or (i_1) > (i_2 - 1):
            ans = 2
        else:
            ans = 0
        print(f"#{tc} {ans}")

if __name__ == "__main__":
    swea16905()