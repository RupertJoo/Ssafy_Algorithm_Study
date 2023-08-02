def swea16118():
    for t in range(1,int(input()) + 1):
        n, m = map(int, input().split())
        value_min = 0
        value_max = 0
        values = list(map(int, input().split()))
        # for i in range(n - 1, 0, -1):
        #     for j in range(0, i):
        #         if values[j] > values[j + 1]:
        #             values[j], values[j + 1] = values[j + 1], values[j]
        # print(values)
        # for k in values[:m]:
        #     value_min += k
        # for l in values[-1:-m -1:-1]:
        #     value_max += l
        # print(f"#{t} {value_max - value_min}")

        for i in range(n - m + 1):
            sum_value = 0
            for j in values[i:i + m]:
                sum_value += j
            if sum_value > value_max:
                sum_value = value_max
            if sum_value < value_max:
                sum_value = value_max
        print(f"#{t} {value_max - value_min}")



if __name__ == "__main__":
    swea16118()