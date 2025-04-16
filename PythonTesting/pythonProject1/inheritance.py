from pythontestingsample import high


class inheritance(high):
    num2 = 200

    def __init__(self):
        high.__init__(self, 2, 5)

    def getfull(self):
        return self.num2 + self.num

obj = inheritance()
print(obj.getfull())
