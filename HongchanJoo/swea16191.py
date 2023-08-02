def swea16191():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        cards = list(map(int, list(input())))
        dict_cards = dict()
        for i in cards:
            dict_cards[i] = dict_cards.setdefault(i, 0) + 1
        result_key = 0
        result_value = 0
        for ik, iv in dict_cards.items():
            if result_value <= iv and result_key <= ik:
                result_key = ik
                result_value = iv
        print(f"#{tc} {result_key} {result_value}")

if __name__ == "__main__":
    swea16191()