class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("제 이름은 " + self.name + "입니다.")
        print("나이는", self.age, "살입니다.")


person1 = Person("철수", 20)
person2 = Person("영희", 25)

person1.introduce()
person2.introduce()