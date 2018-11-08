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

