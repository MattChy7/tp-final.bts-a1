import psutil

# Get the memory usage information
memory = psutil.virtual_memory()

# Print the memory usage details
print("Total Memory: {:.2f} GB".format(memory.total / (1024 ** 3)))
