#!/usr/bin/env python3

# Proposed data structure would be a dictionary of lists of dictionaries:
#    L1 Keys: <Words>
#    L1 Values: [Lists of dictionaries]:
#        Each item in the list is a dictionary:
#            L2 Keys: Time, Revision, Examples
#            L2 Values: Timestamp, Revision number, [List of example sentences]
# JSON would be a sensible choice for data file format.
# We name the file "history.json" temporarily. It may be changed to "history.txt" later.

import json
from string import ascii_letters
from time import strftime, localtime

timenow = lambda: strftime('%Y%m%d_%H%M', localtime())

class Vocab():
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read_json(filepath)
    
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
            Returns valid keywords in capital-case
            Raise an error for invalid keywords
        """
        for letter in word:
            if letter not in ascii_letters:
                raise ValueError(f'"{word}" is not a valid keyword')
        return word.capitalize()

    def show_revisions(self, word):
        keyword = word.capitalize()
        for dct in self.data[keyword]:
            revision = dct['Revision']
            time = dct['Time']
            sentences = dct['Examples']
            head = f'\n{keyword} (Revision {revision}, {time})\n{len(keyword) * "="}\n'
            body = '\n'.join([f'{i + 1}. {x}' for i, x in enumerate(sentences)])
            print(head + body)

    def show_sentences(self, word, revision=-1):
        keyword = word.capitalize()
        head = f'\n{keyword}\n{len(keyword) * "="}\n'
        body = '\n'.join([f'{i + 1}. {x}' for i, x in enumerate(self.data[keyword][revision]['Examples'])])
        print(head + body)

    def add_entry(self, word, sentence):
        """ Add a word into history
            [] If the word does not exist in the history, add the word and one example sentence
            [] Else display the existing sentence(s) and give the user an option to add one example sentence
        """
        keyword = self.keyword(word)
        if keyword in self.data:
            self.show_sentences(keyword)
            phrase = 'already exists'
        else:
            phrase = 'does not exist'
        lines = [
            f'    "{keyword}" {phrase} in history.\n'
            f'    1 - Add "{sentence}" to the list of example sentences.',
            f'    2 - Manually enter a sentence to add to the list of examples.',
            f'    Please enter one of the above options (anything else to quit): '
        ]
        message = '\n'.join(lines)
        try:
            choice = input(message).split()[0]
        except(IndexError):
            return None
        if choice in '12':
#            self.data[keyword] = self.data.get(keyword, []) + [{'Time': timenow()}]
            new_sentence = input('Enter sentence: ') if choice == '2' else sentence
#            self.data[keyword][-1]['Revision'] = len(self.data[keyword])
#            self.data[keyword][-1]['Examples'] = self.data[keyword][-2].get('Examples', []) + [new_sentence]
            if keyword in self.data:
                self.data[keyword][-1]['Revision'] = len(self.data[keyword])
                self.data[keyword][-1]['Examples'] = self.data[keyword][-1].get('Examples', []) + [new_sentence]
                ldct = self.get_latest_dct(keyword)
                dct = {
                    'Revision': ldct['Revision'] + 1,
                    'Examples': ldct['Examples'] + [new_sentence]
                }
            else:
                dct = {
                    'Revision': 1,
                    'Examples': [new_sentence]
                }
            dct['Time'] = timenow()
            self.data[keyword] = self.data.get(keyword, []) + [dct]

    def get_latest_dct(self, keyword):
        return self.data[keyword][-1]
    
    def revise_entry(self, word):
        """ Revise a word in history
            [] Display the chosen word and example sentence(s)
            [?] The user has the option to choose the word based on the latest revision time or number of revisions made to the word
        """
        keyword = self.keyword(word)
        self.show_revisions(word)

def main():
    print('-' * 60)
    vocab = Vocab('history.json')
    vocab.add_entry('newword', 'new sentence')
    vocab.add_entry('newword', 'yet another new sentence')
    vocab.revise_entry('newword')
    vocab.revise_entry('Ebullient')
#    for word in vocab.data:
#        vocab.show_revisions(word)



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
        data[word] = [{
            'Time': timenow(),
            'Revision': 1,
            'Examples': sentences
        }]
    print(data)

    filepath = 'history.json'
    with open(filepath, 'w') as f:
        f.write(json.dumps(data, indent=4))
    
if __name__ == '__main__':
#    create_example_file()
    main()
