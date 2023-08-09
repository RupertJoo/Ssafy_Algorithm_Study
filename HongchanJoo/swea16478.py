# 스택을 활용한 풀이
def swea16478():
    for tc in range(1, int(input()) + 1):
        text = input()

        max_len_text = 1000
        top = -1
        stack = [0] * max_len_text
        # 문자를 스택에 넣고
        top += 1
        stack[top] = text[0]
        for i in range(1, len(text)):
        # 두번째 문자부터 최근에 넣은 글자와 비교하여
        # 같다면 pop (top이 -1일 경우에는 무효)
            if top != -1 and stack[top] == text[i]:
                top -= 1
            else:
                # 다르면 push
                top += 1
                stack[top] = text[i]
        print(f"#{tc} {top + 1}")


if __name__ == "__main__":
    swea16478()





