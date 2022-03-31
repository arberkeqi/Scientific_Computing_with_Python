# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))
    quit()
count = 0
total = 0
avg = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        # print(line)
        # get the number in float
        ipos = line.find(":")
        wsnum = line[ipos + 1:]
        snum = wsnum.strip()
        num = float(snum)
        print(num)
        # count the number of lines
        count = count + 1
        # find the sum
        total = total + num
# find average
avg = total / count
print("There are {} lines.".format(count))
print("Average spam confidence: {}".format(avg))
print("Done")