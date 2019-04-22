import csv
from pprint import pprint

def convert(row):
    return [int(val) if val.isnumeric() else val for val in row]

def insert_tabs(row):
    return ',\t,'.join(row).split(',')

def print_page(page):
    for val in page:
        if val == 'next_page':
            print('Next page.')
            return
        print(val, end='|')

with open('p2.txt') as f:
    reader = csv.reader(f)
    pages = [[val.strip() for val in line] for line in reader]
    pages = [insert_tabs(page) for page in pages]
    pages = [convert(page) + ['next_page'] for page in pages]

# pprint(pages, width=160)

for page in pages:
    print_page(page[1:])
