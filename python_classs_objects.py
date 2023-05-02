class Employee:

    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def greet_person(self):
        print("Hello, Welcome "+self.fname)

emp1 = Employee("Mervin","Harshal","mervaqua1987@gmail.com")
emp2 = Employee("Buddha","Gautama","mervaqua1987@gmail.com")

print(emp1.fname)
print(emp2.lname)

emp1.greet_person()
