def swea1208():
    tc = 10
    for t in range(1, tc + 1):
        num_dump = int(input())
        dumps = list(map(int, input().split()))
        dict_dumps = {}
        for i in dumps:
            dict_dumps[i] = dict_dumps.setdefault(i,0) + 1
        result = dict_dumps
        print(f"#{t} {result}")
    pass

if __name__ == "__main__":
    swea1208()