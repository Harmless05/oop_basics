class Person():
    name = "Person name"
    age = 0

    def setPerson(self, name, age):
        self.age = age
        self.name = name

    def birthday(self):
        self.age = self.age + 1

    def info(self):
        print(self.name)
        print(self.age)