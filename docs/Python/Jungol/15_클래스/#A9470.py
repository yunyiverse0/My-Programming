class j:
    def __init__(self, name, h, w):
        self.name = name
        self.h = int(h)
        self.w = float(w)

    def __str__(self):
        return self.name

people = []

for _ in range(5):
    name, h, w = input().split()
    people.append(j(name, h, w))

people.sort(key = lambda x: (x.h, x.w))

for i in people:
    print(i)
