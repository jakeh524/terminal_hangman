#!/usr/bin python3

# Author: Jake Herron
# Email: jakeh524@gmail.com

import random, os

def display(wrong_count):
	os.system('clear')
	print("------------------------------")
	if(wrong_count == 0):
		print("  _________         ")
		print("  |       |         ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print(" ---")
	elif(wrong_count == 1):
		print("  _________         ")
		print("  |       |         ")
		print("  |       O         ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print(" ---")
	elif(wrong_count == 2):
		print("  _________         ")
		print("  |       |         ")
		print("  |       O         ")
		print("  |       |         ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print(" ---")
	elif(wrong_count == 3):
		print("  _________         ")
		print("  |       |         ")
		print("  |       O         ")
		print("  |      \\|         ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print(" ---")
	elif(wrong_count == 4):
		print("  _________         ")
		print("  |       |         ")
		print("  |       O         ")
		print("  |      \\|/        ")
		print("  |                 ")
		print("  |                 ")
		print("  |                 ")
		print(" ---")
	elif(wrong_count == 5):
		print("  _________         ")
		print("  |       |         ")
		print("  |       O         ")
		print("  |      \\|/        ")
		print("  |       |         ")
		print("  |                 ")
		print("  |                 ")
		print(" ---")
	elif(wrong_count == 6):
		print("  _________         ")
		print("  |       |         ")
		print("  |       O         ")
		print("  |      \\|/        ")
		print("  |       |         ")
		print("  |      /          ")
		print("  |                 ")
		print(" ---")
	elif(wrong_count == 7):
		print("  _________         ")
		print("  |       |         ")
		print("  |       O         ")
		print("  |      \\|/        ")
		print("  |       |         ")
		print("  |      / \\        ")
		print("  |                 ")
		print(" ---")


def play_game(word):

	#init display
	wrong_count = 0
	display(wrong_count)

	#init word data
	word_len = len(word)
	blank_word = []
	for i in range(0, word_len):
		blank_word += ['_']
	print("Word:", ''.join(blank_word))
	wrong_letters = []
	print("Wrong Letters:", ', '.join(wrong_letters))
	print("------------------------------")

	#repeatedly take in and process letters
	end_flag = False
	while(end_flag == False):

		#get a letter from user
		valid_input = False
		while(valid_input == False):
			letter = input("Guess a letter: ")
			letter = letter.lower()
			valid_input = True
			if(len(letter) != 1):
				print("Please only enter a single letter. Try again.")
				valid_input = False
			if(letter < 'a' or letter > 'z'):
				print("Please enter a letter. Try again.")
				valid_input = False
			if(letter in wrong_letters or letter in blank_word):
				print("You already guessed that letter. Try again.")
				valid_input = False

		#letter is correct
		letter_found = False
		for i in range(0, word_len):
			if(word[i] == letter):
				blank_word[i] = letter
				letter_found = True

		#letter is wrong
		if(letter_found == False):
			wrong_count += 1
			wrong_letters.append(letter)

		#display
		display(wrong_count)
		print("Word:", ''.join(blank_word))
		print("Wrong Letters:", ', '.join(wrong_letters))
		print("------------------------------")

		#you win!
		if('_' not in blank_word):
			end_flag = True
			print("Congrats! You won Hangman!")
			return

		#you lose :/
		if(wrong_count == 7):
			end_flag = True
			print("Too bad... you lost Hangman.")
			return


			



def main():

	print("Welcome to Hangman!")

	#read in possible words from file
	with open("words.txt") as f:
		words_list = f.read().splitlines()
	
	#play the game loop
	continue_playing_flag = True
	while(continue_playing_flag == True):
		chosen_word = random.choice(words_list)
		play_game(chosen_word)
		answer = input("Would you like to play again? Enter 'yes' or 'no': ")
		if(answer == 'yes'):
			continue
		elif(answer == 'no'):
			continue_playing_flag = False
			print("Goodbye! See you next time! :)")
			exit(0)



if __name__ == "__main__":
	main()




