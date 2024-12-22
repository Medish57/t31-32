class Student:
    def __init__(self, first_name, last_name, age, national_number, student_number, GPA):
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 
        self.national_number = national_number
        self.student_number = student_number
        self.GPA = GPA
    
    def get_first_name(self):
        return "The first name: " + self.first_name
      
    def get_age(self):
        return "The " + self.first_name + "'s age is " + str(self.age)

# ایجاد شیء از کلاس Student
student_1 = Student('arvin', 'zahere', 24, 37506319, 21215455, 19.8)
student_2 = Student('mahdi', 'Hasani', 22, 992640062012, 2024133458, 18.50)
student_3 = Student('nima', 'sharifi', 23, 9214133002, 26286123, 19.08)

# چاپ اطلاعات دانشجو
print(student_2.get_age())
print(student_2.get_first_name())