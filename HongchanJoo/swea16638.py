def peek():
    global cq
    global front

    if isEmpty():
        return -1
    return cq[(front + 1) % (n + 1)]

def enCQ(item):
    global n
    global cq
    global rear

    if isFull():
        return
    rear = (rear + 1) % (n + 1)
    cq[rear] = item
    return

def deCQ():
    global n
    global cq
    global front
    if isEmpty():
        return

    front = (front + 1) % (n + 1)
    return cq[front]


def isEmpty():
    global front
    global rear

    return front == rear


def isFull():
    global n
    global front
    global rear

    return (rear + 1) % (n + 1) == front


def swea16638():
    global n
    global cq
    global front
    global rear
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())
        cq = [0] + list(map(int, input().split()))
        front = 0
        rear = n
        for _ in range(m):
            enCQ(deCQ())
        print(f"#{tc} {peek()}")


if __name__ == "__main__":
    swea16638()
