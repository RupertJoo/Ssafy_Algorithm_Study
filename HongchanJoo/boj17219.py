import sys
input = sys.stdin.readline
print = sys.stdout.write

def boj17219():
    mail_pw = dict()
    filter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n, m = map(int, input().rstrip().split())
    for _ in range(n):
        mail, pw = input().rstrip().split()
        is_valid = True
        for p in pw:
            if p not in filter:
                is_valid = False
                break
        if is_valid:
            mail_pw[mail] = pw
    for _ in range(m):
        x = input().rstrip()
        ans = mail_pw.setdefault(x, 0)
        if ans:
            print("{} \n".format(ans))


if __name__ == "__main__":
    boj17219()
