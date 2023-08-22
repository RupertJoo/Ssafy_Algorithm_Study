def enq_heap(i):
    global heap_min
    global last

    last += 1
    heap_min[last] = i  # 힙에 i 추가
    child = last  # 자식노드와 부모노드 번호 설정
    parent = child // 2

    while parent and heap_min[child] < heap_min[parent]:  # 부모가 있으며 부모노드의 값이 자식노드보다 클 때
        heap_min[child], heap_min[parent] = heap_min[parent], heap_min[child]  # 두 노드 내의 값을 바꾸고
        child = parent  # 자식노드와 부모노드 번호를 갱신한다.
        parent //= 2


def swea16719():
    global heap_min
    global last

    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list(map(int, input().split()))
        heap_min = [0] * (n + 1)
        last = 0

        for i in arr:
            enq_heap(i)

        ans = 0
        nn = n
        while nn > 0:
            nn //= 2
            ans += heap_min[nn]
        print(*heap_min)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    swea16719()


