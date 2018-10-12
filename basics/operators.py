from commons.utils import Utils as util


def print_message(message, line="start"):
    util.print_message("{0} operator ".format(message), line)


# Arithmetic
print_message("Arithmetic")
print(10 + 20)
print(20 - 10)
print(10 * 2)
print(10 / 2)
print(10 % 3)
print(2 ** 3)
print(10 // 3)
print_message("Arithmetic", "end")
# Relational Operator
print_message("Relational")
print(10 < 20)
print(10 > 20)
print(10 <= 20)
print(10 >= 20)
print(5 == 6)
print(5 != 6)
print_message("Relational", "end")
# Assignment Operator
print_message("Assignment")
c = 10
print(c)
c += 5
print(c)
c -= 5
print(c)
c *= 2
print(c)
c /= 2
print(c)
c %= 3
print(c)
c = 5
c **= 2
print(c)
c //= 2
print(c)
print_message("Assignment", "end")

# Logical operator
print_message("Logical")

a = 5 > 4 and 3 > 2
print(a)
b = 5 > 4 or 3 > 2
print(b)
c = not (5 > 4)
print(c)

print_message("Logical", "end")
# Membership Operators
print_message("Membership")
a = 10
b = 20
list = [10, 20, 30, 40, 50]
if a in list:
    print(" a is in given list")
else:
    print(" a is not in given list")
if b not in list:
    print(" b is not in given list")
else:
    print(" b is  given in list")

print_message("Membership", "end")

# Identity Operator
print_message("Identity")
a = 20
b = 20
if a is b:
    print(" a, b have same identity")
else:
    print(" a,b are different")
b = 10
if a is not b:
    print(" a, b have different identity")
else:
    print(" a, b have same identity")

print_message("Identity", "end")

print("========================= Comment Starts ================================\n")
# This is a single

'''
This is a multi-line comment
'''
print("========================= Comment Ends ================================\n")
