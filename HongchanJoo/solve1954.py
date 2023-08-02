def solve1954():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        nn = n
        array = []
        for _ in range(n):
            array.append(n * [0])
        ii = 0
        jj = 0
        x_array = 1
        array[ii][jj] = 1  
        if n % 2 == 1:
            for _ in range(n - 1):
                jj += 1
                x_array += 1
                array[ii][jj] = x_array
            for  _ in range((n - 1) // 2):
                for _ in range(nn - 1):
                    ii += 1
                    x_array += 1
                    array[ii][jj] = x_array
                    
                for _ in range(nn - 1):
                    jj -= 1
                    x_array += 1
                    array[ii][jj] = x_array
                for _ in range(nn - 2):
                    ii -= 1
                    x_array += 1
                    array[ii][jj] = x_array
                for _ in range(nn - 2):
                    jj += 1
                    x_array += 1
                    array[ii][jj] = x_array
                nn -= 2
            pass
        else:
            for _ in range(n - 1):
                jj += 1
                x_array += 1
                array[ii][jj] = x_array
            for _ in range(n - 1):
                ii += 1
                x_array += 1
                array[ii][jj] = x_array   
            for _ in range(n - 1):
                jj -= 1
                x_array += 1
                array[ii][jj] = x_array    
            for  _ in range((n - 2) // 2):
                for _ in range(nn - 2):
                    ii -= 1
                    x_array += 1
                    array[ii][jj] = x_array
                    
                for _ in range(nn - 2):
                    jj += 1
                    x_array += 1
                    array[ii][jj] = x_array
                for _ in range(nn - 3):
                    ii += 1
                    x_array += 1
                    array[ii][jj] = x_array
                for _ in range(nn - 3):
                    jj -= 1
                    x_array += 1
                    array[ii][jj] = x_array
                nn -= 2                 

            pass

        print(f'#{i}')
        for j in range(n):
            print(*array[j])
    pass

if __name__ == "__main__":
    solve1954()