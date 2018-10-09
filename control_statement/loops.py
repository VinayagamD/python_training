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
#
print("Nested For Example 1 Start")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ", flush=True)
    print()
print("Nested For Example 1 End\n ")

