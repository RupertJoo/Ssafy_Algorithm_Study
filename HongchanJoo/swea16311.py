def counting_sort(arr, n, max_height): # 배열과 배열의 길이, 배열이 가질 수 있는 최대값을 인수로 받아 카운팅정렬된 배열을 반환한다.
    # n = 100
    # max_height = 100
    arr_count = [0] * (max_height + 1) #카운트 배열의 길이는 0 ~ max_height
    arr_sorted = [None] * n # 정렬된 배열의 길이는 원본 배열의 길이와 같다.
    # dump[i]를 인덱스로 갖는 배열 arr_count에 1씩 더해준다
    # 이는 인덱스 및 인덱스값이 각각 arr의 요소 값과 그 갯수에 대응한다.
    for i in range(n):
        arr_count[arr[i]] += 1 # 누적합을 요소로 갖도록 한다.
    for i in range(1, max_height + 1):
        arr_count[i] += arr_count[i - 1]
    # i가 n -1, n - 2, ..., 0 되도록 하기 위해서
    # 길이가 n인 배열 arr의 인덱스 최댓값은 n - 1이니까!
    for i in range(n - 1, -1 ,-1):
        arr_count[arr[i]] -= 1
        arr_sorted[arr_count[arr[i]]] = arr[i]
    return arr_sorted

def swea16311():
    for tc in range(1, int(input()) + 1):
        n = int(input())
        arr = list(map(int, input().split()))
        arr_sorted = counting_sort(arr, n, 100)
        arr_sorted_rev = arr_sorted[::-1]
        result = []
        for i in range(n // 2):
            result.append(arr_sorted_rev[i])
            result.append(arr_sorted[i])
        if n % 2 == 1:
            result.append(arr_sorted[n // 2])
        print(f"#{tc}",end=" ")
        print(*result)

if __name__ == "__main__":
    swea16311()