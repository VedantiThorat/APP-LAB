import threading
import time

# First task
def task1():
    for i in range(1, 4):
        print("Task 1:", i)
        time.sleep(1)

# Second task
def task2():
    for i in range(1, 4):
        print("Task 2:", i)
        time.sleep(1)

# Third task
def task3():
    for i in range(1, 4):
        print("Task 3:", i)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads
t1.join()
t2.join()
t3.join()

print("All tasks completed!")