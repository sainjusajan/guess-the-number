import random

print("hello ! welcome to the Guess the number Game")
print("Whats your name?")
name = input()
print("Starting the game.")
guessedNumber = random.randint(1, 20)
print("I chose a number. What's your guess?" )

for guessnumber in range(1,7):
	guess = int(input())
	if guess > guessedNumber:
		print("Guess is Too HIGH")
	elif guess < guessedNumber:
		print("Guess is Too LOW")
	else:
		break;


if guess == guessedNumber:
	print("Congrats " + name + " you've won the game")
else:
	print("Sorry you've guessed enough")

exit()


