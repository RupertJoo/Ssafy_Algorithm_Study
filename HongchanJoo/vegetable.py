import sys
sys.stdin = open("./refs/vege.txt")


list_vege = list(sys.stdin.readline() for _ in range(8))
for i in list_vege:
    print(i,end='')
print()