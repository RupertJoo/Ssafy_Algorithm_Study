import sys
input = sys.stdin.readline

def boj18111():
    n, m, b = map(int, input().split())
    arr = []
    t_ans = 500 * 500 * 2 * 256  # 다른 어떤 경우에서도 이보다 빠르다.
    h_ans = 256  #  다른 어떤 경우에서도 이보다 높이가 낮다.
    for _ in range(n):
        arr.extend(list(map(int, input().split())))  # 이 경우 가로 세로 정보는 중요하지 않다.

    heights = [0] * 257  # i번 index에 2개 있다 -> 구역 내에 높이가 i인 땅이 2개 있다!
    for h in arr:
        heights[h] += 1
    h_start = min((sum(arr) + b) // (n * m), max(arr))  # 이보단 높은 높이에서 시작해야 한다.
    for h_flat in range(h_start, -1, -1):
        n_dig, n_dump = 0, 0  # n_dig: 파는 횟수, n_dump 쌓는 횟수
        for h, num_h in enumerate(heights):
            if num_h:
                if h > h_flat:
                    n_dig += num_h * (h - h_flat)
                else:
                    n_dump += num_h * (h_flat - h)
        t_flat = n_dump + 2 * n_dig
        if t_ans > t_flat:  # 갱신 가능하다면
            t_ans = t_flat
            h_ans = h_flat
        else:  # 갱신불가 -> 더 이상 유망하지 않다, 순회 불필요!
            break
    print(t_ans, h_ans)


if __name__ == "__main__":
    boj18111()
