def solve2056():
    t = int(input())
    for i in range(1, t + 1):
        
        
        yyyymmdd = input()
        yyyy = int(yyyymmdd[:4])
        mm = int(yyyymmdd[4:6])
        dd = int(yyyymmdd[6:])

        n_day = [0, 31, 28, 31, 30,
                 31, 30, 31, 31,
                 30, 31, 30, 31]
        ans = True    

        if yyyy < 0:
            ans = False
        else:
            if mm < 0 or mm > 13:
                ans = False  
            else:
                if dd > n_day[mm]:
                    ans = False 
                else:
                    pass
                
        if ans != False:
            print(f"#{i} ",end = '')
            print("{0:04d}".format(yyyy), "{0:02d}".format(mm), "{0:02d}".format(dd), sep='/')
        else:
            print(f"#{i} -1")


if __name__ == "__main__":
    solve2056()