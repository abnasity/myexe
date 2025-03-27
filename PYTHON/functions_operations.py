

# def calculator(operation):
#     def add(a ,b):
#         return a + b
    
#     def subtract(a ,b):
#         return a - b
    
#     def multiply(a ,b):
#         return a * b
    
#     def divide(a ,b):
#         return a / b
    
#     if operation == "add":
#         return add
    
#     elif operation == "subtract":
#         return subtract
    
#     elif operation == "multiply":
#         return multiply
    
#     elif operation == "divide":
#         return divide
#     else:
#         return"Invalid operation"
    
    
    
# result_add = calculator("add")(3,4)
# print(f"addition results:{result_add}")
 
#USE CASE 1
 
# def calculator(operation):
#     def add(a, b):
#         return a + b
    
#     def subtract(a, b):
#         return a - b
    
#     def multiply(a, b):
#         return a * b
    
#     def divide(a, b):
#         if b == 0:
#             return "Error: Division by zero"
#         return a / b
    
#     if operation == "add":
#         return add
#     elif operation == "subtract":
#         return subtract
#     elif operation == "multiply":
#         return multiply
#     elif operation == "divide":
#         return divide
#     else:
#         return None

# # User input
# operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# # Perform calculation
# operation_func = calculator(operation)
# if operation_func:
#     result = operation_func(a, b)
#     print(f"Result: {result}")
# else:
#     print("Invalid operation")
    
    
    
#USE CASE 2
def calculator(operation, a, b):
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    
    if operation in operations:
        return operations[operation](a, b)
    else:
        return "Invalid operation"

# User input
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform calculation
result = calculator(operation, a, b)
print(f"Result: {result}")

