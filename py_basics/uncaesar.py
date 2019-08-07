import string

def main():
    cts = {
        'ct1': 'upbtu',
        'ct2': 'Uryyb, zl anzr vf Puhpx naq V arrq zbarl naq n wrg.',
        'ct3': 'Jub vf perqvgrq nf orvat bar bs gur vairagbef bs Rgurearg?',
        'ct4': 'Jung qbrf gur Gjvggre unfugnt #VUGF fgnaq sbe?',
        'ct5': 'Internet History Technology and Security'
    }
    for v in cts.values():
        print(try26(v), end='\n\n')

def shift_char(char, shift):
    if char in string.ascii_lowercase:
        shifted_index = (string.ascii_lowercase.find(char) + shift) % 26
        return string.ascii_lowercase[shifted_index]
    elif char in string.ascii_uppercase:
        shifted_index = (string.ascii_uppercase.find(char) + shift) % 26
        return string.ascii_uppercase[shifted_index]

def shift_text(text, shift):
    text = list(text)
    for i, char in enumerate(text):
        if char in string.ascii_letters:
            text[i] = shift_char(char, shift)
    return ''.join(text)

def try26(text):
    return '\n'.join(f'{i:>5} - {shift_text(text, i)}' for i in range(26))

if __name__ == '__main__':
    main()
