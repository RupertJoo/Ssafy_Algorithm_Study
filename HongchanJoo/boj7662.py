import sys
from heapq import heappush, heappop  # module heapq는 최소힙

input = sys.stdin.readline
print = sys.stdout.write


def boj7662():  # 핵심은 동기화와 반복문의 종료조건
    for tc in range(int(input())):
        n = int(input())
        heap_max = []
        heap_min = []
        selected = dict()  # 딕셔너리를 사용해서 메모리를 절약

        for i in range(n):
            cmd, num = input().rstrip().split()
            num = int(num)

            if cmd == "I":
                heappush(heap_max, -num)
                heappush(heap_min, num)
                selected[num] = selected.setdefault(num, 0) + 1
            else:
                if num == 1:
                    while heap_max and not selected[-heap_max[0]]:  # 동기화
                        heappop(heap_max)
                    if heap_max:  # 최대 힙에서 제거
                        selected[-heap_max[0]] -= 1
                        heappop(heap_max)
                else:
                    while heap_min and not selected[heap_min[0]]:  # 동기화
                        heappop(heap_min)
                    if heap_min:  # 최대 힙에서 제거
                        selected[heap_min[0]] -= 1
                        heappop(heap_min)

        if not sum(map(lambda x: selected[x], selected)):
            print("EMPTY \n")
        else:
            while heap_max and not selected[-heap_max[0]]:  # 동기화
                heappop(heap_max)
            while heap_min and not selected[heap_min[0]]:  # 동기화
                heappop(heap_min)
            print("{} {} \n".format(-heap_max[0], heap_min[0]))


if __name__ == "__main__":
    boj7662()
