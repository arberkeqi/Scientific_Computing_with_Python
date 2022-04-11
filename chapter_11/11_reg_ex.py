import re
fname = input("Enter the name of the file: ")
if len(fname) < 1 :
    fname = "regex_sum_1510105.txt"      # regex_sum_1510105.txt; regex_sum_42.txt
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))

numList = list()
for lines in fhand:
    lines = lines.rstrip()
    nstring = re.findall('[0-9]+', lines)
    if len(nstring) > 0:
        lineSum = sum(map(int, nstring))
        numList.append(lineSum)
        # print("line sum = {0}".format(numSum))
print("The sum is {}".format(sum(numList)))
