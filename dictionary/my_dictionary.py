from commons.utils import Utils


def dictionary_message(message, line='start'):
    Utils.print_message("Dictionary ==========>  {0} ".format(message), line)


# Definition
dictionary_message("definition")

data = {100: 'Ravi', 101: 'Vinay', 102: 'Rahul'}
print(data)

dictionary_message("definition", "end")

# Example2

dictionary_message(" Example 2")
plant = {}
plant[1] = 'Ravi'
plant[2] = 'Manoj'
plant['name'] = 'Hari'
plant[4] = 'Om'
print(plant[2])
print(plant['name'])
print(plant[1])
print(plant)
dictionary_message(" Example 2", "end")

Utils.print_divider()


# Accessing Dictionary values
dictionary_message(" Accessing Values")
data1 = {'Id': 101, 'Name': 'Suresh', 'Profession': 'Developer'}
data2 = {'Id': 102, 'Name': 'Ramesh', 'Profession': 'Trainer'}
print("Id of 1st Employer is ", data1['Id'])
print("Id of 2nd Employer is ", data2['Id'])
print("Name of 1st Employer is ", data1['Name'])
print("Profession of 2nd Employer is ", data2['Profession'])
dictionary_message(" Accessing Values", "end")

Utils.print_divider()


# Updating the elements

dictionary_message(" Updating Elements ")
data1['Profession'] = 'Manager'
data2['Salary'] = 20000
data1['Salary'] = 15000
print(data1)
print(data2)
dictionary_message(" Updating Elements ", "end")

Utils.print_divider()

# Deleting Elements
dictionary_message(" Deleting Elements")
data = {100: 'RAM', 101: 'Suraj', 102: 'Alok'}
del data[102]
print(data)
del data
# print(data)
dictionary_message(" Deleting Elements", "end")

Utils.print_divider()

# Dictionary Functions
dictionary_message("Dictionary Functions")

# len
dictionary_message("len")

data = {100: 'RAM', 101: 'Suraj', 102: 'Alok'}
print(data)
print(len(data))

dictionary_message("len", "end")

# str
dictionary_message("str")
print(str(data))
dictionary_message("str", "end")

# Keys
dictionary_message("Keys")
print(data.keys())
dictionary_message("Keys", "end")

# Values
dictionary_message("Values")
print(data.values())
dictionary_message("Values", "end")

# items
dictionary_message("Items")
print(data.items())
dictionary_message("Items", "end")

# Update
dictionary_message("Update")
data2 = {103: 'Sanjay'}
data.update(data2)
print(data)
dictionary_message("Update", "end")

# clear
dictionary_message("Clear")
print(data)
data.clear()
print(data)
dictionary_message("Clear", "end")

# fromkeys(seq)/fromkeys(seq,value)
dictionary_message("fromkeys(seq)/fromkeys(seq,value)")
seq = ('Id', "Number", "Email")
data = {}
data1 = {}
data1 = data1.fromkeys(seq)
data2 = data2.fromkeys(seq, 100)
print(data1)
print(data2)
dictionary_message("fromkeys(seq)/fromkeys(seq,value)", "end")

# copy
dictionary_message("copy")
data = {'Id': 100, 'Name': 'Aakash', 'Age': 23}
data1 = data.copy()
print(data1)
dictionary_message("copy", "end")

# has_key
dictionary_message(" has_key")
print('Age' in data)
print('Email' in data)
dictionary_message(" has_key", "end")

# get
dictionary_message("get")
print(data.get('Age'))
print(data.get('Email'))
dictionary_message("get", "end")

dictionary_message("Dictionary Functions", "end")



