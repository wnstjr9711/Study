class Calculator:
    def __init__(self,list):
        self.list=list
        self.result=0
    def sum(self):
        while self.list:
            self.result+=self.list.pop()
        return self.result