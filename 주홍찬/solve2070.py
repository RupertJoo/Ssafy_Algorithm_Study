def solve2070():
    t = int(input())
    for i in range(1, t + 1):
        x,y = map(int, input().split(' '))
        if x > y:
            ans = '>'
        elif x == y:
            ans = '='
        else:
            ans = '<'


        print(f"#{i} {ans}")
    pass

if __name__ == "__main__":
    solve2070()