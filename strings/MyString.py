str = "Python"

print(len(str))

for i in range(0, len(str)):
    print(str[i], end="\t")
print()
length = len(str)
for i in range(-1,(-length-1), -1):
    print(str[i], end="\t")
