class employee:
    raise_amount=1.04
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def fullname(self):
      return '{} {}'.format(self.fname,self.lname)  
    def apply_raise(self):
       self.salary=int(self.salary*self.raise_amount)
# *employee.raise_amount* is same as self.raise_amount
#the instances donot have raiseamt so they will look for it in class and use it from there

emp2=employee("bob","kumar",20000)
print(emp2.__dict__)#this will print the attributes of the object emp2
print(employee.__dict__)#this will print the attributes of the class employee,,

#if we dont pass self and try to access any of theftns it will give a type error because obj.ftn is basically passing an argument so ()cant be left empty

#emp2.fullname() is same as employee.fullname(emp2)
