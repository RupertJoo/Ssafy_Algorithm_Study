def swea5658():
    for tc in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        arr = list(input())
        cypher = set()
        q_n = n // 4

        for i in range(4):
            cypher.add(int(''.join(arr[i * q_n: (i + 1) * q_n]), 16))
            # print()

        for _ in range(1000):
            arr_temp = [0] * n
            for i, j in enumerate(arr):
                arr_temp[(i + 1) % n] = j
            arr = arr_temp
            cnt = 0
            for i in range(4):
                if int(''.join(arr[i * q_n: (i + 1) * q_n]), 16) in cypher:
                    cnt += 1
                else:
                    cypher.add(int(''.join(arr[i * q_n: (i + 1) * q_n]), 16))
            if cnt == 4:
                break

        cypher = list(cypher)
        cypher.sort(reverse=True)
        # print(cypher)
        print(f"#{tc} {cypher[k - 1]}")

if __name__ == "__main__":
    swea5658()