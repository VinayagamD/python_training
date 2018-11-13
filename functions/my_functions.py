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


def sum(a, b):
    """Adding the two values"""
    print("Printing within function")
    print(a + b)
    return a + b


def msg():
    print("Hello")
    return


total = sum(10, 20)

print("Printing Outside", total)
msg()
function_message("return", "end")

Utils.print_divider()



