def boj13023():
    n, m = map(int, input().split())
    friends = list(set([i, i + 1]) for i in range(n))
    arr = [1] * n
    friends_i = list(set(map(int, input().split()))for i in range(m))
    # print(friends)
    # print(friends_i)
    ans = 1
    for friend in friends_i:
        if friend in friends:
            print(friend)
            arr[min(friend)] = 0
    print(sum(arr))

if __name__ == "__main__":
    boj13023()