add_1= lambda x, y: x+y
result=add(1,7)
# lamda ftn used when the ftn is being used as an argument
def square(x):
    return x**2

squares=list(map(square,[1,2,3]))
#OR,
squares=list(map(lambda x: x**2,[1,2,3]))
evens=list(filter(lambda x: x%2==0,[1,2,3,4]))
values=[(1,'b',"hello"),(2,'a',"world"),(3,'c',"ok")]
sorted_values=sorted(values, key=lambda x: x[1])
#here sorting happens based on keys

    