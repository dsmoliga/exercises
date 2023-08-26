class User:
    age = 0

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_age(self):
        print(f'Age: {self.age}, {self.name}')


user1 = User(25, "Daniel")
user2 = User(45, "Arek")

user1.print_age()
user2.print_age()
