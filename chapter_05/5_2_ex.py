largest = None
smallest = None

while True:
    nums = input("Enter a number: ")
    if nums == "done":
        break
    try:
        badVal = int(nums)
    except:
        print("Invalid input")
        continue

    num = int(nums)
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    # print("Largest", largest, num)
    
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    # print("Smallest", smallest, num)

print("Maximum is", largest)

print("Minimum is", smallest)
