import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function name: {func.__name__}")
        if args:
            argrpt = args
        else:
            argrpt = "none"
        logger.log(logging.INFO, f"positional arguments: {argrpt}")
        if kwargs:
            kwargrpt = kwargs
        else:
            kwargrpt = "none"
        logger.log(logging.INFO, f"keyword arguments: {kwargrpt}")
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"return value: {result}")
        return result
    return wrapper

@log_decorator
def hello_world():
    print("hello world")

@log_decorator
def pos_args(*args):
    return True

@log_decorator
def kw_args(**kwargs):
    return log_decorator

hello_world()

pos_args("first_arg", "second_arg")
        
kw_args(first="first_kw_arg", second="second_kw_arg")