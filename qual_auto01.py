import time
import pyautogui as pag

pag.PAUSE = 0.1
pag.FAILSAFE = True

def next_page():
    pag.click(100, 100)
    for i in range(4):
        pag.hotkey('shift', '\t')
    pag.press('enter')

def prev_page():
    pag.click(100, 100)
    for i in range(5):
        pag.hotkey('shift', '\t')
    pag.press('enter')

def activate_page(delay=2):
    time.sleep(delay)
    pag.click(100, 100)
    pag.press('\t', presses=2)

def select_option(option_number):
    if option_number == 0:
        return
    elif option_number == 1:
        pag.press('space')
    else:
        pag.press('right', presses=option_number - 1)

def person_filling(person):
    if person == 'mother':
        pag.press('space')
    elif person == 'father':
        pag.press('right')
    elif person == 0:
        pass
    else:
        raise StopError('Manually select person filling in.')



def first_page(page, first_entry=True):
    activate_page()
    pag.typewrite(page[0])
    pag.press('\t')
    pag.typewrite(page[1])
    pag.press('\t')
    if first_entry:
        pag.typewrite(['space', '\t'])
    else:
        pag.typewrite(['down', '\t'])
    pag.typewrite(page[2])
    next_page()

def skip_cbcl():
    for i in range(13):
        time.sleep(2)
        next_page()

def sears(pages, person=None):
    if len(pages) != 3:
        raise ValueError('Incorrect number of pages, expected 3.')
    # Skip the first page.
    time.sleep(2)
    next_page()
    for i, page in enumerate(pages):
        if len(page) != 13:
            raise ValueError
        activate_page()
        for val in page:
            select_option(val)
            pag.press('\t')
        if i < 2:
            # Go to next page.
            next_page()
    person_filling(person)
    next_page()

def pss(page, person=None):
    if len(page) != 10:
        raise ValueError('Incorrect number of values, expected 10.')
    activate_page()
    for val in page:
        select_option(val)
        pag.press('\t')
    person_filling(person)

def srs(pages, person=None):
    if len(pages) != 6:
        raise ValueError('Incorrect number of pages, expected 6.')
    for i, page in enumerate(pages):
        activate_page()
        for val in page:
            select_option(val)
            pag.press('\t')
        if i < 5:
            next_page()
    person_filling(person)

def bsi(pages, person=None):
    if len(pages) != 5:
        raise ValueError('Incorrect number of pages, expected 5.')
    for i, page in enumerate(pages):
        activate_page(delay=3)
        for val in page:
            select_option(val)
            pag.press('\t')
        if i < 4:
            next_page()
    person_filling(person)

def mspss(pages, person=None):
    if len(pages) != 2:
        raise ValueError('Incorrect number of pages, expected 2.')
    for i, page in enumerate(pages):
        activate_page(delay=3)
        for val in page:
            select_option(val)
            pag.press('\t')
        if i < 1:
            next_page()
    person_filling(person)

def les(part1, part2, person=None):
    if len(part1) != 7:
        raise ValueError('Incorrect number of pages, expected 7.')
    for i in range(len(part1)):
        activate_page(delay=3)
        for j in range(len(part1[i])):
            select_option(part1[i][j])
            pag.press('\t')
            if (i == 1 and j == 5) or (i == 3 and j == 6):
                pag.press('\t')
        if any(x != 1 for x in part1[i]):
            next_page()
            activate_page()
            for val in part2[i]:
                select_option(val)
                pag.press('\t')
        if i < 6:
            next_page()
    next_page()
    # Skip others.
    time.sleep(2)
    next_page()
    activate_page()
    person_filling(person)

def skip_les():
    for i in range(16):
        time.sleep(2)
        next_page()

def skip_brief2():
    for i in range(7):
        time.sleep(2)
        next_page()

def skip_ace():
    for i in range(2):
        time.sleep(2)
        next_page()

def ace(pages, person=None):
    if len(pages) != 2:
        raise ValueError('Incorrect number of pages, expected 2.')
    for i, page in enumerate(pages):
        activate_page(delay=3)
        for val in page:
            select_option(val)
            pag.press('\t')
        if i < 1:
            next_page()
    person_filling(person)

def pcq():
    pass

def skip_pcq():
    for i in range(38):
        print(f'Skipping page {i + 1}...')
        if i in [13, 20, 22, 24]:
            print(f'Adding spaces to page {i + 1}...')
            activate_page(delay=3)
            pag.press('space')
            pag.press('\t')
            pag.press('space')
        elif i == 18:
            print(f'Adding spaces to page {i + 1}...')
            activate_page(delay=3)
            pag.press('space')
        elif i == 31:
            print(f'Adding spaces to page {i + 1}...')
            time.sleep(3)
            pag.click(100, 100)
            for i in range(6):
                pag.hotkey('shift', '\t')
            pag.press('space')
        else:
            time.sleep(2)
        next_page()


def main():
    page1 = ['010-20257', 'Roscoe', '16/04/2019']
    first_page(page1, first_entry=True)
    skip_cbcl()
    sears39 = [[1, 1, 1, 2, 2, 2, 2, 2, 4, 3, 3, 3, 3],
               [2, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 2],
               [4, 4, 3, 2, 3, 3, 3, 4, 3, 3, 3, 3, 2]]
    sears(sears39, 'father')
    pss10 = [3, 3, 4, 4, 1, 2, 3, 3, 3, 2]
    pss(pss10, 'father')
    next_page()
    srs65 = [[1, 1, 1, 2, 3, 3, 3, 2, 3, 2, 3],
             [3, 3, 2, 2, 1, 1, 1, 1, 2, 2, 2],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
             [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [2, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3],
             [2, 1, 1, 1, 1, 1, 1, 2, 2, 2]]
    srs(srs65, 'father')
    next_page()
    bsi53 = [[3, 3, 2, 4, 3, 3, 1, 2, 2, 1],
             [2, 2, 2, 1, 2, 2, 2, 3, 3, 3],
             [3, 3, 2, 2, 1, 1, 1, 1, 1, 2],
             [2, 2, 2, 1, 1, 2, 2, 2, 1, 1],
             [1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1]]
    bsi(bsi53, 'father')
    next_page()
    mspss12 = [[3, 3, 4, 4, 4, 3],
               [2, 4, 4, 4, 4, 4]]
    mspss(mspss12, 'father')
    next_page()

##    les47a = [[1, 1, 1, 1],
##              [3, 1, 1, 1, 1, 1, 1],
##              [3, 1, 1, 1, 1, 1, 1, 2, 2],
##              [1, 1, 1, 1, 1, 1, 1, 1],
##              [2, 1, 3, 3, 1, 2, 1, 1, 1, 1],
##              [3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
##    les47b = [[],
##              [3],
##              [2, 2, 6],
##              [],
##              [2, 3, 1, 7],
##              [2],
##              []]
##    les(les47a, les47b, 'mother')
##    next_page()

    skip_les()
    skip_brief2()
    skip_ace()
    skip_pcq()
##
##    ace10 = [[1, 2, 2, 1, 2],
##             [2, 2, 2, 2, 2]]
##    ace(ace10, 'mother')
##    next_page()

    # Primary Caregiver Questionnaire
    # This will be extremely challenging...

if __name__ == '__main__':
    main()
