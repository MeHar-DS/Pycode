class RateofInterest:
    interest = 0.06  #class level variable

    def __init__(self,name,loan):
        self.name = name
        self.loan = loan


    def calc_interest(self):
        print("Total Interest is :", self.loan * self.interest)

    # def calc_interest(self):
    #     print("Total Interest is :", self.loan * RateofInterest.interest)  # Using class level variable


p1 = RateofInterest("Mervin",43000000)
p2 = RateofInterest("Udaya",43000000)


RateofInterest.interest = 8  # Class level variable can be changed like this
p1.interest = 2  # classlevel variable can be customised for each instance as well
p1.calc_interest()

p2.interest = 4
p2.calc_interest()



