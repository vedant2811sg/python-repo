age=input()
print("Age is:",age)
dogs=["roger",1,"syd",True]
print("roger" in dogs)#true because roger is present in the list
print(dogs[-1  ])#True because -1 index is True
print(dogs[1:3])#prints 1 and syd because 3 is not included
dogs.extend(["cat",2])#adds cat and 2 to the list
dogs+=["cat",2]#adds cat and 2 to the list
dogs+="cat" #adds c,a,t to the list because string is iterable
dogs.remove("roger")#removes roger from the list
sorted(dogs,key=str.lower)#sorts the list in ascending order not caring about the case
            #tuples are immutable so we cannot change the values of a tuple
names=("vedant","syd","roger")
names[0]
names.index("syd")#gives the index of syd in the tuple
len(names)#gives the length of the tuple
print("roger" in names)#true because roger is present in the tuple      
names[0:2]#prints vedant and syd because 2 is not included
sorted(names)
print(sorted(names))
newtuple=names+("cat",)#adds cat to the tuple
      #dictionaries are mutable so we can change the values of a dictionary
dogs={"name":"roger","age":1,"breed":"syd"}
#{key:value} pairs are called items in a dictionary
print(dogs["name"])#prints roger because name is the key and roger is the value
dogs["age"]=2#changes the value of age to 2
print(dogs.get("name"))#prints roger because name is the key and roger is the value 
print(dogs.get("color", "brown"))#prints brown because color is not present in the dictionary so it returns the default value brown
print(dogs.keys())#prints the keys of the dictionary
print(dogs.values())#prints the values of the dictionary
print(dogs.pop("age"))#removes the key age and its value from the dictionary and returns the value 2
print(dogs.popitem())#removes the last item from the dictionary and returns it as a tuple
print(list(dogs.items()))#prints the items of the dictionary as a list of tuples
    #sets are mutable so we can change the values of a set
dogs={"roger","syd","cat"}#creates a set with three elements
set1={"roger","syd","cat"}
set2={"cat","dog","hamster"}
print(set1 & set2)  # prints the intersection of the two sets
print(set1 | set2)  # prints the union of the two sets
print(set1 - set2)  # prints the difference of the two sets
print(set1 ^ set2)  # prints the symmetric difference of the two sets
print(set1<set2)  # prints False because set1 is not a subset of set2
print(list(set1))  # converts the set to a list
#a set cannot have 2 of the same item evenn if we add two same items its gonna print only one 
    