
#     Guessing game challenge 


import random

answer = int(random.randint(1,100))

print('Guess the number I have in mind, it should be between 1 and 100')

guess = int(input("What is your guess ? Enter a number here:"))
mylist = [] # will store the answers for each round

while guess != answer:
    if guess < 1 or guess > 100:
        print('out of bound, it should be between 1 and 100, this try does not count')
    else:
        if len(mylist) == 0: #for the first turn
            if abs(guess - answer) <= 10 and abs(guess - answer) >= 1:
                print('WARM! within 10 of the number')
            else:
                print('COLD! further than 10 away')
        else: #for subsequent turns
            if abs(int(mylist[-1]) - answer) > abs(answer - guess):
                print(f'{guess} is warmer than {mylist[-1]}')
            else:
                print(f'{guess} is colder than {mylist[-1]}')
    mylist.append(guess)
    guess = int(input("Enter a number here:"))
else:
    mylist.append(guess) #add the guess to mylist
    times = len(mylist) #number of element in the mylist, which is number of guesses
    print(f'great! the answer was {guess} and it took {times} time(s) to guess\nyour guess(es) was/were {mylist}')      


#  
