def boj2475():
    lst = list(map(int, input().split()))
    print(sum(map(lambda x: x ** 2, lst)) % 10)


if __name__ == "__main__":
    boj2475()