import random
print('Welcome to the Guessing Game!')

number = random.randint(1, 100)
guess = 0
while guess != number:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess > 100 or guess < 1:
        print('Please enter a number between 1 and 1001')
        continue
    if guess < number:
        print('Too Low')
    elif guess > number:
        print('Too High')
    elif guess == number:
        print('Correct!')
        break
