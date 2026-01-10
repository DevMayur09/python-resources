# SIMPLE DECORATORS


def deco(func):
    def wrapper(*args):
        print("execute somethign before func")
        print ("Function Name:", func.__name__)
        return func(*args)
    return wrapper

@deco
def decorated_me(name):
    print(f"Hello {name}, I am decorated")


decorated_me("Mayur")


