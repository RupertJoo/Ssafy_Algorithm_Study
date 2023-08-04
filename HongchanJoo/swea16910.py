def swea16910():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        list_x = list(range(-n, n + 1))
        list_y = list(range(-n, n + 1))
        result = 0
        for i in list_x:
            for j in list_y:
                if i ** 2 + j ** 2 <= n ** 2:
                    result += 1
        print(f"#{tc} {result}")
    pass


if __name__ == "__main__":
    swea16910()



# def swea():
#     pass
#
#
# if __name__ == "__main__":
#     swea()