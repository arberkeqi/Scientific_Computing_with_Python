# for i in [5,4,3,2,1]:
#     print(i)
# print("Blastoff!")

# largest = -1
# for i in [3,41,5,74,15]:
#     if i > largest:
#         i = largest
#     print(i, largest)
# print("After", largest)

# Smallest number function
# smallest = None
# print("Before")
# for value in [9, 41, 12, -3, 74, 15]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print("After", smallest)

# Largest number function
largest = None
print("Before")
for value in [9, 41, 12, -3, 74, 15]:
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    print(largest, value)
print("After", largest)

# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         # break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)


# found = False
# print("Before", found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#         break
#     print(found, value)
# print("After", found)