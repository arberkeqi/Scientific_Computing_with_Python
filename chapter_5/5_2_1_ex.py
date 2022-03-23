largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    if largest is None:
        largest = num
    elif num == largest:
        largest = num
    
    print(largest, num)
    print(num)

print("Maximum", largest)

print("Before")
for value in [9, 41, 12, -3, 74, 15]:
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    print(largest, value)
print("After", largest)