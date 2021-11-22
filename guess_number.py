import random

given_number = input("Type a number : ")
if given_number.isdigit():
    given_number = int(given_number)

    if given_number <= 0:
        print("Please type a number larger than Zero next time.")
        quit()
else:
    print("Please type a digit next time.")
    quit()


random_number = random.randint(0, given_number)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("please make a guess :")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time ..!")
        break

    if user_guess == random_number:
        print("Wow....You got the number...!")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")
print("You got it in", guess_count , "guesses")



