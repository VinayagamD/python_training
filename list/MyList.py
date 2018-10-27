
from commons.utils import Utils


def cmp(a, b):
    return (a > b) - (a < b)


def my_string_message(message, line="start"):
    Utils.print_message("List ==========>  {0} ".format(message), line)


# List Example

# Defining List
my_string_message("Defining List")
data1 = [1, 2, 3, 4]
data2 = ['x', 'y', 'z']
data3 = [12.5, 11.6]
data4 = ['raman', 'rahul']
data5 = []

data6 = ['vinay', 10, 4.56, 'a']

print(f"data1 ===========> {data1}")
print(f"data2 ===========> {data2}")
print(f"data3 ===========> {data3}")
print(f"data4 ===========> {data4}")
print(f"data5 ===========> {data5}")
print(f"data6 ===========> {data6}")

my_string_message("Defining List", line='end')

# Accessing the list

my_string_message("Accessing List")

print(data1[0])
print(data1[0:2])
print(data2[-3:-1])
print(data1[0:])
print(data2[2:])

my_string_message("Accessing List", line='end')


# python list operator

my_string_message("Python List operator")

# adding a list
my_string_message("Adding a list")
list1 = [10, 20]
list2 = [30, 40]
list3 = list1+list2

print(f"list3 ===========> {list3}")

# Error Code
# list1 + 30
# print(f"list1 ============> {list1} ")
my_string_message("Adding a list", line='end')


# Python list Replication
my_string_message("lists replication")
print(list1*4)
my_string_message("lists replication", line='end')

# List Splicing
my_string_message("list splicing")
list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[0:2])
print(list1[4])
list1[1] = 9
print(list1)
my_string_message("list splicing", "end")

# updating list
my_string_message("updating list")
data1 = [5, 10, 15, 20, 25]
print(data1)
data1[2] = "Multiple of 5"
print(data1)
my_string_message("updating list", "end")

# appending the list
my_string_message(" appending the list")
list1 = [10, 'vinay', 'z']
print("Elements of list are: ")
print(list1)
list1.append(10.45)
print("List after appending")
print(list1)
my_string_message(" appending the list", "end")

# deleting the element from the list
my_string_message(" Deleting element from the list")
list1 = [10, 'vinay', 50.8, 'a', 20, 30]
print(list1)
del list1[0]
print(list1)
del list1[0:3]
print(list1)
my_string_message(" Deleting element from the list", "end")

# min
my_string_message("min")

list1 = [101, 981]
list2 = [100.45, 98.2]
print("Minimum value in List1: ", min(list1))
print("Minimum value in List2 ", min(list2))

my_string_message("min", "end")

# max
my_string_message("max")

print("Maximum value in List1: ", max(list1))
print("Maximum value in List2 ", max(list2))

my_string_message("max", "end")

# cmp
my_string_message("cmp")
list1 = [101, 981]
list2 = [100.45, 98.2]
list3 = [101, 981]
print(cmp(list1, list2))
print(cmp(list2, list1))
print(cmp(list3, list1))
my_string_message("cmp", "end")

my_string_message("Python List operator", line='end')


