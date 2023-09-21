from sys import stdin
input = stdin.readline


def boj27866():
    text = input().rstrip()
    print(text[int(input())-1])


if __name__ == "__main__":
    boj27866()