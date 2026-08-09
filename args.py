def add (*args):
    print (type(args))# prtinting the type of args which is tuple

add(1,2,3,4,5)
def add (*args):
    total=0
    for i in args:
        total+=i
    return total
add(1,2,3)    
def display_names(*args):
    for arg in args:
        print(arg,end=" ")
display_names("vedant","kumar","singh")
def print_address(**kwargs):
    print(type(kwargs))#printing the type of kwargs which is dict
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_address(street="abc",city="xyz",state="pqr"   )
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.value():
        print(value,end=" ")
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("dr.","spongebob","squarepants",street="123 street",city="bikini bottom",state="ocean"   )
