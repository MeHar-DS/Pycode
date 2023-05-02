class ParentClass:
    interest = 0.06
    def __init__(self,name,loan):
        self.name = name
        self.loan = loan
        print("Parent Class Instance")

    def parent_method(self):
        print("Parent\'s Money")

    def calc_interest(self):
        print("Total Interest",self.loan*self.interest)


class Student(ParentClass):
    interest = 0.04


s = Student("Mervin",2000)
s.calc_interest()
# class ChildClass(ParentClass):
#     pass


# p = ParentClass()
# p.parent_method()

# c = ChildClass()
#
# c.parent_method()

