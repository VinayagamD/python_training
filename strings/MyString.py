str = "Python"

print(len(str))

for i in range(0, len(str)):
    print(str[i], end="\t")
print()
length = len(str)
for i in range(-1, (-length - 1), -1):
    print(str[i], end="\t")
print()

# Expression
print('vinay' + 'ganesh')

# print('10'+20)
print("s" + 'abc')

print(5 * 'Vinay')
print('Soono' * 2)
print('$' * 5)

from commons.utils import Utils as util


def my_operator_message(message, line="start"):
    util.print_message("String {0} operator".format(message), line)


def my_string_message(message, line="start"):
    util.print_message("String {0} ".format(message), line)


# String Membership Operator
str1 = "javatpoint"
str2 = "sssit"
str3 = "seomount"
str4 = "java"
str5 = "it"
str6 = "seo"

my_operator_message("Membership")
print(str4 in str1)
print(str6 in str3)
print(str4 not in str1)
print(str1 not in str4)
my_operator_message("Membership", "ends")

# String Relation Operator
my_operator_message("Relational")
print("RAJAT" == "RAJAT")
print("afsha" >= 'Afsha')
print('Z' != 'z')
my_operator_message("Relational", "ends")

# String Slicing
my_string_message("Slicing")
str = "Nikhil"
print(str[0:6])
print(str[0:3])
print(str[2:5])
print(str[2:len(str)])
print(str[3:])

str = "Mahesh"
print(str[:6]+str[6:])

my_string_message("Slicing", "ends")


# String Function and methods
my_string_message("Function and methods")

print('abc'.capitalize())
print('abc'.upper())
print('ABC'.lower())

msg = "welcome to vtu"
substr1 = 'o'
print(msg.count(substr1, 4, 16))
substr2 = 't'
print(msg.count(substr2))

# ends with

string1 = "Welcome to vtu"
substr1 = "vtu"
substr2 = "to"
substr3 = "of"
print(string1.endswith(substr1))
print(string1.endswith(substr2, 2, 14))
print(string1.endswith(substr3, 2, 17))
print(string1.endswith(substr3))


# find
substr1 = "come"
substr2 = "to"
print(string1.find(substr1))
print(string1.find(substr2))
print(string1.find(substr1, 3, 10))
print(string1.find(substr2, 17))

# index


my_string_message("Function and methods", "ends")
