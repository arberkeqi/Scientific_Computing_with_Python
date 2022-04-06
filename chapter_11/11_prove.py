import re
x = "My 2 favorite numbers are 19 and 42."
y = re.findall("[0-9]+", x)
# [0-9] -> means ther is only one character, if add + means one or more digits
u = re.findall("[AEIOU]+", x)
print(u)
print(y)

# # Greedy Matching
# import re
# x = "From: Using the : character"
# y = re.findall("^F.+:", x)
# print(y)

# Non-Greedy Matching
# import re
# x = "From: Using the : character"
# y = re.findall("^F.+?:", x)
# print(y)

lin = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# y = re.findall('@(\S*)', lin)
y = re.findall('^From .*@(\S*)', lin)
print(y)

re.findall()