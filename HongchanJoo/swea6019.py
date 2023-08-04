"""
def swea6019():
    for tc in range(1, int(input()) + 1):
        dist, a, b, f = map(int, input().split())
        alpha = (f - a) / (f + a)
        beta = (f - b) / (f + b)
        t1 = f * dist / (f + b)
        result = t1 * (1 + alpha) * (1 / (1 - alpha * beta))
        print(f"#{tc} {result}")
    pass


if __name__ == "__main__":
    swea6019()
"""
def boj9469():
    for tc in range(1, int(input()) + 1):
        _, dist, a, b, f = map(float, input().split())
        alpha = (f - a) / (f + a)
        beta = (f - b) / (f + b)
        t1 = f * dist / (f + b)
        result = t1 * (1 + alpha) * (1 / (1 - alpha * beta))
        print(f"{tc} {result}")
    pass


if __name__ == "__main__":
    boj9469()