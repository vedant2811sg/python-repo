def add_sprinklers(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles to your ice cream!")
        func(*args, **kwargs)
    return wrapper
# if we dont write wrapper func we get ice cream even without calling the geticecreamfunc


def add_fudge():
    def wrapper(*args, **kwargs):
        print("u add  fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinklers
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream!")

get_ice_cream()
