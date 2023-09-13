import sys
input = sys.stdin.readline

def boj1927():
    n = int(input())
    heap = [0] * (n + 1)
    tail = 0
    for _ in range(n):
        cmd = int(input())
        if cmd:
            tail += 1
            heap[tail] = cmd
            child = tail
            parent = tail // 2
            while parent:
                if heap[parent] > heap[child]:
                    heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
                parent //= 2
            print(heap)
        else:
            if not tail:
                print(0)
            else:
                print(heap[1])
                heap[1] = heap[tail]
                tail -= 1
                parent = 1
                child = parent * 2
                while child <= tail:
                    if child + 1 <= tail and heap[child] > heap[child + 1]:
                        child += 1
                    if heap[parent] > heap[child]:
                        heap[parent], heap[child] = heap[child], heap[parent]
                    parent = child
                    child *= 2
                print(heap)



if __name__ == "__main__":
    boj1927()