# Class methods = Allow operations related to the class itself;
#                 Take (cls) as the first parameter, which represents the class itself;

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += self.gpa

    #INSTANCE method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students is {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    

#Objects; 
student1 = Student("MORO", 5.4)
student2 = Student("Adam", 3.5)
student3 = Student("XPLD", 6.7)

#Print data;
print(Student.get_count())
print(Student.get_average_gpa())