fname = input("Enter files name: ")
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))
    quit()

lst = list()
# using append()
for lines in fhand:
    lines = lines.rstrip()
    lines = lines.split()
    for line in lines:
        lst.append(line)
print(sorted(set(lst)))     # use sorted() to sort the list and use set() to remove the dublicates on the list

# # using extend
# for line in fhand:
#     line = line.rstrip()
#     line = line.split()
#     # print(line)
#     lst.extend(line)
# print(sorted(set(lst)))     # use sorted() to sort the list and use set() to remove the dublicates on the list    