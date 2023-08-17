def backtracking(i, n, isPlay):
    global guitar_song
    global used
    global m
    global min_guitar  # 초기값 n
    global max_song  # 초기값 0

    element = 0
    for xx in list(map(int, list(isPlay[2:]))):
        element += xx

    if max_song < element:
        min_guitar = i
        max_song = element

    elif max_song == element:
        if min_guitar >= i:
            min_guitar = i
            max_song = element

    for j in range(i, n):
        if not used[j]:
            used[j] = 1
            temp = int(isPlay,2)
            backtracking(i + 1, n, bin(int(isPlay, 2) | int(guitar_song[j][1], 2)))
            isPlay = bin(temp)[2:]
            used[j] = 0


def boj1497():
    global guitar_song
    global used
    global m
    global min_guitar
    global max_song

    max_song = 0
    n, m = map(int, input().split())  # n: 기타의 갯수, m: 곡의 갯수
    min_guitar = n
    guitar_song = list(list(input().split()) for _ in range(n))
    for gs in guitar_song:
        gs[1] = gs[1].replace("Y", "1")
        gs[1] = gs[1].replace("N", "0")
        gs[1] = '0b' + gs[1]
    isPlay = '0b'+'0' * m
    used = [0] * n
    backtracking(0, n, isPlay)
    if max_song == 0:
        print(-1)
    else:
        print(min_guitar)


if __name__ == "__main__":
    boj1497()