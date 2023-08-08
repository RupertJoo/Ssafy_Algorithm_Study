def make_primes():
    MAX = 1_000_000
    dm, mm = divmod(MAX, 2)
    primes = [False, False, True] + [True, False] * dm + [True] * mm
    for i in range(3, int(MAX ** 0.5 + 1), 2):
        if primes[i] == True:
            k = 2
            while i * k <= MAX:
                primes[i * k] = False
                k += 1
    return primes


def swea4698():
    primes = make_primes()
    # print(primes[:50])
    for tc in range(1, int(input()) + 1):
        d, a, b = map(int, input().split())
        d = str(d)
        result = 0
        for i in range(a, b + 1):
            if primes[i] == True and d in str(i):
                result += 1
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea4698()
