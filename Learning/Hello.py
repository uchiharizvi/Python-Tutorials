x = 1
if x == 1:
    print("X is 1.")
myInt = 7
myFloat = 7.0
print(myInt)
print(myFloat)
# type conversion
myFloat = float(7)
print(myFloat)
#  String
myString = 'hello'
print(myString)
myString = "world"
print(myString)
myString = "Don't worry about the world"
print(myString)

#  Assignments Operators
a, b = 3, 4
print(a, b)

# Multiple Operators
one = 1
two = 2
hello = "hello"
print(one, two, hello)

# None can be used as Null
myString = None
myFloat = 10.0
myInt = None

if myString == "hello":
    print("String: %s" % myString)  # use % for concatenation
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)

#  Using List
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3

# Prints out 1,2,3
for x in mylist:
    print(x)

print(mylist[10])

