parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
    for i in range(len(parrot)):
        if parrot[i] == letter:
            print("I found the letter at the {} index".format(i))
else:
    print("I don't need that letter")
