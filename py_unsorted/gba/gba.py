#!/usr/bin/env python3

"""
Tasks:
Add a word into "history.txt":
[] If the word does not exist in the history, add the word and one example sentence
[] Else display the existing sentence(s) and give the user an option to add one example sentence
Revise a word in "history.txt":
[] Display the chosen word and example sentence(s)
[?] The user has the option to choose the word based on the latest revision time or number of revisions made to the word
"""

# Proposed data structure would be a dictionary of lists of dictionaries:
#	L1 Keys: <Words>
#	L1 Values: Lists of dictionaries:
#		Each item in the list is a dictionary:
#			L2 Keys: Time, Revision, Examples
#			L2 Values: Timestamp, Revision number, List of example sentences
# JSON would be the sensible choice for data file format.
# We name the file "history.json" temporarily. It may be changed to "history.txt" later.

# Management of keys: Make sure all words follow a standard. E.g. Capitalize.

import json
from string import ascii_letters
from time import strftime, localtime

timenow = lambda: strftime('%Y%m%d_%H%M', localtime())

class Vocab():
	def __init__(self, filepath):
		self.filepath = filepath
		self.data = self.read_json(filepath)
	
	def __str__(self):
		head = 'Words available in list:\n'
		body = '\n'.join([f'{i + 1:>5} - {k} - {len(v["Examples"])} example(s)' for i, (k, v) in enumerate(self.data.items())])
		return head + body + '\n'
	
	def read_json(self, filepath):
		with open(filepath) as f:
			return json.loads(f.read())
	
	def to_json(self, filepath):
		with open(filepath) as f:
			f.write(json.dumps(self.data, indent=4))

	def keyword(self, word):
		""" Check that the proposed keyword:
			- is a single word
			- contains no spaces or symbols
			- (consider allowing dashes "-" in the future)
			Returns valid keywords in capital-case.
			Raise an error for invalid keywords
		"""
		for letter in word:
			if letter not in ascii_letters:
				raise ValueError(f'"{word}" is not a valid keyword')
		return word.capitalize()

	def show_sentences(self, word):
		keyword = word.capitalize()
		for dct in self.data[keyword]:
			head = f'\n{keyword} (Revision {dct["Revision"]}, {dct["Time"]})\n{len(keyword) * "="}\n'
			body = '\n'.join([f'{i + 1}. {x}' for i, x in enumerate(dct['Examples'])])
			print(head + body)

	def add_entry(self, word, sentence):
		keyword = self.keyword(word)
		lines = [
			f'    1 - Add "{sentence}" to the list of example sentences.',
			f'    2 - Manually enter a sentence to add to the list of examples.',
			f'    Please enter one of the above options (anything else to quit): '
		]
		if keyword not in self.data:
			message = f'"{keyword}" does not exist in history.\n' + '\n'.join(lines)
			try:
				choice = input(message).split()[0].lower()
				if choice in '12':
					if choice == '1':
						new_sentence = sentence
					elif choice == '2':
						new_sentence = input('Enter sentence: ')
					dct = {
						'Time': timenow(),
						'Revision': 1,
						'Examples': [new_sentence]
					}
					self.data[keyword] = [dct]
			except(IndexError):
				pass
		else:
			message = f'"{keyword}" already exists in history.\n' + '\n'.join(lines)
			try:
				choice = input(message).split()[0].lower()
				if choice in '12':
					if choice == '1':
						new_sentence = sentence
					elif choice == '2':
						new_sentence = input('Enter sentence: ')
					dct = {
						'Time': timenow(),
						'Revision': self.data[keyword][-1]['Revision'] + 1,
						'Examples': self.data[keyword][-1]['Examples'] + [new_sentence]
					}
					self.data[keyword].append(dct)
			except(IndexError):
				pass
	
	def revise_entry(self, word):
		keyword = self.keyword(word)
		self.show_sentences(word)

def main():
	print('-' * 60)
	vocab = Vocab('history.json')
	vocab.add_entry('newword', 'new sentence')
	vocab.add_entry('newword', 'yet another new sentence')
	vocab.revise_entry('Belligerent')
#	for word in vocab.data:
#		vocab.show_sentences(word)



def create_example_file():
	with open('examples.txt') as f:
		lines = f.read().splitlines()
	lines = [line.split() for line in lines]

	examples = {}
	for line in lines:
		word = line[0]
		sentence = ' '.join(line[1:])
		examples[word] = examples.get(word, []) + [sentence]
	print(examples)
	print()

	data = {}
	for word, sentences in examples.items():
		data[word] = {
			'Time': timenow(),
			'Revision': 1,
			'Examples': sentences
		}
	print(data)

	filepath = 'history.json'
	with open(filepath, 'w') as f:
		f.write(json.dumps(data, indent=4))
	
if __name__ == '__main__':
	create_example_file()
#	main()
