def swea16904():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        list_se = [list(map(int, input().split())) for _ in range(n)]
        # 작업 종료시간을 기준으로 list_se를 정렬하면 된다. (key를 활용해보자)
        list_se.sort(key=lambda item: item[1])
        cnt = 0
        time = 0
        print(list_se)
        while list_se:
            next_work = list_se.pop(0)  # 다음 작업을 꺼내온다
            if next_work[0] >= time:  # 꺼낼 수 있는 조건에서
                cnt += 1
                time = next_work[1]  # 꺼낸 후 갱신한다.
        print(f"#{tc} {cnt}")


if __name__ == "__main__":
    swea16904()
