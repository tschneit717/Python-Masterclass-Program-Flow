print("Congratulations! You've been selected to go on a holiday!")
name = input("What is your name? ")
age = int(input("Hi {}! What is your age? ".format(name)))

if 18 <= age < 31:
    print("Awesome! You'll fit right in")
elif age >= 31:
    print("Hmm... looks like you're just out of the age range we're looking for. Sorry!")
else:
    print("You're too young to go!")