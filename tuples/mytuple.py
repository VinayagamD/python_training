from commons.utils import Utils


def my_tuple_message(message, line="start"):
    Utils.print_message("Tuple ==========>  {0} ".format(message), line)


# Define
my_tuple_message("define")
data = (10, 20, 'ram', 56.8)
data2 = "a", 10, 20.9
print(data)
print(data2)
my_tuple_message("define", "end")

# Empty tuple

my_tuple_message("Empty Tuple")
tuple1 = ()
print(tuple1)
my_tuple_message("Empty Tuple", "end")


# Single Object Tuple
my_tuple_message(" Single Object Tuple")
tuple1 = (10,)
print(tuple1)
my_tuple_message(" Single Object Tuple", "end")

# Tuples with tuple
my_tuple_message("Tuples with tuple")
tupl1 = 'a', 'mahesh', 10.56
tupl2 = tupl1, (10, 20, 30)
print(tupl1)
print(tupl2)
my_tuple_message("Tuples with tuple", "end")


# Accessing Tuples
my_tuple_message("Accessing Tuples")
data1 = (1, 2, 3, 4)
data2 = ('x', 'y', 'z')
print(data1[0])
print(data1[0:2])
print(data2[-3:-1])
print(data1[0:])
print(data2[:2])
my_tuple_message("Accessing Tuples", "end")

Utils.print_divider()

# Python Tuple Operation
my_tuple_message(" Tuple Operation")

Utils.print_divider()
# Adding Tuples
my_tuple_message(" Adding Tuple")
data1 = (1, 2, 3, 4)
data2 = ('x', 'y', 'z')
data3 = data1 + data2
print(data1)
print(data2)
print(data3)
my_tuple_message(" Adding Tuple", "end")

# Replicating Tuple
my_tuple_message(" Replicating Tuple")
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
print(tuple1*2)
print(tuple2*3)
my_tuple_message(" Replicating Tuple", "end")

my_tuple_message(" Tuple Operation", "end")

# Python tuple Slicing
my_tuple_message("tuple slicing")
data1 = (1, 2, 4, 5, 7)
print(data1[0:2])
print(data1[4])
print(data1[:-1])
print(data1[-5:])
print(data1)
my_tuple_message("tuple slicing", "end")

# Python Tuple Other Operation
my_tuple_message(" Tuple Other Operation")

# Creating tuple From Existing

data1 = (10, 20, 30)
data2 = (40, 50, 60)
data3 = data1+data2
print(data3)
my_tuple_message(" Tuple Other Operation", "end")

# deleting tuple
my_tuple_message(" deleting ")
data = (10, 20, 'rahul', 40.6, 'z')
print(data)
del data
# print(data)
my_tuple_message(" deleting ", "end")
