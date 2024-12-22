class Human:

     counter=0
    def __init__(self, name, student_number,number_of_units ,semester_equivalentweight):

        self.name = name 

        self.student_number = student_number

        self.number_of_units = number_of_units

        self.semester_equivalentweight =semester_equivalentweight


        Human.counter += 1


    def die(self):
        Human.counter -= 1


ali = Human('Ali','0025096342', 18, 12)

javad = Human('Javad', '0025096341', 16, 18 )

Reza = Human('Reza', '0025076426', 20, 15 )
print(self.ali)