fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))
    quit()

count = 0
for lines in fhand:
    lines = lines.rstrip()
    if lines.startswith("From:"):
        words = lines.split()
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")