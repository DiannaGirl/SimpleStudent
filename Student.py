
class Student:
    def __init__(self,name):
        self.name = name;
        self.age = 0;
        self.school = "";
        self.rank = "";
        self.list = {};

    def setName(self,s):
        self.name = s;
    def setAge(self,a):
        self.age = a;
    def getRank(self):
        return self.rank;
    def setRank(self,name):
        self.rank = name;
    def setSchool(self,school):
        self.school = school;



