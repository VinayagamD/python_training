# For loop

# Example 1
print("Example 1 Start")
num = 2
for a in range(1, 6):
    print(num*a)
print("Example 1 End \n")
# Example 2
print("Example 2 Start")
sum = 0
for n in range(1, 11):
    sum += n

print(sum)
print("Example 2 End\n")

# Nested For Loop
# Nested For Loop Example1
print("Nested For Example 1 Start")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ", flush=True)
    print()
print("Nested For Example 1 End\n ")

# Nested For Loop Example 2
print("Nested For Example 2 starts")
for i in range(1, 6):
    for j in range(5, i-1, -1):
        print("*", end=" ")
    print()

print("Nested For Example 2 ends \n")

# While

# Example1
print("While Example 1 starts")
a = 10
while a > 0:
    print(f"Value of a is {a}")
    a -= 2
print("While Example 1 ends \n")

# Example2
print("While Example 2 starts")
n = 153
sum = 0
while n > 0:
    r = n % 10
    sum += r
    n = n/10
print(sum)
print("While Example 2 ends \n")

# Break
# Example1
print("Break Example 1 starts")
for i in [1, 2, 3, 4, 5]:
    if i == 4:
        print("Element Found")
        break
    print(i)
print("Break Example 1 ends \n")

# Example2
print("Break Example 2 starts")
for letter in 'Python3':
    if letter == 'o':
        break
    print(letter)
print("Break Example 2 ends\n")

# Continue
# Example 1
print("Continue Example 1 starts")
a = 0
while a <= 5:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)
print("End of Loop")
print("Continue Example 1 ends \n")

# Pass
# Example 1
print("Pass Example 1 starts")
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        pass
        print(f"Pass when value is {i}")
    print(i)
print("Pass Example 1 ends \n")

