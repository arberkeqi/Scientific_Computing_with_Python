lotto = [2, 14,26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)
print(len(lotto))

friends = ["Joseph", "Glenn", "Sally"]
print(range(len(friends)))

# Sorting a list
friends.sort()
print(friends)

for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year:", friend)

# create an empty list and add elements using append method
stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)

# using in to see if True or False
some = [1, 9, 21, 10, 16]
if 2 in some:
    print(True)
else:
    print(False)

# different way to do 7_2_ex.py
# numlist = list()
# while True:
#     inp = input("Enter a number: ")
#     if inp == "done":
#         break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print("Average:", average)
# it is easier but it requires more memory because at line "numlist.append"
# it stores all the values and then does the calculations

line = "first;second;third"
# if we dont have "blank space" but still want to split do it this way
thing = line.split(";")
print(thing)