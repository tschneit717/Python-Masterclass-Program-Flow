# If it can be used in a for loop, it is an iterable
for i in range(10, 2):
    print(i % 3)

parrot = "Norwegian Blue"

for character in parrot:
    print(character)

pets = (
    {"name": "Kirby", "type": "cat"},
    {"name": "Monty", "type": "cat"},
    {"name": "Banana", "type": "dog"},
    {"name": "Simon", "type": "cat"}
)

for pet in pets:
    print(pet)

number = input("Please enter a series of numbers using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))

