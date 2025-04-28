# Handling exceptions with try-except

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution completed.")
