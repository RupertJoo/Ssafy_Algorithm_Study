def deLQ():
    global pizza
    global front_pizza
    front_pizza += 1
    return pizza[front_pizza]

def enCQ(item):
    global n
    global rear_oven
    global oven

    rear_oven = (rear_oven + 1) % (n + 1)
    oven[rear_oven] = item


def deCQ():
    global n
    global front_oven
    global oven
    front_oven = (front_oven + 1) % (n + 1)
    return oven[front_oven]


def isEmptyLQ():
    global m
    global front_pizza

    return front_pizza == m - 1


def isEmptyCQ():
    global front_oven
    global rear_oven

    return front_oven == rear_oven


def isFullCQ():
    global n
    global front_oven
    global rear_oven

    return (rear_oven + 1) % (n + 1) == front_oven


def swea16638():
    global m
    global pizza
    global front_pizza

    global n
    global oven
    global front_oven
    global rear_oven

    for tc in range(1, int(input()) + 1):
        result = 1
        n, m = map(int, input().split()) #  n: 화덕의 크기, m: 피자의 갯수
        pizza = list(map(int, input().split()))
        list_cnt = list(range(1, m + 1))
        pizza = list(map(lambda x, y: [x, y], list_cnt, pizza))
        # print(pizza)
        front_pizza = -1
        oven = [0] * (n + 1)
        front_oven = rear_oven = 0

        i = 0
        while not isFullCQ() and not isEmptyLQ():
            enCQ(deLQ())
        # print(oven)
        # print(front_pizza)

        while not isEmptyCQ():
            # print(front_oven, rear_oven)
            temp0, temp1 = deCQ()
            temp1 //= 2
            if temp1 == 0:
                if not isEmptyLQ():
                    # print("새거넣을게")
                    enCQ(deLQ())
                else:
                    pass
            else:
                enCQ([temp0, temp1])
            # print(oven[rear_oven][0])
        print(f"#{tc} {oven[rear_oven][0]}")

if __name__ == "__main__":
    swea16638()
