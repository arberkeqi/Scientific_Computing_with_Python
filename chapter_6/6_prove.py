fruit = "banana"
i = 0
while i < len(fruit):
    letter = fruit[i]
    print(i, letter)
    i = i + 1

print()

for letter in fruit:
    print(letter)

print()

word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
print(count)

print()

word = "bananana"
i = word.find("na")
print(i)