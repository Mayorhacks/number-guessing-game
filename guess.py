import random

secret = random.randint(1,20)
tries = 0

while True:
	guess = int(input('guess a number from 1 t0 20:'))
	tries = tries + 1
	
	if guess < secret:
		print('Too low')
	elif guess > secret:
		print('Too high')
	else:
		print('you guess correctly', tries, 'tries')
		break


