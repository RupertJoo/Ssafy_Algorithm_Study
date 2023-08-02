
# return == 0: 충전소가 없다
# return >= 0: 충전소가 배치되어 있다.
# 최대 거리만큼 이동하되, 충전기가 없을 경우 한칸씩 뒤로빼며
# 충전소 확인

def swea16192():
    # 테스트케이스
    for tc in range(1, int(input()) + 1):
        # k: 최대 이동거리 n: 종점, m: 충전소의 수
        k, n, m = map(int, input().split())
        charge = list(map(int, input().split()))
        stop = [0] * n
        count = 0
        for i in charge:
            stop[i] = 1
        location = 0
        while location != n:
            if location >= n - k:
                location = n
                break
            else:
                chargeable = False
                for j in range(k, 0, -1):
                    if location + j >= n:
                        location = n
                        break
                    if stop[location + j] == 1:
                        location += j
                        count += 1
                        chargeable = True
                        break
                # 반복문의 범위에 항상 유의하자!!
                if chargeable == False:
                    count = 0
                    location = n
                    break
        print(f"#{tc} {count}")


if __name__ == "__main__":
    swea16192()
