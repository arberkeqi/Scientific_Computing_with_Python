# purse = dict()
# purse["money"] = 12
# purse["candy"] = 3
# purse["tissue"] = 75
# print(purse)

# print(purse["candy"])
# purse["candy"] = purse["candy"] +2
# print(purse)

# jjj = {"chuck" : 1, "fred" : 42, "jan" : 100}       # Dictionary Literals
# print(jjj)

# ccc = dict()
# ccc["csev"] = 1
# ccc["cwen"] = 1
# print(ccc)
# ccc["cwen"] += 1
# print(ccc)

# counts = dict()
# names = ["csev", "cwen", "csev", "zqian", "cwen"]
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] += 1
# print(counts)

# counts = dict()
# names = ["csev", "cwen", "csev", "zqian", "cwen"]
# for name in names:
#     counts[name] = counts.get(name, 0) + 1  # does same thing as 4 lines above
# print(counts)

# How to count the words in a line of text
# counts = dict()
# print("Enter a line of text:")
# line = input("")
# words = line.split()
# print("Words:", words, "\n")
# print("Counting...\n")
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print("Counts", counts)

# How to loop in a simple dictionary
# counts = {"chuck" : 1, "fred" : 42, "jan" : 100}
# for key in counts:
#     print(key, counts[key])

# Get a list of keys, values, or items
# jjj = {"chuck" : 1, "fred" : 42, "jan" : 100}
# print(list(jjj))
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())  # give us tuples

# for aaa, bbb in jjj.items():    # Can be done ONLY in PYTHON
#     print(aaa, bbb)

# Open a file, count the words and find the biggest word
fname = input("Enter the name of the file: ")
try:
    fhand = open(fname)
except:
    print("This file name {} is invalid. Please try again.".format(fname))
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord, "is mentioned", bigCount)
