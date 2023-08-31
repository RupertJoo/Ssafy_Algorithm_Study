from itertools import combinations


def countReadableWords(words, learned):
   cnt = 0
   for word in words:
      readable = True
      for w in word:
          if not learned[ord(w)]:  # 단어 순회 중 배우지 않은 알파벳이 나올 경우
            readable = False  # 이 단어는 읽을 수 없으므로 다음 단어로 넘어간다.
            break
      if readable:  # 읽을 수 있을 때에는 cnt를 1 가산.
         cnt += 1
   return cnt


def boj1062():
    n, k = map(int, input().split())
    words = list(list(input())[4:-4] for _ in range(n))
    ans = 0
    learned_basic = {"a", "c", "i", "n", "t"}
    learned_yet = {chr(i) for i in range(97, 123)} - learned_basic

    if k >= 5:
      learned = [0] * 123
      for lb in learned_basic:
         learned[ord(lb)] = 1
      for learned_soon in list(combinations(learned_yet, k - 5)):  # 배워야 할 알파벳 리스트
         for ls in learned_soon:
            learned[ord(ls)] = 1
         cnt = countReadableWords(words, learned) # 조합으로부터 나온 알파벳을 배운 상태에서 몇개의 단어를 읽을지 세어야 한다.
         if ans < cnt:
            ans = cnt
         for ls in learned_soon:  # 다음 조합에서도 셀 수 있도록 초기화
            learned[ord(ls)] = 0
      print(ans)
    else:
       print(0)


if __name__ == "__main__":
    boj1062()
