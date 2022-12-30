# for i in range(1, 13):
#     print("No. {:2} squared is {:3} and cubed is {:<4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)

name = input("Please enter your name: ")
age = int(input("Please enter your age, {0}? ".format(name)))
if age >= 18:
    print("You are old enough to vote")
    vote = input("Please type 'X' to vote: ")
    while vote != 'X':
        vote = input("You did not type 'X', please type 'X'")
    print("Thank you, {}".format(name))
elif age < 0 or age > 200:
    print("I don't think you understand the question, go home")
else:
    print('You are not old enough to vote')
    print('Please try again in {} years'.format(18 - age))