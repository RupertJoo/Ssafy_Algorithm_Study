from collections import deque
from itertools import permutations


def n_queen(n, position):
    global cnt
    move = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    # chessboard = [[0] * n for _ in range(n)]
    # for r, c in enumerate(position):
    #     chessboard[r][c] = 1
    # for cb in chessboard:
    #     print(*cb)

    is_nq = True

    q_position = deque()
    for r, c in enumerate(position):
        for ii in range(4):
            q_position.append((r + move[ii][0], c + move[ii][1], ii))
    while q_position:
        r_now, c_now, d = q_position.popleft()
        if 0 <= r_now < n and 0 <= c_now < n:
            if position[r_now] == c_now:
                is_nq = False
                break
            q_position.append((r_now + move[d][0], c_now + move[d][1], d))

    # for r_now, c_now in enumerate(position):
    #     for dr, dc in move:
    #         r_nxt, c_nxt = r_now + dr, c_now + dc
    #         while 0 <= r_nxt < n and 0 <= c_nxt < n:
    #             if position[r_nxt] == c_nxt:
    #                 is_nq = False
    #                 break
    #             r_nxt += dr
    #             c_nxt += dc
    #         if not is_nq:
    #             break
    #     if not is_nq:
    #         break

    if is_nq:
        cnt += 1

def perm(i, n, selected, position):
    global cnt
    move = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
    if i == n:
        # n_queen(n, position)
        cnt += 1
    else:
        for ii in range(n):
            if not selected[ii]:
                selected[ii] = 1
                position.append(ii)
                perm(i + 1, n, selected, position)
                selected[ii] = 0
                position.pop()


def boj9663():
    global cnt
    cnt = 0
    n = int(input())
    selected = [0] * n

    perm(0, n, selected, deque())
    # for p in permutations(range(n), n):
    #     n_queen(n, p)
    print(cnt)

if __name__ == "__main__":
    boj9663()

