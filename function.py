def decorator_func(func):
    def wrapper():
        print("You will be printed before function.")
        func()
        print("You will be printed after function call.")
    return wrapper

@decorator_func
def say_hi():
    print("Hello World")

say_hi()

import time

def time_calculator(func):
    def wrapper(*args, **kwargs):
        start = time.time()          # Start time
        result = func(*args, **kwargs)  # Call original function
        print("Time taken by this function is:", time.time() - start, "seconds")
        return result
    return wrapper

@time_calculator
def display():
    time.sleep(2)   # Pause for 2 seconds
    print("Hello World")

display()