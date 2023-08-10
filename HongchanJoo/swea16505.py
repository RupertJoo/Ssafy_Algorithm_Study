def swea16505():
    x = int(input())
    for tc in range(1, x + 1):

        n = (int(input()) // 10) - 1
        # arr = [[] for _ in range(n + 1)]
        # arr[0] = ["10"]
        # if len(arr) > 1:
        #     arr[1] = ["11", "1010", "20"]
        # for i in range(2, n + 1):
        #     for j in range(i - 1, -1, -1):
        #         # print(j, i - j - 1)
        #         for k in range(len(arr[j])):
        #             for kk in range(len(arr[i - j - 1])):
        #                 arr[i].append(arr[j][k] + arr[i - j - 1][kk])
        #                 # if arr[j][k] + arr[i - j - 1][kk] not in arr[i]:
        #                 #     arr[i].append(arr[j][k] + arr[i - j - 1][kk])
        #     arr[i] = list(set(arr[i]))
        # result = len(arr[n])

        arr = [None] * (n + 1)
        arr[0] = 1
        for i in range(1, n + 1):
            if i % 2 == 1:
                arr[i] = arr[i - 1] * 2 + 1
            else:
                arr[i] = arr[i - 1] * 2 - 1
        result = arr[n]
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16505()

n = int(input())//10
result = 1
for i in range(2, n + 1):
    if i % 2 == 0:
        result = result * 2 + 1
    else:
        result = result * 2 - 1

