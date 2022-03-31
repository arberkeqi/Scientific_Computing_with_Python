fname = input("Enter the file's name: ")
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))
    quit()

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
