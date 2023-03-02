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
	print_map = ['','','','','']

	# As far as I can tell, we MUST iterate through the answer twice - once for exact 
	# matches and once for partial matches.  With only one iteration, it's possible to 
	# reach an edge case where an exact match for a char occurs after a partial match, 
	# and we double mark the first char bc/ the alg hasn't yet seen the exact match.
	# --------------------------------------------------------------------------------
	# For example, if the answer is bukes, and out guess is supes, using only one iteration
	# will result in the first 's' in supes being marked a partial match.  This is incorrect,
	# since the only 's' in bukes is already accounted for with the exact match at the end.
	
	for i in range(5):
		if guess[i] == answer[i]:
			answer_dict[guess[i]] -= 1
			print_map[i] = 'g'

	for i in range(5):
		# Skip already discovered matches
		if print_map[i] == 'g':
			continue
		else:
			if guess[i] in answer_dict:
				if yellow_chars_dict[guess[i]] < answer_dict[guess[i]]:
					yellow_chars_dict[guess[i]] += 1
					print_map[i] = 'y'
				else:
					print_map[i] = 'x'
			
			else:
				bad_chars.add(guess[i])
				print_map[i] = 'x'

	if '' in print_map:
		sys.exit('error: unable to parse print_map')

	print_guess(guess, print_map)

	if guess == answer:
		print('\tCorrect!')
		sys.exit(0)

	return bad_chars

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