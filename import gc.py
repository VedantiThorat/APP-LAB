import gc

# Check garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())

# Get garbage collection counts
print("Garbage Collection Count:", gc.get_count())

# Create objects
a = [1, 2, 3]
b = [4, 5, 6]

print("\nObjects created")

# Delete objects
del a
del b

print("Objects deleted")

# Perform manual garbage collection
collected = gc.collect()

print("Garbage Collected:", collected)

# Disable automatic garbage collection
gc.disable()
print("Automatic Garbage Collection Disabled")

# Enable automatic garbage collection
gc.enable()
print("Automatic Garbage Collection Enabled")

# Check final status
print("Final Status:", gc.isenabled())