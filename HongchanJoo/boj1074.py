import sys
input = sys.stdin.readline
print = sys.stdout.write

def is_range(n, r_t, c_t, r_start, c_start, r_end, c_end):
    return r_start <= r_t < r_end and c_start <= c_t < c_end


def traversal_z(n, r_t, c_t, r_start, c_start, r_end, c_end):
    global cnt
    global is_break

    if not is_break:
        if not n:
            if r_t == r_start and c_t == c_start:
                is_break = True
                return
            cnt += 1
        else:
            r_mid = (r_start + r_end) >> 1
            c_mid = (c_start + c_end) >> 1
            half_n = n - 1

            if is_range(half_n, r_t, c_t, r_start, c_mid, r_mid, c_end):
                cnt += (1 << (n - 1)) ** 2
            if is_range(half_n, r_t, c_t, r_mid, c_start, r_end, c_mid):
                cnt += 2 * (1 << (n - 1)) ** 2
            if is_range(half_n, r_t, c_t, r_mid, c_mid, r_end, c_end):
                cnt += 3 * (1 << (n - 1)) ** 2

            if is_range(half_n, r_t, c_t, r_start, c_start, r_mid, c_mid):
                traversal_z(half_n, r_t, c_t, r_start, c_start, r_mid, c_mid)
            if is_range(half_n, r_t, c_t, r_start, c_mid, r_mid, c_end):
                traversal_z(half_n, r_t, c_t, r_start, c_mid, r_mid, c_end)
            if is_range(half_n, r_t, c_t, r_mid, c_start, r_end, c_mid):
                traversal_z(half_n, r_t, c_t, r_mid, c_start, r_end, c_mid)
            if is_range(half_n, r_t, c_t, r_mid, c_mid, r_end, c_end):
                traversal_z(half_n, r_t, c_t, r_mid, c_mid, r_end, c_end)


def boj1074():
    global cnt
    global is_break

    cnt = 0
    is_break = False
    n, r_t, c_t = map(int, input().rstrip().split())
    traversal_z(n, r_t, c_t, 0, 0, 1 << n, 1 << n)
    print("{} \n".format(cnt))


if __name__ == "__main__":
    boj1074()