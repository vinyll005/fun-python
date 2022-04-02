from random import randrange

searched_number = randrange(2, 19)
less_number = randrange(1, 10)
more_number = randrange(11, 20)

while True:
    if less_number < searched_number < more_number:
        break
    else:
        less_number = randrange(1, 10)
        more_number = randrange(11, 20)

print("Searched number is between " + str(less_number) + " and " + str(more_number))
print("Try to guess it!")

i = 0
correct_answer = False
while i < 3:
    user_number = input("Your number is: ")
    if (int(user_number) == searched_number):
        print("Congrats! You did it!")
        correct_answer = True
        break
    else:
        print("Oops, no, try again!")
        i += 1

if (correct_answer is False):
    print("You lose :( ")