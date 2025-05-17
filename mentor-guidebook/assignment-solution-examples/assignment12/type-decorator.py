def type_decorator(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return type_of_output(func(*args,**kwargs))
        return wrapper
    return decorator

@type_decorator(str)
def return_int():
    return 5

@type_decorator(int)
def return_string():
    return "not a number"

print(type(return_int()).__name__)

try:
    return_string()
    print("shouldn't get here")
except ValueError:
    print("you can't convert a string to an integer")