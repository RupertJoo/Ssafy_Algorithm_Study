# def calDist(n, m, azi_i, dist_i, azi, dist):
#     move_ccw = [[-1, 0], [0, -1], [0, 1], [1, 0]]
#     dist_min_ccw = 0
#     move_cw = [[1, 0], [0, 1], [0, -1], [-1, 0]]
#     dist_min_cw = 0
#
#     azi_ccw = azi
#     r = c = None
#     if azi_ccw == 1:
#         r, c = 0, dist
#     elif azi_ccw == 2:
#         r, c = m, dist
#     elif azi_ccw == 3:
#         r, c = dist, 0
#     elif azi_ccw == 4:
#         r, c = dist, n
#
#     azi_ccw = azi
#     # print(f" azi  = {azi_ccw}, r = {r}, c = {c}")
#     is_break = False
#
#     if (azi_ccw % 4) == (azi_i % 4) and dist == dist_i:
#         return 0
#     else:
#         for _ in range(5):
#             r_nxt = r + move_ccw[azi_ccw % 4][0]
#             c_nxt = c + move_ccw[azi_ccw % 4][1]
#             while 0 <= r_nxt <= m and 0 <= c_nxt <= n:
#                 if (azi_ccw % 4) == 0 or (azi_ccw % 4) == 3:
#                     # print("세로")
#                     if r_nxt == dist_i and (azi_ccw % 4) == (azi_i % 4):
#                         dist_min_ccw += 1
#                         is_break = True
#                         break
#                 else:
#                     # print("가로")
#                     if c_nxt == dist_i and (azi_ccw % 4) == (azi_i % 4):
#                         dist_min_ccw += 1
#                         is_break = True
#                         break
#                 if is_break:
#                     break
#                 r = r_nxt
#                 c = c_nxt
#                 # print(f" while azi  = {azi_ccw}, r = {r}, c = {c}")
#                 r_nxt = r + move_ccw[azi_ccw % 4][0]
#                 c_nxt = c + move_ccw[azi_ccw % 4][1]
#                 dist_min_ccw += 1
#             if is_break:
#                 break
#             # azi_ccw = (azi_ccw + 1) % 4
#             if azi_ccw % 4 == 0:
#                 azi_ccw = 1
#             elif azi_ccw % 4 == 1:
#                 azi_ccw = 3
#             elif azi_ccw % 4 == 2:
#                 azi_ccw = 0
#             elif azi_ccw % 4 == 3:
#                 azi_ccw = 2
#
#     azi_cw = azi
#     r = c = None
#     if azi_cw == 1:
#         r, c = 0, dist
#     elif azi_cw == 2:
#         r, c = m, dist
#     elif azi_cw == 3:
#         r, c = dist, 0
#     elif azi_cw == 4:
#         r, c = dist, n
#     # print(f" azi  = {azi_ccw}, r = {r}, c = {c}")
#     is_break = False
#     if (azi_cw % 4) == (azi_i % 4) and dist == dist_i:
#         return 0
#     else:
#         for _ in range(5):
#             r_nxt = r + move_cw[azi_cw % 4][0]
#             c_nxt = c + move_cw[azi_cw % 4][1]
#             while 0 <= r_nxt <= m and 0 <= c_nxt <= n:
#                 if (azi_cw % 4) == 0 or (azi_cw % 4) == 3:
#                     # print("세로")
#                     if r_nxt == dist_i and (azi_cw % 4) == (azi_i % 4):
#                         dist_min_cw += 1
#                         is_break = True
#                         break
#                 else:
#                     # print("가로")
#                     if c_nxt == dist_i and (azi_cw % 4) == (azi_i % 4):
#                         dist_min_cw += 1
#                         is_break = True
#                         break
#                 if is_break:
#                     break
#                 r = r_nxt
#                 c = c_nxt
#                 # print(f" while azi  = {azi_ccw}, r = {r}, c = {c}")
#                 r_nxt = r + move_cw[azi_cw % 4][0]
#                 c_nxt = c + move_cw[azi_cw % 4][1]
#                 dist_min_cw += 1
#             if is_break:
#                 break
#             # azi_ccw = (azi_ccw + 1) % 4
#             if azi_cw % 4 == 0:
#                 azi_cw = 2
#             elif azi_cw % 4 == 1:
#                 azi_cw = 0
#             elif azi_cw % 4 == 2:
#                 azi_cw = 3
#             elif azi_cw % 4 == 3:
#                 azi_cw = 1
#
#
#
#     if dist_min_cw > dist_min_ccw:
#          dist_min = dist_min_ccw
#     else:
#          dist_min = dist_min_cw
#
#     return dist_min
#
#
# def boj2654():
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(int(input()))]
#     azi, dist = map(int, input().split())
#
#     # print(arr)
#     # print(azi, dist)
#
#     ans = 0
#     for azi_i, dist_i in arr:
#         x = calDist(n, m, azi_i, dist_i, azi, dist)
#         # print(x)
#         ans += x
#
#         # print(azi_i, dist_i)
#     print(ans)
#
# if __name__ == "__main__":
#     boj2654()

def calDistCW(n, m, a, d):
    if a == 1:
        return d
    elif a == 2:
        return 2 * n + m - d
    elif a == 3:
        return 2 * (n + m) - d
    else:
        return n + d


def boj2654():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(int(input()))]
    azi, dist = map(int, input().split())

    dist_cw = calDistCW(n, m, azi, dist)
    ans = 0
    for azi_i, dist_i in arr:
        dist_i_cw = calDistCW(n, m, azi_i, dist_i)
        x = min(abs(dist_cw - dist_i_cw), 2 * (n + m) - abs(dist_cw - dist_i_cw))
        ans += x
    print(ans)


if __name__ == "__main__":
    boj2654()

