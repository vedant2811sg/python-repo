def hello(name="vedant"):
    print(f"Hello{name}") 

hello("bob")
hello(1)

def talk(phrase):
    def say(word):
        print(word)

    words=phrase.split(' ')#creates list seperating at every ' ' 
    for word in words:
        say(word)

talk("hello vedant how are you")
def counter():
    count=0
    def increment():
        nonlocal count# to access a variable of outer ftn in inner ftn
        count+=1
        return(count)
    return  increment()

increment=counter()
print(increment())#1
print(increment())#2 calls the inner function only not resetting count to 0
