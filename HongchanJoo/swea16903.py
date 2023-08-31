def swea16903():
    global list_perm
    for tc in range(1, int(input()) + 1):
        n, m = map(int, input().split())  # n개의 컨테이너, m개의 트럭
        container = list(map(int, input().split()))
        truck = list(map(int, input().split()))
        container.sort(reverse=True)
        truck.sort(reverse=True)
        print(container)
        print(truck)
        weight = 0
        idx_truck = 0
        while container:
            c = container.pop(0)
            for i in range(idx_truck, m):
                if c <= truck[i]:
                    weight += c
                    idx_truck += 1
                    break
            if idx_truck == m:
                break
        print(f"#{tc} {weight}")




if __name__ == "__main__":
    swea16903()
