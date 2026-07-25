# Decorator function
def decorator(func):
    def wrapper():
        print("Hello")
        func()
    return wrapper

# Function to decorate
@decorator
def message():
    print("Welcome!")

# Function call
message()