#!/usr/bin/env python3
from random import choice as randchoice
from termcolor import colored, cprint

def check_guess(guess, answer):

	print('\t ', end='')

	for i in range(5):
		if guess[i] == answer[i]:
			cprint(guess[i], 'white', 'on_green', end='')

		elif guess[i] in answer:
			cprint(guess[i], 'white', 'on_yellow', end='')

		else:
			cprint(guess[i], 'white', 'on_grey', end='')

	print('')

	if guess == answer:
		sys.exit('Correct!')

if __name__ == '__main__':

	word_list = []

	with open('word_list.txt', 'r') as word_list_file:
		for line in word_list_file:
			word_list.append(line.rstrip())

	answer = randchoice(word_list)

	for i in range(1,6):
		guess = input("Guess {}: ".format(i))

		while guess not in word_list:
			print('Invalid Guess')
			guess = input("Guess {}: ".format(i))

		check_guess(guess, answer)