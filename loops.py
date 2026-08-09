condition =True
while condition==True:
    print("vedant is a good boy")
    condition=False
items=[1,2,3,4]
for item in items:
    print(item)

 #class
class animal:
     def walk(self):
            print("walking")
class dog(animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
            print("woof")

roger=dog("roger",5)
print(roger.name)
print(roger.age)

roger.bark()
roger.walk()

