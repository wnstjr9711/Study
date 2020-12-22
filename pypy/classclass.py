class Cal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def sum(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
A=Cal()
B=Cal()

A.setdata(5,3)
print(A.sum())
print(A.mul())
class safeCal(Cal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
A=safeCal()
A.setdata(4,0)
print(A.div())
print(A.sum())