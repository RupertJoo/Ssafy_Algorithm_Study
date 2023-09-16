import sys
input = sys.stdin.readline
print = sys.stdout.write


def boj1620():
    n, m = map(int, input().rstrip().split())
    dict_poke = dict()
    dict_poke_rev = dict()
    for i in range(n):
        poke = input().rstrip()
        dict_poke[poke.lower()] = i + 1
        dict_poke_rev[i + 1] = poke

    for _ in range(m):
        ip = input().rstrip()
        if ip[0] in "0123456789":
            print("{} \n".format(dict_poke_rev[int(ip)]))
        else:
            print("{} \n".format(dict_poke[ip.lower()]))


if __name__ == "__main__":
    boj1620()

