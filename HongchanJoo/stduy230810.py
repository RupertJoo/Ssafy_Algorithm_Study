"""
V E
v1 w1 v2 v2....
7 8

1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
그래프에서 나중에 구체적으로 다룰 것이다.
그래프의 저장방식
인접행렬
인접리스트
0[0]
1[2,3]
2[1,4,5]
...
"""
# def dfs(n, v, adj_m):
#     stack = []  # 스택 생성
#     visited = [0] * (v + 1)  # visited 생성
#     visited[n] == 1  # 시작점 방문 표시
#     print(n)  # do[n]
#     while True:
#         for w in range(1, v):
#             if adj_m [n][w] == 1 and visited[w] == 0:
#                 stack.append(n)  # push(n), v = w
#                 n = w
#                 print(n)  # do(w)
#                 visited[n] = 1 # w 방문 표시
#                 break  # for w, n에 인접인 w c 찾은경우
#         # 현재 정점 n에 인접하고 미방문 w 표시
#         else:
#             if stack:  # 스택에 지나온 정점이 남아있으면
#                 n = stack.pop()  # pop()해서 다른 w 찾기
#             else:  # t스택이 비어있으면면
#                 break  # while True 탐색 끝끝
#
#
# v, e = map(int, input().split())  # 1번부터 v번의 정점,e개의 간선
# arr = list(map(int, input().split()))
# adj_m = [[0]*(v + 1) for _ in range(v + 1)]
# for i in range(e):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1
# dfs(1, v,adj_m)



# DFS
# s: 시작 정점의 번호
# v: 점점의 갯수
# def dfs(s, v):
#     visited = [0] * v
#     stack = []
#
#     # 시작 정점은 방문했다고 처리한다.
#     visited[s] = 1
#     print(node[s])
#     # i: 현재 방문한 정점
#     i = s
#
#     # 모든 정점을 방문할 때까지 반복, 다만 그 횟수를 알 수 없으므로
#     # while로 반복문을 짠 후, 조건에 맞추어 탈출하도록 한다.
#     while True:
#         # 현재 정점에서 탐색가능한 정점의 존재여부 확인
#         # i에서 다른 정점 j로 갈 수 있는 길을 어떻게 확인할까?
#         # 인접행렬 or 인접리스트로!
#         # adj_m == 1 이 때 갈 수 있다!!
#         for j in range(v):
#             # 이전에 정점 j의 방문여부 확인 (방문한 적이 없어야 갈 수 있다!)
#             if adj_m[i][j] == 1 and not visited[j]:
#                 #정점 j룰 방문하기에 이전 정점i로 되돌아가기 위해
#                 stack.append(i)
#                 # 정점 j에서 할 일
#                 print(node[j])
#                 # 방문처리
#                 visited[j] = 1
#                 # 현재 위치를 j로 바꾼 후 다음탐색을 진행한다.
#                 i = j
#                 # 새로운 i에서 방문하기 위해 break로 탈출한다.
#                 break
#         else: # i에서 탐색을 마쳤을 때(더 이상 탐색할 정점이 없다)
#             # 가장 최근의 정점으로 돌아가기
#             if stack: # stack 안에 원소가 있다(돌아갈 곳이 있다)
#                 i = stack.pop()
#             else: # stack 안에 원소가 없다(탐색을 마쳤으므로 반복을 마친다.
#                 break
#     return


# 그래프의 형태를 나타내기 위해 어떤 방법을 사용할까?
# 1. 인접행렬(2차원 배열)
# 1번 정점에서 2번 정점으로 가는 길이 있다
# adj_m[1][2] = 1
# 2번 정점에서 3번 정점으로 가는 길이 없다.
# adj_[2][3] = 0
# 무향 그래프는 대칭행렬, 유향 그래프는 비대칭행렬
#        A  B  C  D  E  F  G


# adj_m = [
#         [0, 1, 1, 0, 0, 0, 0],  # A
#         [1, 0, 0, 1, 1, 0, 0],  # B
#         [1, 0, 0, 0, 1, 0, 0],  # C
#         [0, 1, 0, 0, 0, 1, 0],  # D
#         [0, 1, 1, 0, 0, 1, 0],  # E
#         [0, 0, 0, 1, 1, 0, 1],  # F
#         [0, 0, 0, 0, 0, 1, 0]   # G
#         ]
# node = ["A", "B", "C", "D", "E", "F", "G"]
# n = 7
# dfs(0, n)

# 인접리스트
# adj_l[i] => 정점i와 연결되어 있는 정점의 모음
# adj_l[A] = [B,C]

"""
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
"""

def dfs_1(s, v):
    visited = [0] * (v + 1)
    stack = []
    # 시작정점 i를 방문처리
    i = s
    visited[i] = 1
    print(i)
    # 모든 정점을 방문할 때까지 반복
    while True:
        # 현재 정점 i에서 갈 수 있는 정점 j 찾기
        for j in adj_l[i]:
            # j는 i와 연결된 정점이므로 j의 방문여부만을 확인하고 탐색한다.
            if visited[j] == 0:
                stack.append(i) # 방문 정점 기억
                i = j # 새로운 i에서 탐색 시작
                visited[j] = 1
                print(i)
                break
        else: # 현재 갈 수 있는 정점이 없다면..
            if stack:
                i = stack.pop()
            else:
                break


v, ee = map(int, input().split())
adj_l = [[] for _ in range(v + 1)]
for i in range(ee):
    # 연결의 시점: s, 종점: e
    s, e = map(int, input().split())
    adj_l[s].append(e)
    adj_l[e].append(s)

dfs_1(1, v)


# v, ee = map(int, input().split())
# adj_lst = [[] for _ in range(v + 1)]
# for j in range(ee):
#     s, e = map(int, input().split())
#     adj_lst[s].append(e)
#     adj_lst[e].append(s)
#
# visited = [0] * (v + 1)
# visited[1] = 1
# # now : 현재 정점
# def dfs_2(now):  # 재귀는 모든 정점을 방문할 때 까지
#     print(now)  # 현재 정점 출력
#     # 현재 정점에서 방문가능한 정점을 찾아 방문한다.
#     for next in adj_lst[now]:  # 점점 now 에서 방문가능한 next 정점
#         if not visited[next]:
#             visited[next] = 1  # 방문 처리
#             dfs_2(next)  # 재귀 호출
#
# dfs_2(1)