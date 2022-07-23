from logging import FileHandler
import urllib.request, urllib.parse, urllib.error

# we don't get headers because they are consumed by urlopen (keeps the headers)  
# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt") # encode automatically
# # gives us an object that looks like a file handler (this we can put on a 
# # for loop)
# for line in fhand:
#     print(line.decode().strip())

# We can treat it like a FILE

# Count the words
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# Read a webpage
# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# for line in fhand:
#     print(line.decode().strip())