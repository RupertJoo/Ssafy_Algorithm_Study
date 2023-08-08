def swea16370():
    for tc in range(1, int(input()) + 1):
        str1 = ''.join(set(input()))
        str2 = input()
        dict_str = {}
        for i in str1:
            for j in str2:
                if j == i:
                    dict_str[i] = dict_str.setdefault(i, 0) + 1
        result = 0
        for v in dict_str.values():
            if result < v:
                result = v
        print(f"#{tc} {result}")


if __name__ == "__main__":
    swea16370()