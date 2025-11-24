class Person:
    def __init__(self, h, w):
        self.h = int(h)
        self.w = float(w)

    def __add__(self, other):
        return Person(self.h + other.h, self.w + other.w)

    def __sub__(self, other):
        return Person(abs(self.h - other.h), abs(self.w - other.w))

    def __truediv__(self, other):
        return Person((self.h + other.h)//2, (self.w + other.w)/2)

    def __str__(self):
        return f"키: {self.h}, 몸무게: {self.w:.1f}"


mh, mw = input().split()
fh, fw = input().split()

me = Person(mh, mw)
friend = Person(fh, fw)

plus = me + friend
minus = me - friend
avg = me / friend

print(f"당신의 키와 몸무게를 입력하세요.친구의 키와 몸무게를 입력하세요.my {me}")
print(f"friend {friend}")
print(f"plus {plus}")
print(f"minus {minus}")
print(f"avg {avg}")
