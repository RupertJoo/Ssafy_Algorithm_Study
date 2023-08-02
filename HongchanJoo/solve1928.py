'''
def solve1928():
    b64 = []
    b64_0_25 = list(map(lambda x: chr(x), range(65, 91)))
    b64_26_51 = list(map(lambda x: chr(x), range(97, 123)))
    b64_52_61 = list(map(lambda x: chr(x), range(48, 58)))
    b64_52_63 = ['+','/']

    b64 += b64_0_25
    b64 += b64_26_51
    b64 += b64_52_61
    b64 += b64_52_63

    t = int(input())
    for i in range(1, t + 1):
        y = list(input())
        # print(y)
        vv = []
        for j in y:
            # print('0'+str(bin(ord(j)))[2:])
            jj = str(bin(b64.index(j)))[2:].zfill(6)
            vv.append(jj)
        # print(f"#{i} {y}")
        # print(f"#{i} {vv}")
        pass
        vvv = []
        for iii in range(len(vv) // 4):
            pink = ''
            for iiii in range(4):
                pink += vv[4*iii + iiii]
            
            string_0 = chr(int(pink[0:8],2))
            string_1 = chr(int(pink[8:16],2))
            string_2 = chr(int(pink[16:24],2))
            vvv.extend([string_0, string_1, string_2])
        print(f"#{i} ", *vvv, sep='')
    pass

if __name__ == "__main__":
    solve1928()
    #TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u
'''

def solve1928():
    table = {keyTable: valueTable for valueTable, keyTable in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
    for testCase in range(1,int(input()) + 1):
        words = input()
        bit_l = ''.join([bin(table[i])[2:].zfill(6) for i in words])
        result = ''.join(chr(int(bit_l[j:j+8],2)) for j in range(0,len(bit_l),8))
        print(f"#{testCase} {result}")

    pass

if __name__ == "__main__":
    solve1928()


'''
'''