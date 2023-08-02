def swea1206():
    # 테스트케이스 10회
    tc = 10
    for i in range(1, tc + 1):
        n = int(input())
        # 빌딩들의 높이를 리스트로 저장한다.
        buildings = list(map(int, input().split()))
        result = 0
        # buildings 양 끝 2칸씩은 건물이 없으므로
        for j in range(2, n - 2):
            max_height = 0
            # 건물 자신을 제외한 2칸 범위 내의 인덱스는 다음과 같다.
            for k in [j - 2, j - 1, j + 1, j + 2]:
                if max_height < buildings[k]:
                    max_height = buildings[k]
            value = buildings[j] - max_height
            # 조망권이 확보된 세대 수를 result에 더한다.
            if value > 0:
                result += value
        print(f"#{i} {result}")

if __name__ == "__main__":
    swea1206()