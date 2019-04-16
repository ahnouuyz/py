import time
import pyautogui as pag

pag.PAUSE = 0.05
pag.FAILSAFE = True
REDCOLOR = (195, 36, 50)
REDPOS = (1, 80)
TIMEOUT = 10

def wait():
    start_time = time.time()
    while pag.screenshot().getpixel(REDPOS) != REDCOLOR:
        elapsed_time = time.time() - start_time
        if elapsed_time > TIMEOUT:
            raise TimeoutError('Timeout on wait().')
    time.sleep(0.5)

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

def activate_page():
    wait()
    pag.click(100, 100)
    pag.press('\t', presses=2)

def select_option(option_number):
    if option_number == 0:
        return
    elif option_number == 1:
        pag.press('space')
    else:
        pag.press('right', presses=option_number - 1)

def person_filling(person=None):
    if person == 'mother':
        pag.press('space')
    elif person == 'father':
        pag.press('right')
    elif person == None:
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
        wait()
        next_page()

def sears(pages, person=None):
    if len(pages) != 3:
        raise ValueError('Incorrect number of pages, expected 3.')
    # Skip the first page.
    wait()
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

def pss(page, person=None):
    if len(page) != 10:
        raise ValueError('Incorrect number of values, expected 10.')
    activate_page()
    for val in page:
        select_option(val)
        pag.press('\t')
    person_filling(person)

def skip_pss():
    wait()
    next_page()

def skip_srs():
    for i in range(6):
        wait()
        next_page()

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
        activate_page()
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
        activate_page()
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
        activate_page()
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
    wait()
    next_page()
    activate_page()
    person_filling(person)

def skip_les():
    for i in range(16):
        wait()
        next_page()

def skip_brief2():
    for i in range(7):
        wait()
        next_page()

def skip_ace():
    for i in range(2):
        wait()
        next_page()

def skip_sears():
    for i in range(4):
        wait()
        next_page()

def ace(pages, person=None):
    if len(pages) != 2:
        raise ValueError('Incorrect number of pages, expected 2.')
    for i, page in enumerate(pages):
        activate_page()
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
        pag.press('end')
        print(f'Skipping page {i + 1}...')
        if i in [13, 20, 22, 24]:
            print(f'Adding spaces to page {i + 1}...')
            activate_page()
            pag.press('space')
            pag.press('\t')
            pag.press('space')
        elif i == 18:
            print(f'Adding spaces to page {i + 1}...')
            activate_page()
            pag.press('space')
        elif i == 31:
            print(f'Adding spaces to page {i + 1}...')
            wait()
            pag.click(100, 100)
            for i in range(6):
                pag.hotkey('shift', '\t')
            pag.press('space')
        else:
            wait()
        next_page()


def main():
    page1 = ['010-20289', 'Roscoe', '16/04/2019']
    first_page(page1, first_entry=True)
    skip_cbcl()
    
##    skip_sears()
##    skip_pss()
##    skip_srs()
        
    sears39 = [[4, 3, 2, 4, 3, 3, 3, 3, 2, 2, 3, 3, 3],
               [3, 2, 2, 3, 3, 3, 3, 2, 3, 1, 4, 2, 3],
               [2, 3, 2, 3, 2, 2, 2, 4, 2, 2, 3, 2, 2]]
    sears(sears39, 'mother')
    next_page()
    pss10 = [1, 1, 3, 4, 4, 2, 3, 4, 3, 1]
    pss(pss10, 'mother')
    next_page()
    srs65 = [[4, 1, 4, 1, 2, 2, 3, 1, 2, 2, 4],
             [4, 2, 1, 4, 1, 1, 2, 2, 1, 4, 3],
             [1, 1, 2, 3, 2, 2, 1, 1, 2, 3, 1],
             [1, 1, 1, 1, 3, 2, 3, 1, 1, 4, 2],
             [3, 1, 2, 4, 2, 1, 1, 1, 1, 1, 3],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    srs(srs65, None)
    next_page()
    bsi53 = [[2, 1, 1, 2, 2, 2, 1, 1, 1, 5],
             [1, 2, 1, 2, 1, 1, 1, 2, 1, 5],
             [1, 1, 1, 3, 2, 4, 2, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 5, 1, 1]]
    bsi(bsi53, 'mother')
    next_page()
    mspss12 = [[5, 5, 5, 5, 5, 5],
               [5, 5, 5, 5, 5, 5]]
    mspss(mspss12, 'mother')
    next_page()

    les47a = [[0, 1, 1, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [0, 0, 1, 0, 1, 1, 1, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
              [0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]]
    les47b = [[6, 2],
              [],
              [3, 4, 6, 6, 6],
              [],
              [4, 4, 3, 6, 4, 4, 4],
              [5, 5, 4, 4, 4, 4, 4],
              [3, 3, 4]]
    les(les47a, les47b, 'father')
    next_page()

##    skip_les()

    skip_brief2()
    
    ace10 = [[2, 2, 2, 2, 2],
             [1, 1, 2, 2, 1]]
    ace(ace10, 'mother')
    next_page()
##    skip_ace()
##    skip_pcq()

    # Primary Caregiver Questionnaire
    # This will be extremely challenging...

if __name__ == '__main__':
    main()
