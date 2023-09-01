def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n


def bfs(r, c, n, arr):
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    len_q = 25 ** 2
    q = [[]] * len_q
    front = rear = 0
    rear = (rear + 1) % len_q
    q[rear] = [r, c]
    arr[r][c] = 0

    buildings = 0
    while front != rear:
        front = (front + 1) % len_q
        r_now, c_now = q[front]
        buildings += 1

        for dr, dc in move:
            r_nxt, c_nxt = r_now + dr, c_now + dc
            if is_valid(r_nxt, c_nxt, n) and arr[r_nxt][c_nxt]:
                rear = (rear + 1) % len_q
                q[rear] = [r_nxt, c_nxt]
                arr[r_nxt][c_nxt] = 0
    return arr, buildings

def boj2667():
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    cnt = 0
    list_buildings = []
    for r in range(n):
        for c in range(n):
            if arr[r][c]:
                arr, buildings = bfs(r, c, n, arr)
                cnt += 1
                list_buildings.append(buildings)
    list_buildings.sort()
    print(cnt)
    _ = [print(i) for i in list_buildings]


if __name__ == "__main__":
    boj2667()