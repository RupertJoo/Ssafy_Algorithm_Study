from itertools import combinations
def boj1759():
    alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "x"}
    vowels = {"a", "e", "i", "o", "u"}
    consonants = alphabet - vowels
    n, m = map(int, input().split())
    arr = list(input().split())
    arr.sort()
    # print(arr)
    for i in combinations(arr, n):
        set_i = set(i)
        if len(set_i & vowels) >= 1 and len(set_i & consonants) >= 2:
            print(''.join(i))

if __name__ == "__main__":
    boj1759()
