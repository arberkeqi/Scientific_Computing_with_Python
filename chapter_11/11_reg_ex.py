from itertools import count
import numbers
import re
fname = input("Enter the name of the file: ")
if len(fname) < 1 :
    fname = "regex_sum_42.txt"      # regex_sum_1510105.txt; regex_sum_42.txt
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))

numList = list()
# counts = dict()
for lines in fhand:
    lines = lines.rstrip()
    nstring = re.findall('[0-9]+', lines)
    if len(nstring) != 1:
        continue
    num = int(nstring)
    # counts[num] = counts.get(num, 0) + 1
    numList.append(num)
# print("There are {} numbers.".format(counts))
print("The sum is {}".format(sum(numList)))
