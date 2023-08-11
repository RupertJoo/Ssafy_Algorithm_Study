def boj1439():
    text = input()
    num_0 = 0
    count_0 = 0
    num_1 = 0
    count_1 = 0

    chr_now = text[0]
    for i in text[1:]:
        if chr_now != i:
            chr_now = i
            if i == '0':
                num_0 += 1
            else:
                num_1 += 1
    if num_0 < num_1:
        result = num_0
    else:
        result = num_1

    print(result)


if __name__ == "__main__":
    boj1439()




