def isEmpty(front, rear):
    return front == rear


def isFull(len_q, front, rear):
    return rear - front == len_q

def enqOven(x):
    global n
    global oven
    global front_oven
    global rear_oven

    if isFull(n, front_oven, rear_oven):
        return
    rear_oven += 1
    oven[rear_oven] = x


def deqOven():
    global front_oven
    global rear_oven
    if isEmpty(front_oven, rear_oven):
        return
    front_oven += 1
    return oven[front_oven]

def deqPizza():
    global front_pizza
    global rear_pizza
    if isEmpty(front_pizza, rear_pizza):
        return
    front_pizza += 1
    return pizza[front_pizza]

def swea16638_2():
    MAX = 1_000
    global m
    global pizza
    global front_pizza
    global rear_pizza

    global n
    global oven
    global front_oven
    global rear_oven

    for tc in range(1, int(input()) + 1):
        result = None
        n, m = map(int, input().split())  # n: 화덕의 크기, m: 피자의 갯수
        pizza = list(map(lambda x,y: [x,y], list(range(1, m + 1)), list(map(int, input().split()))))
        front_pizza = -1
        rear_pizza = m - 1
        oven = [0] * MAX
        front_oven = rear_oven = -1

        while not isFull(n, front_oven, rear_oven) and not isEmpty(front_pizza, rear_pizza):
            enqOven(deqPizza())

        while not isEmpty(front_oven, rear_oven):
            idx, cheese = deqOven()
            cheese //= 2
            if cheese == 0:
                if not isEmpty(front_pizza, rear_pizza):
                    enqOven(deqPizza())
                else:
                    pass
            else:
                enqOven([idx, cheese])

        print(f"#{tc} {oven[rear_oven][0]}")


if __name__ == "__main__":
    swea16638_2()