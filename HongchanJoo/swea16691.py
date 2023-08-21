def preorder(t): # V-> L -> R
    global count
    global child_left
    global child_right
    if t:
        count += 1
        preorder(child_left[t])
        preorder(child_right[t])



def swea16691():
    global count
    global child_left
    global child_right

    for tc in range(1, int(input()) + 1):
        e, n = map(int, input().split())
        tree = list(map(int, input().split()))
        count = 0
        child_left = [0] * (e + 2)
        child_right = [0] * (e + 2)

        for i in range(e):
            p = tree[i * 2]
            c = tree[i * 2 + 1]
            if not child_left[p]:
                child_left[p] = c
            else:
                child_right[p] = c
        count = 0
        preorder(n)
        print(f"#{tc} {count}")


if __name__ == "__main__":
    swea16691()