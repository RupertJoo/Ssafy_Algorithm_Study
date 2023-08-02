# import sys
# sys.stdin = open("./refs/input_swea_4836.txt")

def fill_color(area_info,list_result):
    r_s, c_s, r_e, c_e, color = area_info
    for i in range(r_s, r_e + 1):
        for j in range(c_s, c_e + 1):
            list_result[i][j] += color
    return list_result


def swea4836():
    for tc in range(1, int(input()) + 1):
    # for tc in range(1, int(sys.stdin.readline()) + 1):
        N = int(input())
        list_area = list(list(map(int, input().split())) for _ in range(N))
        arr_result = list([0]* 10 for _ in range(10))
        result= 0

        for area_info in list_area:
            arr_result = fill_color(area_info, arr_result)
        for i in range(10):
            for j in range(10):
                if arr_result[i][j] == 3: result += 1
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea4836()