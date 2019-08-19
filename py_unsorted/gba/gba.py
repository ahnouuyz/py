#!/usr/bin/env python3

# Propose to simplify the data structure to a dictionary of lists of lists.
# The keys will be the words.
# The values will be lists containing lists.
# Each inner list is a revision.
# The first entry in each inner list will be a timestamp.
# Still use JSON for now.

import json
from string import ascii_letters
from time import strftime, localtime

timenow = lambda: strftime('%Y%m%d_%H%M', localtime())

class Vocab():
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read_json(filepath)

    def add_entry(self, word, sentence):
        """ Add a word into history
            [ok] If the word does not exist in the history, add the word and one example sentence
            [ok] Else display the existing sentence(s) and give the user an option to add one example sentence
        """
        keyword = self.keyword(word)
        message = [
            f'    1 - Add "{sentence}" to the list of example sentences.',
            f'    2 - Manually enter another sentence to add to the list of examples.',
            f'    Please enter one of the above options (anything else to quit): '
        ]

        if keyword in self.data:
            print(f'"{keyword}" already exists in history:')
            self.show_sentences(keyword)
        else:
            print(f'"{keyword}" does not exist in history:')

        try:
            choice = input('\n'.join(message)).split()[0]
            print()
        except(IndexError):
            return True

        if choice in '12':
            new_sentence = input('Enter sentence: ') if choice == '2' else sentence
            if keyword in self.data:
                self.data[keyword].append(self.data[keyword][-1] + [new_sentence])
                self.data[keyword][-1][0] = timenow()
            else:
                self.data[keyword] = [[timenow(), new_sentence]]

    def get_entry(self):
        print('Select a word in record, or enter a new word:')
        for i, word in enumerate(self.data):
            print(f'{i + 1} - {word}')
        word = input('Enter word (q to quit): ')
        if word.strip() == 'q':
            return True
        if word.strip().isnumeric():
            word = list(self.data)[int(word) - 1]
        sentence = input('Enter sentence (q to quit): ')
        if sentence.strip() == 'q':
            return True
        return self.add_entry(word, sentence)

    def get_revisions(self):
        print('Select a word in record:')
        for i, word in enumerate(self.data):
            print(f'{i + 1} - {word}')
        try:
            word = input('Enter word: ')
            if word.strip().isnumeric():
                word = list(self.data)[int(word) - 1]
            return self.revise_entry(word)
        except(KeyError):
            print(f'"{word}" is not a valid entry.')
            return True

    def keyword(self, word):
        """ Check that the proposed keyword:
            - is a single word
            - contains no spaces or symbols
            - (consider allowing dashes "-" in the future)
            Returns capitalized valid keywords
        """
        for letter in word:
            if letter not in ascii_letters:
                raise ValueError(f'"{word}" is not a valid keyword')
        return word.capitalize()
    
    def read_json(self, filepath):
        with open(filepath) as f:
            return json.loads(f.read())
    
    def revise_entry(self, word):
        """ Revise a word in history
            [ok] Display the chosen word and example sentence(s)
            [] The user has the option to choose the word based on the 
            [] latest revision time or 
            [ok] number of revisions made to the word
        """
        keyword = self.keyword(word)
        self.show_revisions(keyword)
        try:
            revision = int(input('Choose revision number (anything else to quit): '))
            print()
        except(ValueError):
            return True
        try:
            self.data[keyword].append(self.data[keyword][revision - 1])
            self.data[keyword][-1][0] = timenow()
        except(IndexError):
            return True

    def show_revisions(self, word):
        keyword = word.capitalize()
        for i, lst in enumerate(self.data[keyword]):
            rev = i + 1
            time = lst[0]
            sents = lst[1:]
            print(f'{keyword} (Revision {rev}, {time})\n{len(keyword) * "="}')
            for j, sent in enumerate(sents):
                print(f'{j + 1}. {sent}')
            print()

    def show_sentences(self, word, revision=-1):
        keyword = word.capitalize()
        print(f'{keyword}\n{len(keyword) * "="}')
        for i, sent in enumerate(self.data[keyword][revision][1:]):
            print(f'{i + 1}. {sent}')
        print()

    def to_json(self, filepath):
        with open(filepath, 'w') as f:
            f.write(json.dumps(self.data, indent=4))

    def user_prompt(self):
        print('1 - Input word/sentence.')
        print('2 - Revise current record.')
        try:
            choice = int(input('Choose an option (anything else to quit): '))
        except(ValueError):
            return True
        if choice == 1:
            return self.get_entry()
        elif choice == 2:
            return self.get_revisions()
        else:
            return True

def main():
    print()
    vocab = Vocab('history.json')
    while True:
        stop = vocab.user_prompt()
        if stop:
            print('--- Exit Program ---')
            break
        vocab.to_json('history.json')

# ============================================================================

def create_example_file():
    with open('examples.txt') as f:
        lines = [line.split() for line in f.read().splitlines()]

    examples = {}
    for line in lines:
        word = line[0]
        sentence = ' '.join(line[1:])
        if word in examples:
            examples[word][-1].append(sentence)
        else:
            examples[word] = [[timenow(), sentence]]
    print(examples)

    filepath = 'history.json'
    with open(filepath, 'w') as f:
        f.write(json.dumps(examples, indent=4))
    
if __name__ == '__main__':
#    create_example_file()
    main()
