def nqueen(i, n):
    global dr
    global dc
    global rows
    if i == n:
        print(rows)
    else:
        for col in range(n):
            if rows[col] == 0:
                rows[col] = 1
                nqueen(i + 1, n)
                rows[col] = 0



def swea2806():
    global dr
    global dc
    global rows
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for tc in range(1, int(input()) + 1):
        n = int(input())
        rows = [0] * n
        nqueen(0, n)
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea2806()