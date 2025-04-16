







class high:
    num = 101

    def __init__(self, a, b):
        self.fnumber = a
        self.snumber = b
        print("auto call")


    def getdata(self):
        print("hellooooo")


    def summation(self):
        return self.fnumber + self.snumber


obj = high(2, 2)
print(obj.num)
obj.getdata()



