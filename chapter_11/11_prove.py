# import re
# x = "My 2 favorite numbers are 19 and 42."
# y = re.findall("[0-9]+", x)
# # [0-9] -> means ther is only one character, if add + means one or more digits
# u = re.findall("[AEIOU]+", x)
# print(u)
# print(y)

# # # Greedy Matching
# # import re
# # x = "From: Using the : character"
# # y = re.findall("^F.+:", x)
# # print(y)

# # Non-Greedy Matching
# # import re
# # x = "From: Using the : character"
# # y = re.findall("^F.+?:", x)
# # print(y)

# lin = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# # y = re.findall('@(\S*)', lin)
# y = re.findall('^From .*@(\S*)', lin)
# print(y)

import re
fname = input("Enter the name of the file: ")
if len(fname) < 1 :
    fname = "regex_sum_42.txt"      # regex_sum_1510105.txt; regex_sum_42.txt
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))

numList = list()
for lines in fhand:
    lines = lines.rstrip()
    nstring = re.findall('[0-9]+', lines)
    if len(nstring) != 1:
        continue
    lineSum = sum(map(int, nstring))
    numList.append(lineSum)
    print("line sum = {0}".format(lineSum))
print(sum(numList))     # all the sums are on the list
print("The sum is {}".format(sum(numList)))     # why don't you sum it MF!!!
