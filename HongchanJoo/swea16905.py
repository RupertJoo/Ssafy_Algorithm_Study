def is_run(deck_x):
    cnt = 1
    for i in range(len(deck_x) - 1):
        if deck_x[i] and deck_x[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt == 3:
            break
    return cnt == 3

def is_triplet(deck_x):
    return 3 in deck_x

def swea16905():
    for tc in range(1, int(input()) + 1):
        deck = list(map(int, input().split()))
        deck_1 = [0] * 10
        deck_2 = [0] * 10
        for i in range(4):
            if i % 2:
                deck_2[deck[i]] += 1
            else:
                deck_1[deck[i]] += 1

        for i in range(4, len(deck)):
            if i % 2:
                deck_2[deck[i]] += 1
                if is_triplet(deck_2) or is_run(deck_2):
                    print(f"#{tc} {2}")
                    break
            else:
                deck_1[deck[i]] += 1
                if is_triplet(deck_1) or is_run(deck_1):
                    print(f"#{tc} {1}")
                    break
        else:
            print(f"#{tc} {0}")


if __name__ == "__main__":
    swea16905()