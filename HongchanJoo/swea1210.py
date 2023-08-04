import sys
sys.stdin = open("./refs/input_swea_1204.txt")
def solve1204():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        numbers = list(map(int, input().split()))
        n_numbers = [0] * (max(numbers) + 1)
        for number in numbers:
            n_numbers[number] += 1
        # print(n_numbers)
        n_numbers.reverse()
        ans = max(numbers) - n_numbers.index(max(n_numbers))
        print(f"#{i} {ans}")

if __name__ == "__main__":
    solve1204()