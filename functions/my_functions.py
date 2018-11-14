from commons.utils import Utils


def function_message(message, line='start'):
    Utils.print_message("Function ==========>  {0} ".format(message), line)


# Definition
function_message("definition")


def my_sum(x, y):
    """ Going to add x and y"""
    s = x + y
    print("Sum of two numbers is")
    print(s)


# calling
function_message("calling function")
my_sum(20, 30)
my_sum(10, 20)
function_message("calling function", "end")

function_message("definition", "end")

Utils.print_divider()

# Return
function_message("return")


def my_sum(a, b):
    """Adding the two values"""
    print("Printing within function")
    print(a + b)
    return a + b


def msg():
    print("Hello")
    return


total = my_sum(10, 20)

print("Printing Outside", total)
msg()
function_message("return", "end")

Utils.print_divider()

# Function Argument and parameter

function_message("Function Argument and parameter")


def addition(x, y):
    print(x+y)


x = 15
addition(x, 10)
addition(x, x)
y = 20
addition(x, y)
function_message("Function Argument and parameter", "end")


# Passing Parameter

function_message("Passing Parameter")


def my_sum(a, b):
    """Function having two parameters"""
    c = a+b
    print(c)


my_sum(10, 20)
# my_sum(20)

function_message("Passing Parameter", "end")


# Default arguments
function_message("Default arguments")


def msg(id, name, age=21):
    """Printing the passed value"""
    print(id)
    print(name)
    print(age)
    return


msg(id=100, name='Ravi', age= 20)
msg(id=101, name='Ratan')

function_message("Default arguments", "end")

Utils.print_divider()

# Anonymous Function

function_message("Anonymous Function")

square = lambda x1: x1*x1

print("Square number is ", square(10))

function_message("Anonymous Function", "end")

# Scope of variable
function_message(" Scope of variables")

# Local Scope

function_message("Local Scope")


def msg():
    a = 10
    print("Value of a is ", a)
    return


msg()

# print(a) # Error line

function_message("Local Scope", "end")

# Global Variable
function_message("Global Scope")

b = 20


def msg():
    a = 10
    print("Value of a is ", a)
    print("Value of b is ", b)
    return


msg()
print(b)

function_message("Global Scope", "end")
function_message(" Scope of variables", "end")

