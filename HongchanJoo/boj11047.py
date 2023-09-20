# def boj11047():
#     n, k = map(int, input().split())
#     coins = [int(input()) for _ in range(n)]
#     # coins.sort(reverse=True)
#     cnt = 0
#
#     for c in coins[::-1]:
#         cc, k = divmod(k, c)
#         cnt += cc
#     print(cnt)
#
#
# if __name__ == "__main__":
#     boj11047()


from collections import deque
global diff

def get_count(k, coins):
    global diff
    q = deque()
    vc = {0: 0}
    q.append(0)

    while q:
        v_now = q.popleft()
        if v_now == k:
            return vc[v_now]
        for c in coins:
            v_nxt = v_now + c
            if v_nxt <= k and diff > k - v_nxt:
                vc[v_nxt] = vc[v_now] + 1
                q.append(v_nxt)
                diff = k - v_nxt

def boj11047():
    global min_cnt
    global diff
    diff = float("inf")
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort(reverse=True)
    min_cnt = get_count(k, coins)
    print(min_cnt)


if __name__ == "__main__":
    boj11047()