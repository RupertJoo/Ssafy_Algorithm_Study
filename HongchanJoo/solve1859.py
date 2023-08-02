def solve1859():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        prices = list(map(int, input().split(' ')))
        # 초기 이득은는 0
        benefit = 0
        # 초기 판매가는 0
        sell = 0
        # 뒷편에 가장 큰 수가 나올 경우, 계산시간을 줄일 수 있다.
        for buy in prices[::-1]:
            # 판매가가 구매가 이하일 경우 판매가를 구매가로 갱신한다.
            if sell <= buy:
                sell = buy
            else:
                # 구매가보다 판매가가 클 경우에만 이익이 발생하므로
                benefit += sell - buy
        print(f"#{i} {benefit}")
    pass
if __name__ == '__main__':
    solve1859()
 

