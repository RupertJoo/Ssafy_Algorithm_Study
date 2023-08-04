def solve1945():
    t = int(input())
    for iii in range(1, t + 1):
        n = int(input())
        abcde = [0]*5
        primes = [2, 3, 5, 7, 11]
        idx = 0
        for i in primes:
            while n % i == 0:
                n = n // i
                abcde[idx] += 1
            idx += 1
        ans = abcde
        # ans = list(range(1,6))
        print(f"#{iii}", *ans,sep=' ')
        pass
    pass


if __name__ == "__main__":
    solve1945()