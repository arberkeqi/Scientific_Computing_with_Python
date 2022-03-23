text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(":")
print(ipos)
piece = text[ipos + 1:]
print(piece)
snum = piece.strip()
print(snum)
num = float(snum)
print(num)
print(type(num))
# num = text.find("0.8475")
# print(num)
# ftext = float(text[23:])
# print(ftext)