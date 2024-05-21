import random
import time

while True:
    user_num = input('How many numbers do you want to include: ')

    if user_num.isdigit():
        user_num = int(user_num)

        if user_num < 0:
            print('Type a positive number')
            quit()
        else:
            break

    else:
        print('Type a number')

random_num = random.randint(1, user_num)
print(f"A random number has been chosen between 1 and {user_num}. Try to guess it!")
guesses = 0
start_time = time.time()

while True:
    guesses += 1
    user_guess = input('Guess the number: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number')
        continue

    if user_guess == random_num:
        end_time = time.time()
        time_taken = end_time - start_time
        print(f'You guessed correct! {random_num} was the right number! Your guessed {guesses} times in{time_taken: .2f} seconds 🤖')

        quit()
    elif user_guess < random_num:
        print(f'The number is greater than {user_guess}')
    else:
        print(f'The number is less than {user_guess}')
