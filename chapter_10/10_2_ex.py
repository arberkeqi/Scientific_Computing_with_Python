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
    if lines.startswith("From "):
        words = lines.split()
        times = words[5]
        time = times.split(":")
        hour = time[0]
        counts[hour] = counts.get(hour, 0) + 1

lhour = list()
for k, v in counts.items():
    ntup = (k, v)
    lhour.append(ntup)
lhour = sorted(lhour)
for k, v in lhour:
    print(k, v)