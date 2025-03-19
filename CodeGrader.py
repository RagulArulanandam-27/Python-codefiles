from datetime import datetime


class CodeGradeUser:
    def __init__(self, username, institute):
        self.username = username
        self.institute = institute
        pass

    def hello(self):
        print("Hello {0} from code University".format(self.username))


class Student(CodeGradeUser):
    def __init__(self, name, institute, graduate_year):
        super().__init__(name, institute) 
        self.graduate_year = graduate_year

    def graduated(self):
        current_year = datetime.now().year
        if (current_year > self.graduate_year):
            return True
        else:
            return False
        
    def handin(self):
        if (self.graduated()):
            print("Thanks, Peter! Your submission Python was successfully handed in!")
        else:
            print("Sorry Peter, you can only hand in if you haven’t graduated yet!")


class Teacher(CodeGradeUser):
    
    def __init__(self, username, institute, student_institute):
        super().__init__(username, institute)
        self.student_institute = student_institute
 
    def teach(self):
        print("Python is fun to learn and it's usefull)")

    def grade(self):
        if (self.institute == self.student_institute):
            print("Teacher Robin graded Peter with grade 90.")
        else:
            print("You cannot grade Peter as they are from another institute.")


a = CodeGradeUser("Ragul", "UOL")
a.hello()

student_class = Student("Ragul", "UOL", 2025)
student_class.handin()


teacher_class = Teacher("Alex", "UOL", student_class.institute)
teacher_class.grade()

print(datetime.date(1956, 1, 31))
