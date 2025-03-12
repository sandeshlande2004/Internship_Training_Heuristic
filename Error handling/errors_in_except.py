# Zero dividsion error and value error in except block

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = a / b
# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# except ValueError:
#     print("Please enter a integer number value")
    
# except ArithmeticError:
#     print("Arithmetic error occurred") # ArithmeticError error is a parent class of ZeroDivisionError
    

# KeyboardInterrupt error is a parent class of ValueError
# KeyboardInterrupt error is a parent class of EOFError
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = a / b
# except KeyboardInterrupt:
#     print("Keyboard interrupt occurred")
# except EOFError:
#     print("End of file error occurred")
# except ArithmeticError:
#     print("Arithmetic error occurred")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# except ValueError:
#     print("Please enter a integer number value")
    
# EOFError 
# EOFError is raised when one of the built-in functions (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data.

try:
    data = input("Enter your data here: ")
except EOFError:
    print("End of file error occurred")
    
    

