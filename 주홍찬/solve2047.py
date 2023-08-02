def solve2047():
    string = input().split('_')
    string_end = string.pop()
    for i in string:
        print(i.upper(),end='_')
    print(string_end.upper())
    # print(string)
    # string_end = string.pop()    
    # for j in string:
    #     print(j,sep='_',end='')
    # print(string_end)
    
    pass

if __name__ == "__main__":
    solve2047()