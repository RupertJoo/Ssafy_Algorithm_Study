import copy
def rotateCube(cmd, cube):
    cube_copy = copy.deepcopy(cube)
    obj, d = list(cmd)
    dict_index = {"U": {"B": [[2, 0], [2, 1], [2, 2]], "R": [[0, 2], [0, 1], [0, 0]], "F": [[0, 2], [0, 1], [0, 0]], "L": [[0, 2], [0, 1], [0, 0]]},
                  "D": {"F": [[2, 0], [2, 1], [2, 2]], "R": [[2, 0], [2, 1], [2, 2]], "B": [[0, 2], [0, 1], [0, 0]], "L": [[2, 0], [2, 1], [2, 2]]},
                  "F": {"U": [[2, 0], [2, 1], [2, 2]], "R": [[0, 0], [1, 0], [2, 0]], "D": [[0, 2], [0, 1], [0, 0]], "L": [[2, 2], [1, 2], [0, 2]]},
                  "B": {"D": [[2, 0], [2, 1], [2, 2]], "R": [[2, 2], [1, 2], [0, 2]], "U": [[0, 2], [0, 1], [0, 0]], "L": [[0, 0], [1, 0], [2, 0]]},
                  "L": {"U": [[0, 0], [1, 0], [2, 0]], "F": [[0, 0], [1, 0], [2, 0]], "D": [[0, 0], [1, 0], [2, 0]], "B": [[0, 0], [1, 0], [2, 0]]},
                  "R": {"U": [[2, 2], [1, 2], [0, 2]], "B": [[2, 2], [1, 2], [0, 2]], "D": [[2, 2], [1, 2], [0, 2]], "F": [[2, 2], [1, 2], [0, 2]]}}
    temp_obj = [[None] * 3 for _ in range(3)]
    list_x = []

    if d == "+":
        for r in range(3):
            for c in range(3):
                temp_obj[c][2 - r] = cube[obj][r][c]
        cube[obj] = temp_obj
        list_idx = []
        for x, idx in dict_index[obj].items():
            list_x.append(x)
            list_idx.append(idx)
        list_x_cw = copy.deepcopy(list_x)
        list_x_cw = [list_x_cw.pop()] + list_x_cw
        list_idx_cw = copy.deepcopy(list_idx)
        list_idx_cw = [list_idx_cw.pop()] + list_idx_cw
        for i in range(4):
            x = list_x[i]
            x_nxt = list_x_cw[i]
            for rc_now, rc_nxt in zip(list_idx[i], list_idx_cw[i]):
                r_now, c_now = rc_now[0], rc_now[1]
                r_nxt, c_nxt = rc_nxt[0], rc_nxt[1]
                cube[x][r_now][c_now] = cube_copy[x_nxt][r_nxt][c_nxt]
    elif d == "-":
        for r in range(3):
            for c in range(3):
                temp_obj[r][c] = cube[obj][c][2 - r]
        cube[obj] = temp_obj
        list_idx = []
        for x, idx in dict_index[obj].items():
            list_x.append(x)
            list_idx.append(idx)
        list_x_ccw = copy.deepcopy(list_x)
        list_x_ccw = list_x_ccw + [list_x_ccw.pop(0)]
        list_idx_ccw = copy.deepcopy(list_idx)
        list_idx_ccw = list_idx_ccw + [list_idx_ccw.pop(0)]
        for i in range(4):
            x = list_x[i]
            x_nxt = list_x_ccw[i]
            for rc_now, rc_nxt in zip(list_idx[i], list_idx_ccw[i]):
                r_now, c_now = rc_now[0], rc_now[1]
                r_nxt, c_nxt = rc_nxt[0], rc_nxt[1]
                cube[x][r_now][c_now] = cube_copy[x_nxt][r_nxt][c_nxt]
    return cube


def boj5373():
    for tc in range(int(input())):
        cube = {"U": [["w"] * 3 for _ in range(3)],
                "D": [["y"] * 3 for _ in range(3)],
                "F": [["r"] * 3 for _ in range(3)],
                "B": [["o"] * 3 for _ in range(3)],
                "L": [["g"] * 3 for _ in range(3)],
                "R": [["b"] * 3 for _ in range(3)]}
        n = int(input())
        list_cmd = input().split()
        for cmd in list_cmd:
            cube = rotateCube(cmd, cube)
        for c in cube["U"]:
            print(*c, sep="")


if __name__ == "__main__":
    boj5373()
