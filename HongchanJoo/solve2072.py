# 2072. 홀수만 더하기

def solve2072():
    for t in range(1, int(input()) + 1):
        list_t = list(map(int, input().split()))
        list_ans = [i for i in list_t if i % 2 == 1]
        ans = sum(list_ans)
        print(f"#{t} {ans}")

if __name__ == "__main__":
    solve2072()


