class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def msg_name(self):
        print("学生的姓名为",self.name)
    def msg_age(self):
        print("%s的年龄为%d"%(self.name,self.age))

stu1=Student("王明",20)
stu2=Student("张三",18)

stu1.msg_name()
stu2.msg_age()

x=input()
print("x=",x)