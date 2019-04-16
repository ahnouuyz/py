""" Qualtrics is not an ideal data entry tool.
    It's an experience not to be missed.
"""

import time
import pyautogui as pag

pag.PAUSE = 0.05
pag.FAILSAFE = True
REDCOLOR = (195, 36, 50)
REDPOS = (1, 80)
TIMEOUT = 10

def wait(delay=0.5):
    """ Need to find an event that is unique to completing a page load.
    """
    start_time = time.time()
    while pag.screenshot().getpixel(REDPOS) != REDCOLOR:
        elapsed_time = time.time() - start_time
        if elapsed_time > TIMEOUT:
            raise TimeoutError('Timeout on wait().')
    time.sleep(delay)

def next_page():
    pag.click(100, 100)
    for i in range(4):
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

def fill_page(page):
    activate_page()
    for val in page:
        select_option(val)
        pag.press('\t')

def person_filling(person=None):
    if person == 'mother':
        pag.press('space')
    elif person == 'father':
        pag.press('right')
    elif person == None:
        pass
    else:
        raise ValueError('Unrecognized person filling in.')



def first_page(metadata, first_entry=True):
    pscid, enterer, date = metadata
    activate_page()
    pag.typewrite(pscid)
    pag.press('\t')
    pag.typewrite(enterer)
    pag.press('\t')
    pag.typewrite([('down', 'space')[first_entry], '\t'])
    pag.typewrite(date)
#    pag.typewrite(page[0])
#    pag.press('\t')
#    pag.typewrite(page[1])
#    pag.press('\t')
#    if first_entry:
#        pag.typewrite(['space', '\t'])
#    else:
#        pag.typewrite(['down', '\t'])
#    pag.typewrite(page[2])
    next_page()

def skip(saq):
    saqs = {'cbcl': 13, 
            'sears': 4, 
            'pss': 1, 
            'srs': 6, 
            'bsi': 5, 
            'mspss': 2, 
            'les': 16, 
            'brief2': 7, 
            'ace': 2}
    for i in range(saqs[saq]):
        wait()
        next_page()

def fill_pages(pages, person=None):
    """ sears
        pss
        srs
        bsi
        mspss
        ace
    """
    for i, page in enumerate(pages):
        fill_page(page)
        if i == len(pages) - 1:
            person_filling(person)
        next_page()

def les(part1, part2, person=None):
    for i, (page1, page2) in enumerate(zip(part1, part2)):
        activate_page()
        for j, val in enumerate(page1):
            select_option(val)
            pag.press('\t')
            if (i == 1 and j == 5) or (i == 3 and j == 6):
                pag.press('\t')
        if any(x != 1 for x in page1):
            next_page()
            fill_page(page2)

    for i in range(len(part1)):
        activate_page()
        for j in range(len(part1[i])):
            select_option(part1[i][j])
            pag.press('\t')
            if (i == 1 and j == 5) or (i == 3 and j == 6):
                pag.press('\t')
        if any(x != 1 for x in part1[i]):
            next_page()
            fill_page(part2[i])
        if i < 6:
            next_page()
    next_page()
    wait()
    next_page()
    activate_page()
    person_filling(person)

def pcq():
    pass

def skip_pcq():
    """ There are still issues...
    """
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
    metadata = ['010-20289', 'Roscoe', '16/04/2019']
    sears39 = [[],
               [4, 3, 2, 4, 3, 3, 3, 3, 2, 2, 3, 3, 3],
               [3, 2, 2, 3, 3, 3, 3, 2, 3, 1, 4, 2, 3],
               [2, 3, 2, 3, 2, 2, 2, 4, 2, 2, 3, 2, 2]]
    pss10 = [[1, 1, 3, 4, 4, 2, 3, 4, 3, 1]]
    srs65 = [[4, 1, 4, 1, 2, 2, 3, 1, 2, 2, 4],
             [4, 2, 1, 4, 1, 1, 2, 2, 1, 4, 3],
             [1, 1, 2, 3, 2, 2, 1, 1, 2, 3, 1],
             [1, 1, 1, 1, 3, 2, 3, 1, 1, 4, 2],
             [3, 1, 2, 4, 2, 1, 1, 1, 1, 1, 3],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    bsi53 = [[2, 1, 1, 2, 2, 2, 1, 1, 1, 5],
             [1, 2, 1, 2, 1, 1, 1, 2, 1, 5],
             [1, 1, 1, 3, 2, 4, 2, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 5, 1, 1]]
    mspss12 = [[5, 5, 5, 5, 5, 5],
               [5, 5, 5, 5, 5, 5]]
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
    ace10 = [[2, 2, 2, 2, 2],
             [1, 1, 2, 2, 1]]

    first_page(metadata, first_entry=True)
    skip('cbcl')

    fill_pages(sears39, 'mother')
#    skip('sears')

    fill_pages(pss10, 'mother')
#    skip('pss')

    fill_pages(srs65, None)
#    skip('srs')

    fill_pages(bsi53, 'mother')

    fill_pages(mspss12, 'mother')

    les(les47a, les47b, 'father')
    next_page()
#    skip_les()

    skip_brief2()

    fill_pages(ace10, 'mother')
#    skip_ace()

#    skip_pcq()


if __name__ == '__main__':
    main()
