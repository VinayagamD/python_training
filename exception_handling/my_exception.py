from commons.utils import Utils


def exception_message(message, line='start'):
    Utils.print_message(" Exception =========> {0} ".format(message), line=line)


# Definition

exception_message("Definition")

try:
    a = 10 / 0
    print(a)
except ArithmeticError:
    print("This statement is raising an exception")
else:
    print("Welcome")

exception_message("Definition", "end")

Utils.print_divider()
# Except with no exception
exception_message("Except with no exception")
try:
    a = 10 / 0
except:
    print("Arithmetic Exception")
else:
    print("Successfully done")

exception_message("Except with no exception", "end")

# Declaring Multiple Exception
exception_message("Declaring Multiple Exception")

try:
    a = 10/0
except (ArithmeticError, SystemError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")

exception_message("Declaring Multiple Exception", "end")

# Raise An Exception
exception_message(" Raise An Exception")

try:
    a = 10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occurred")
    print(e)

exception_message(" Raise An Exception", "end")

# Custom Exception
exception_message("Custom Exception")

exception_message("Custom Exception", "end")
