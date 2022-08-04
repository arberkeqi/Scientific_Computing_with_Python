import email


fname = input("Enter name: ")
if len(fname) < 1:
    fname = "mbox.txt"
try:
    fhand = open(fname)
except:
    print("The file name {} is invalid. Please try again!".format(fname))
    quit()

counts = dict()
for lines in fhand:
    if not lines.startswith("From:"):
        continue
    pieces = lines.split()
    email = pieces[1]
    # print(email)
    atpos = email.find("@")
    orgname = email[atpos + 1:]
    # print(orgname)    # its all the email organizations
    counts[orgname] = counts.get(orgname, 0) + 1

lorg = list()
for org, ncount in counts.items():
    ntup = (org, ncount)
    lorg.append(ntup)
lorg = sorted(lorg)
for org, ncount in lorg:
    print(org, ncount)

print(counts)