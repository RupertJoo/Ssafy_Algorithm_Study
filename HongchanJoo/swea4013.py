def drive(gearbox, cmd):
    n, d = cmd
    n -= 1

    gear_temp = [0] * 8
    rl = gearbox[n][2]
    lr = gearbox[n][6]
    for i, j in enumerate(gearbox[n]):
        gear_temp[(i + d) % 8] = j
    gearbox[n] = gear_temp

    # right
    if n < 3 and rl != gearbox[n + 1][6]:
        d_right = d * -1
        rotatable_right = True
    else:
        rotatable_right = False
    # left
    if n > 0 and lr != gearbox[n - 1][2]:
        d_left = d * -1
        rotatable_left = True
    else:
        rotatable_left = False

    # right
    for ii in range(n + 1, 4):
        if rotatable_right:
            rl = gearbox[ii][2]
            gear_temp = [0] * 8
            for i, j in enumerate(gearbox[ii]):
                gear_temp[(i + d_right) % 8] = j
            gearbox[ii] = gear_temp
            if ii == 3:
                break
            if ii == 3 or (ii < 3 and rl != gearbox[ii + 1][6]):
                d_right *= -1
                rotatable_right = True
            else:
                rotatable_right = False
        else:
            break

    # left
    for ii in range(n - 1, -1, -1):
        if rotatable_left:
            lr = gearbox[ii][6]
            gear_temp = [0] * 8
            for i, j in enumerate(gearbox[ii]):
                gear_temp[(i + d_left) % 8] = j
            gearbox[ii] = gear_temp
            if ii == 0:
                break
            if ii == 0 or (ii > 0 and lr != gearbox[ii-1][2]):
                d_left *= -1
                rotatable_left = True
            else:
                rotatable_left = False
        else:
            break

    return gearbox


def swea4013():
    for tc in range(1, int(input()) + 1):
        n_cmd = int(input())
        gearbox = [list(map(int, input().split())) for _ in range(4)]
        list_cmd = [list(map(int, input().split())) for _ in range(n_cmd)]

        for i in range(n_cmd):
            gearbox = drive(gearbox, list_cmd[i])

        ans = 0
        for i in range(4):
            ans += gearbox[i][0] * (1 << i)
        print(f"#{tc} {ans}")

if __name__ == "__main__":
    swea4013()