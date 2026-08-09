class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    
    def mean(self):
        i=0
        s=0
        for i in range(len(self.marks)):
            s+=self.marks[i]
            i+=1
        return s/len(self.marks)
std1=student("bob",[10,20,30])
print(std1.mean())
