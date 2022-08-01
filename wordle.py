#!/usr/bin/env python3
import sys, random
from termcolor import colored, cprint
from collections import defaultdict

def print_guess(guess, print_map):

	print('\t ', end='')

	for i in range(5):
		if print_map[i] == 'g':
			cprint(guess[i], 'white', 'on_green', end='')

		elif print_map[i] == 'y':
			cprint(guess[i], 'white', 'on_yellow', end='')

		else:
			cprint(guess[i], 'white', 'on_grey', end='')

def check_guess(guess, answer):

	answer_dict = defaultdict(int)
	for char in answer:
		answer_dict[char] += 1

	yellow_chars_dict = defaultdict(int)
	bad_chars = set()
	print_map = []

	print('\t ', end='')

	for i in range(5):
		if guess[i] == answer[i]:
			answer_dict[guess[i]] -= 1
			print_map.append('g')

		elif guess[i] in answer_dict:
			if yellow_chars_dict[guess[i]] < answer_dict[guess[i]]:
				yellow_chars_dict[guess[i]] += 1
				print_map.append('y')
			else:
				print_map.append('x')
		
		else:
			bad_chars.add(guess[i])
			print_map.append('x')

	print_guess(guess, print_map)

	return bad_chars

	if guess == answer:
		sys.exit('Correct!')

if __name__ == '__main__':

	word_list = []

	with open('word_list.txt', 'r') as word_list_file:
		for line in word_list_file:
			word_list.append(line.rstrip())

	answer = random.choice(word_list)

	bad_chars = set()

	for i in range(1,6):
		guess = input("Guess {}: ".format(i))

		while guess not in word_list:
			print('Invalid Guess')
			guess = input("Guess {}: ".format(i))

		bad_chars.update(check_guess(guess, answer))

		cprint('\t\t{}'.format(''.join(sorted(bad_chars))), 'white', 'on_grey')

	print('Answer:  {}'.format(answer))