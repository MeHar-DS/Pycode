class AreaRect():
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l*self.b


area1 = AreaRect(8, 5)
area2 = AreaRect(28, 15)

print(area1.calculate_area())
print(area2.calculate_area())