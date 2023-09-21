from sys import stdin, stdout
input = stdin.readline
print = stdout.write


def is_prior():
    pass

def boj25618():
    n = int(input())
    cnt = 0
    classified = {i: 0 for i in range(1, 18)}
    roaster = [0] * (n + 1)
    powers = [0] * (n + 1)
    for i in range(n):
        n_roaster = list(map(int, input().split()))
        classified[n_roaster[0]] += 1 << i
        for r in n_roaster[1:]:
            roaster[i + 1] += 1 << r
        roaster[i + 1] >>= 1
    print("{} \n".format(classified))
    print("{} \n".format(roaster))
    print("{} \n".format(powers[1:]))


if __name__ == "__main__":
    boj25618()


