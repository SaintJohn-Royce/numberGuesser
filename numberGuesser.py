import random

number = random.randint(1,100)
inputNumber = input('please put in your guess: ')
inputNumber = int(inputNumber)

index = 0

while True:

	index += 1


	if inputNumber == number:

		print('correct, the number is indeed', number, '; took you', index, 'time(s) to solve')

		break

	elif inputNumber < number:

		inputNumber = input('your guess was too small, please retry: ')

		inputNumber = int(inputNumber)

	else: 
	#inputNumber > number:

		inputNumber = input('your guess was too large, please retry: ')

		inputNumber = int(inputNumber)