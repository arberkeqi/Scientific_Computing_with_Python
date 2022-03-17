num = input("Enter number: ")
try:
    ival = int(num)
except:
    ival = input("Enter a number:")

if ival < 10:
    print("Smaller than 10")
elif ival > 10:
    print("Bigger than 10")
else:
    print("equal to 10")