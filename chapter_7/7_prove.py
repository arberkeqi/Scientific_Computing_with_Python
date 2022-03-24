# fhand = open("mbox.txt")
# for line in fhand:
#     line = line.rstrip()  # if not this it will print a newline in the end
#     if line.startswith("From: "):
#         print(line)

# or do it by skipping

# fhand = open("mbox.txt")
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith("From: "):
#         continue          # we skip a line by using "continue" statement
#     print(line)

# use in to select lines

# fhand = open("mbox.txt")
# for line in fhand:
#     line = line.rstrip()
#     if not "@uct.ac.za" in line:  # if this text is not in this line we skip
#         continue
#     print(line)








# # Example to read a file
# xfile = open("mbox.txt")
# for cheese in xfile:
#     print(cheese)
