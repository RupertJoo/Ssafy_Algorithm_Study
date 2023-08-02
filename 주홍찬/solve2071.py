def solve2071():
    t = int(input())
    for i in range(1, t + 1):
        numbers = list(map(int, input().split(' ')))
        mean = sum(numbers) / len(numbers)
        if mean - int(mean) < 0.5:
            mean_round = int(mean)
        else:
            mean_round = int(mean) + 1
        print(f"#{i} {mean_round}")
    pass



if __name__ == "__main__":
    solve2071()