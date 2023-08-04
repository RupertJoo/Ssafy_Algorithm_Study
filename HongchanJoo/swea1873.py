import sys
sys.stdin = open("./refs/input_swea_1873.txt")


def swea1873():
    for tc in range(1, int(sys.stdin.readline()) + 1):
    # for tc in int(input()):
        h, w = map(int, input().split())
        arr = list(list(input()) for _ in range(h))
        n = input()
        commands = list(input())

        terrain = ['.', '*', '#', '-']
        tank = ['^', 'v', '<', '>']
        actions = ['U', 'D', 'L', 'R', 'S']
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        is_break = False
        for i in range(h):
            for j in range(w):
                if arr[i][j] in tank:
                    is_break = True
                break
            if is_break:
                break
        r, c = i, j

        for cmd in commands:
            if cmd == 'U':
                pass
            elif cmd == 'D':
                pass
            elif cmd == 'L':
                pass
            elif cmd == 'R':
                pass
            elif cmd == 'S':
                pass
            pass
        print(f"#{tc}", end=" ")
        for row_arr in arr:
            print(*row_arr)
    pass


if __name__ == "__main__":
    swea1873()