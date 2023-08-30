def swea4012():  # 순열재귀로 풀면 시간초과 -> 비트마스킹으로 풀자!! (승호야고맙다!!)
    for tc in range(1, int(input()) + 1):
        n = int(input())
        sy = [list(map(int, input().split())) for _ in range(n)]
        ans = 1_000_000
        for i in range(1, 1 << (n - 1)):  # 공집합을 제외하고, 중복하는 일이 없도록 순회범위는 2^(n-1) - 1 까지만 한다.
            sy_a = []
            sy_b = []
            for j in range(n):  # 0, 1, ..., n - 1번째에 이르는, n개의 식재료에 대하여
                if i & (1 << j):
                    sy_a.append(j)
                else:
                    sy_b.append(j)
            if len(sy_a) == len(sy_b):  # 식재료의 갯수가 동등하게 나뉘어 졌을 때에
                sum_a_ith = 0
                for r in sy_a:  # 요소 2개의 순열이면 반복문을 쓰는게 더욱 간단하다.
                    for c in sy_a:
                        if r!= c: sum_a_ith += sy[r][c]
                sum_b_ith = 0
                for r in sy_b:
                    for c in sy_b:
                        if r!= c: sum_b_ith += sy[r][c]
                ans = min(ans, abs(sum_a_ith - sum_b_ith))  # 결과 갱신
        print(f"#{tc} {ans}")


if __name__ == "__main__":
     swea4012()
