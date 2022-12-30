age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("You should get a job")
elif age < 16:
    print("Get back to school")
else:
    print("Enjoy your retirement")

if 16 > age or age > 65:
    print("Have fun not working")
