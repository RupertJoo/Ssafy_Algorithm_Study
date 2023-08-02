def swea16117():
    for t in range(1, int(input()) + 1):
        n = int(input())
        values = list(map(int, input().split()))

        for i in range(n - 1, 0 ,-1):
            for j in range(0, i):
                if values[j] > values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]
        print(f"#{t} {values[-1] - values[0]}")
    pass

if __name__ == "__main__":
    swea16117()