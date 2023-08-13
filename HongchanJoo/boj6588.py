# 골드바흐의 추측
import sys
def make_primes():
    MAX = 1_000_000
    primes = [False] * 2 + [True] * (MAX - 1)
    k = 2
    while 2 * k <= MAX:
        primes[2 * k] = False
        k += 1
    for i in range(3, int(MAX ** 0.5 + 1), 2):
        if primes[i]:
            k = 2
            while i * k <= MAX:
                primes[i * k] = False
                k += 1
    return primes


def boj6588():
    primes = make_primes()
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        else:
            for i in range(3, n + 1 // 2, 2):
                if primes[i] and primes[n -i]:
                    print(f"{n} = {i} + {n - i}")
                    break
            else:
                print( "Goldbach's conjecture is wrong.")



if __name__ == "__main__":
    boj6588()