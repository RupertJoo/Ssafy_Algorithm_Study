def peek():
    global cq
    global front
    global len_cq

    return cq[(front + 1) % len_cq]


def enCQ(item):
    global len_cq
    global cq
    global rear

    if isFull():
        return
    rear = (rear + 1) % len_cq
    cq[rear] = item
    return


def deCQ():
    global len_cq
    global cq
    global front
    if isEmpty():
        return

    front = (front + 1) % len_cq
    return cq[front]


def isEmpty():
    global front
    global rear

    return front == rear


def isFull():
    global len_cq
    global front
    global rear

    return (rear + 1) % len_cq == front


def swea1225():
    global len_cq
    global cq
    global rear
    global front

    while True:
        try:
            tc = int(input())
            cq = [0] + list(map(int, input().split()))
            len_cq = len(cq)
            front = 0
            rear = len_cq - 1
            i = 0
            isBreak = False
            while peek() - ((i % 5) + 1) > 0:
                temp = deCQ()
                if temp - (i % 5) + 1 < 0:
                    temp = 0
                    isBreak = True
                else:
                    temp -= (i % 5) + 1
                enCQ(temp)

                if isBreak:
                    break
                i += 1
            cq[front] = 0
            print(f"#{tc}", end=' ')
            for ii in range(2, len_cq + 1):
                print(cq[(front+ii) % len_cq], end=" ")
            print()
        except:
            return


if __name__ == "__main__":
    swea1225()