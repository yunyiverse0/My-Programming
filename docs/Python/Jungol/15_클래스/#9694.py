

class p:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'My name is {self.name}.')
        print(f'I am {self.age} years old.')

Name, Age = input().split()
P = p(Name, Age)
