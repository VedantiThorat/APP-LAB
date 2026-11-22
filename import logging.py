import logging

# Set logging level
logging.basicConfig(level=logging.DEBUG)

# Different logging messages
logging.debug("This is a debug message")
logging.info("This is an information message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# Simple calculation
a = 10
b = 5

logging.info("Addition: %d", a + b)
logging.info("Subtraction: %d", a - b)
logging.info("Multiplication: %d", a * b)

# Division
try:
    result = a / 0
except ZeroDivisionError:
    logging.error("Cannot divide by zero")

print("Program completed")