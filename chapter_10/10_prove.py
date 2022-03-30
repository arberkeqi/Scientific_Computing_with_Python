from itertools import count


d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():        # k for key; v for value
    print(k, v)

tups = d.items()
print(tups)

# take adv of the ability to compare tuples and sort the dictionaries
# first we sort the dictionary by the key using the items() method and sorted() function
d = {'a' : 10, 'b' : 1, 'c' : 22}
d.items()
sorted(d.items())

# sort by value and not by key
c = {'a' : 10, 'b' : 1, 'c' : 22}       # we have a dictionary
tmp = list()                            # we create an empty list
for k, v in c.items():                  # create a loop that goes around the dict
    tmp.append((v, k))                  # we append in order value, key not k,v
print(tmp)
tmp = sorted(tmp, reverse=True)         # we know that lists get sorted so we sort
print(tmp)                              # sorted in reverse order

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# here we can do all the work that is done on the below block of code
# print( sorted( [ (val, key) for key, val in counts.items() ] ) )

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)