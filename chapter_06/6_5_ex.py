text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(":")       # find the ":"
print(ipos)
piece = text[ipos + 1:]     # extract the portion of text from ":" to the end
print(piece)
snum = piece.strip()        # remove the whitespace
print(snum)
num = float(snum)           # turn it into a float point
print(num)
print(type(num))
# num = text.find("0.8475")
# print(num)
# ftext = float(text[23:])
# print(ftext)