#Guess the Number Game
import random
def guessNumber(x):
    #range for the random_number
    random_number= random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess any number bewteen 1 to {x} :"))
        if guess > random_number:
            print(f'Sorry! Guess again your guess {guess}  is too High')
        elif guess < random_number:
            print(f"Sorry! Guess again your guess {guess}  is too Low")
    print(f'Yaay!! You Guessed it right {random_number}')

##guess game where computer guesses the number that we thought of by using low and high values as it constraints
def guess_computer(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is computers {guess} is too high (H), or too low (L),or it is correct (C): ').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'Yaay Computer guess your number {guess},correctly !')

guess_computer(200)