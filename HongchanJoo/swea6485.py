import sys
# sys.stdin = open("./refs/input_swea_6485.txt")

def swea6485():
    # for tc in range(1, int(sys.stdin.readline()) + 1):
    for tc in range(1, int(input()) + 1):
        N = int(input())
        stops = list(list(map(int, input().split())) for _ in range(N))
        P = int(input())
        numbers = list(int(input()) for _ in range(P))
        result = [0] * (5000 + 1) # 정류장은 1 ~ 5000 까지지만 배열은 0 ~ 5000
        for i in range(N):
            for j in range(stops[i][0], stops[i][1] + 1): # 순회 범위가 stops[i][0] 이상 stops[i][1] 이하 임을 유념하자.
                result[j] += 1
        list_ans = list()
        for i in numbers:
            if result[i] != 0:
                list_ans.append(result[i])
            else:
                list_ans.append(0)
        print(f"#{tc}", *list_ans)

if __name__ == "__main__":
    swea6485()