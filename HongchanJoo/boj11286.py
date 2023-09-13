import sys

input = sys.stdin.readline
print = sys.stdout.write

def is_vaild(num1, num2):
    return abs(num1) > abs(num2) or (abs(num1) == abs(num2) and num1 > num2)


def boj11286():
    n = int(input())
    heap = [0] * (n + 1)
    tail = 0
    for _ in range(n):
        x = int(input())
        if x:
            tail += 1
            heap[tail] = x
            child = tail
            parent = tail // 2
            while parent:
                if is_vaild(heap[parent], heap[child]):
                    heap[parent], heap[child] = heap[child], heap[parent]
                child = parent
                parent //= 2
        else:
            if tail:
                # print(heap[1])
                print("{} \n".format(heap[1]))
                heap[1] = heap[tail]
                tail -= 1
                parent = 1
                child = parent * 2
                while child <= tail:
                    if child + 1 <= tail and is_vaild(heap[child], heap[child + 1]):
                        child += 1
                    if is_vaild(heap[parent], heap[child]):
                        heap[parent], heap[child] = heap[child], heap[parent]
                    parent = child
                    child *= 2
            else:
                # print(0)
                print("0 \n")

if __name__ == "__main__":
    boj11286()
