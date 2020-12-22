class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def __repr__(self):
        return repr((self.name,self.age,self.grade))