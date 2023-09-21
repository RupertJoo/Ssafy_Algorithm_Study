class jojo:
    def __init__(self):
        self.familia = None
        self.user_stand = {}
        self.sounds = {}

    def match(self, user, stand):
        if user not in self.familia:
            print(f"우리 죠스타 가에는 {user}라는 사람은 없다!!")
        self.user_stand[user] = stand

    def record(self, user, voice):
        if user not in self.familia:
            print(f"기록할 필요가 없군!")
            return
        self.sounds[user] = voice

    def shout(self, user):
        if user not in self.familia or not self.user_stand.get(user, 0):
            print(f"{user}라는 자의 기합은 들어본적이 없어!")
            return
        print(self.sounds[user][0:2] + self.sounds[user][2:] * 8 + "!!!!")


jj = jojo()
jj.familia = ["죠나단 죠스타", "죠셉 죠스타", "쿠죠 죠타로", "히가시카타 죠스케", "죠르노 죠바나", "쿠죠 죠린"]
jj.match("쿠죠 죠타로", "스타 플라티나")
# print(jj.user_stand)
jj.match("DIO", "The World")
# print(jj.user_stand)
jj.record("쿠죠 죠타로", "오라오라")
jj.shout("쿠죠 죠타로")

jj.record("히가시카타 죠스케", "도라라라")
jj.shout("히가시카타 죠스케")
# print(jj.user_stand)

jj.match("히가시카타 죠스케", "크레이지 다이아몬드")
jj.shout("히가시카타 죠스케")

jj.familia.append("죠니 죠스타")
jj.match("죠니 죠스타", "터스크")
print(jj.familia)
print(jj.user_stand)
jj.record("죠니 죠스타","이야아아")
jj.shout("죠니 죠스타")