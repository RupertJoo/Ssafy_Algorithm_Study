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
            i = 1
            while cq[rear] != 0:
                temp = deCQ()
                if temp - i < 0:
                    temp = 0
                else:
                    temp -= i
                enCQ(temp)
                i += 1

            print(f"#{tc}", end=' ')
            # print(*cq)
            for ii in range(len_cq - 1):
                print(cq[(front+ii) % len_cq], end=" ")
            print()
            # print("www")

        except:
            return


if __name__ == "__main__":
    swea1225()