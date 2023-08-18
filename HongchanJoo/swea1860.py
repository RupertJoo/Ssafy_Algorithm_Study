def bfs(q, m, k):
    fishbread = 0
    front = 0
    rear = len(q) - 1
    ii = 0
    # print(q)
    for i in range(len(q)):
        # print(fishbread)
        if ii == m:
            ii = 0
            fishbread += k
        if q[i]:
            fishbread -= q[i]
            # print(fishbread)
        if fishbread < 0:
            return "Impossible"
        ii += 1
    return "Possible"


def swea1860():
    MAX = 11_111
    for tc in range(1, int(input()) + 1):
        q = [0] * (MAX + 1)
        n, m, k = map(int, input().split())
        customer = list(map(int, input().split()))
        for i in customer:
            q[i] = 1

        ans = bfs(q, m, k)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea1860()