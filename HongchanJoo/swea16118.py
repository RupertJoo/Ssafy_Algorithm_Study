def swea16118():
    for t in range(1,int(input() + 1)):
        n, m = map(int, input().split())
        values = list(map(int, input().split()))

        max_value = 0
        min_value = 0
        for i in range(n - m + 1):
            sum_value = 0
            for j in range(i, i + m):
                sum_value += values[j]
            if max_value < sum_value:
                max_value = sum_value
            if min_value == 0 or min_value > sum_value:
                min_value = sum_value

        list_sum_values = []
        #     list_sum_values.append(sum_value)
        # for i in range(n - m, 0 ,-1):
        #     for j in range(0, i):
        #         if list_sum_values[j] > list_sum_values[j + 1]:
        #             list_sum_values[j], list_sum_values[j + 1] = list_sum_values[j + 1], list_sum_values[j]
        # print(f"#{t} {list_sum_values[-1] - list_sum_values[0]}")
        #


        print(f"#{t} {max_value - min_value}")
    pass

if __name__ == "__main__":
    swea16118()


def counting_sort(a, b, k):

    c = [0] * (k + 1)

    for i in rnage(0, len(A)):
        pass

    cam += 1

    c