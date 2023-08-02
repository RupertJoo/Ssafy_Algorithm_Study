def solve1926():
    x = int(input())
    numbers = list(map(str,range(1, x + 1))) 
    numbers2 = list(range(1,x + 1))
    list_369 = ['3','6','9']
    for i in range(len(numbers2)):
        ii = list(numbers[i])
        num_369 = 0
        for j in ii:
            if j in list_369:
                num_369 += 1
        if num_369 != 0:
            numbers2[i] = '-' * num_369
    print(*(i for i in numbers2), sep=' ')

    

if __name__ == "__main__":
    solve1926()