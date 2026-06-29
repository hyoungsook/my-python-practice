class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_result(self):
        print(self.name + "님의 점수는", self.score, "점입니다.")

        if self.score >= 60:
            print("합격입니다.")
        else:
            print("불합격입니다.")


name = input("이름: ")
score = int(input("점수: "))

student = Student(name, score)
student.show_result()