import sys
input = sys.stdin.readline

def boj1931():
    cnt = 0
    n = int(input())
    meetings =[list(map(int, input().split())) for _ in range(n)]
    meetings.sort(key=lambda x: (x[0], (x[1] - x[0])))
    # print(meetings)
    mt_start, mt_end = (float("inf"), 0)
    for i in range(n - 1, -1, -1):
        if meetings[i][1] <= mt_start:
            # print(meetings[i])
            mt_start, mt_end = meetings[i]
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    boj1931()