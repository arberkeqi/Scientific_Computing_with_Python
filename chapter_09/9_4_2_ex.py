fname = input("Enter the name of the file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))
    quit()

counts = dict()
for lines in fhand:
    lines = lines.rstrip()
    if lines.startswith("From:"):
        ipos = lines.find(":")
        mname = lines[ipos + 1:]
        mname = mname.strip()
        # print(mname)
        counts[mname] = counts.get(mname, 0) + 1

bigCount = None
bigWord = None
for mname, counter in counts.items():
    if bigCount is None or counter > bigCount:
        bigWord = mname
        bigCount = counter
print(bigWord, "is mentioned", bigCount)