class Student:
    def __init__(self, name, surname, age, avg_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_score = avg_score

    def change_avg_score(self, changed_avg_score):
        self.avg_score = changed_avg_score

    def display_info(self):
        print(f"Name: {self.name} {self.surname}, Age: {self.age}, Average Score: {self.avg_score}")


std_nesterenko = Student(name="Nick", surname="Nesterenko", age="23", avg_score="over 9000")

std_nesterenko.display_info()
std_nesterenko.change_avg_score(changed_avg_score="actually not over 9000")
std_nesterenko.display_info()

