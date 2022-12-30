answer = 5
print("Please guess a number between 1 and 10:")
guess = int(input())
while guess != answer:
    if guess < answer:
        print("Try again! You're too low")
    elif guess > answer:
        print("Try again! You're too high")
    guess = int(input())

print("Wow you got it right!")