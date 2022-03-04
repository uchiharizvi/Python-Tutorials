myList = ["a", "b", "c", "d", "c", "a"]
myList = list(dict.fromkeys(
    myList))
# Create a dictionary, using the List items as keys.
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
print(myList)
