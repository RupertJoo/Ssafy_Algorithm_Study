# import sys # build in module sys를 가져온다.

def swea16268():

    for tc in range(1, int(input()) + 1):
    # sys.stdin = open("./refs/input_swea_16268.txt") # 로컬에 저장된 인풋파일을 불러온다
    # for tc in range(1, int(sys.stdin.readline()) + 1): # 메서드 input()을 sys.stdin.readline()으로 대체한다.
        N, M = map(int, input().split()) # 배열의 크기 N, M
        arr = list(list(map(int, input().split()))for _ in range(N)) # 리스트 컴프리헨션으로 한줄로 구현 가능하다.
        list_dr = [-1, 1, 0, 0] # 열 방향
        list_dc = [0, 0, -1, 1] # 행 방향
        result = 0 # 초기 반환값
        for i in range(N): # 행 순회
            for j in range(M): # 열 순회
                value_sum = arr[i][j]
                for dr, dc in zip(list_dr, list_dc): # zip을 써서 순회 가능하다.
                    nr = i + dr
                    nc = j + dc
                    if 0 <= nr < N and 0 <= nc < M: # 좌표가 배열 내에 있을 때 더해준다.
                        value_sum += arr[nr][nc]
                if result < value_sum: # 반환값보다 최대값이 클 때 반환값을 갱신한다.
                    result = value_sum
        print(f"#{tc} {result}")

if __name__ == "__main__":
    swea16268()