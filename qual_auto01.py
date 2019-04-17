""" Qualtrics is not an ideal data entry tool.
    It's an experience not to be missed.
"""

import time
import pyautogui as pag

pag.PAUSE = 0.02
pag.FAILSAFE = True
REDCOLOR = (195, 36, 50)
REDPOS = (1, 80)
TIMEOUT = 60

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
        if isinstance(val, int):
            select_option(val)
        elif isinstance(val, str):
            pag.typewrite(val)
        else:
            raise TypeError('Only int and str types recognized.')
        pag.press('\t')

def person_filling(person=None):
    if person == 'mother':
        pag.press('space')
    elif person == 'father':
        pag.press('right')
    elif person == 'maid':
        pag.press('right', presses=6)
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

def fill_pages(pages, saq, person):
    """ cbcl
        sears
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
    metadata = ('010-20861', 'Roscoe', '17/04/2019')
    first_page(metadata, first_entry=True)

    cbcl112 = [[2, '', 1, 3, 2, 1, 1, 2, 2, '', 2, 2],
               [2, 2, 1, 2, 1, 1, 1, 1, 2, 1],
               [1, 2, 1, 2, 1, 2, 2, 2, '', 3, 2],
               [2, 1, 1, 1, 1, 1, 1, 2, 1, '', 1],
               [1, 1, 1, 1, 1, '', 1, 2, 1, 1, 1],
               [1, 1, 1, 1, 1],
               [1, 1, 1, '', 1, 1, 1, 1, '', 1],
               [1, '', 1, 1, 1],
               [1, 1, 2, 2, 1, '', 1, 1, 1, 1, '', 1],
               [2, 1, '', 1, 1, 2, 1, '', 1, 1, '', 1, 1],
               [1, 1, '', 1, '', 1, '', 1, 1, 1, 1, 1, 1],
               [1, '', 1, 2, 1, 1, 1, 1, 1, 1, '', 1],
               [1, 1, 1, 1, '', 1, 1, 1, 1, 1, 1, 1, 1]]
    fill_pages(cbcl112, 'cbcl', 'mother')
##    skip('cbcl')

    sears39 = [[],
               [3, 3, 2, 2, 2, 3, 4, 3, 2, 2, 2, 2, 3],
               [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 2, 2, 3, 2, 2, 2, 3, 1, 2, 1, 2, 2]]
    fill_pages(sears39, 'sears', 'mother')
##    skip('sears')
    
    pss10 = [[3, 3, 3, 5, 3, 3, 4, 4, 3, 3]]
    fill_pages(pss10, 'pss', None)
##    skip('pss')
    
    srs65 = [[1, 1, 3, 2, 3, 1, 2, 1, 1, 2, 3],
             [3, 2, 1, 4, 1, 4, 1, 2, 1, 2, 4],
             [1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1],
             [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1],
             [2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    fill_pages(srs65, 'srs', 'mother')
##    skip('srs')
    
    bsi53 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    fill_pages(bsi53, 'bsi', 'mother')
##    skip('bsi')
    
    mspss12 = [[5, 5, 5, 5, 5, 5],
               [5, 5, 5, 5, 5, 5]]
    fill_pages(mspss12, 'mspss', 'mother')
##    skip('mspss')

    les47 = [[0, 1, 1, 1],
             [7],
             [1, 0, 0, 0, 0, 0, '', 0],
             [0, 0, 0, 0, 0, '', 0],
             [1, 1, 1, 0, 1, 0, 1, 1, 1],
             [7, 0],
             [1, 0, 0, 0, 0, 0, 0, '', 0],
             [0, 0, 0, 0, 0, 0, '', 0],
             [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
             [7],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
             [0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##             [],
             [],
             []]
    fill_pages(les47, 'les', 'mother')
##    skip('les')

    brief2_63 = [[],
                 [1, 1, 1, 2, 1, 1, 2, 2, 1, 1],
                 [1, 2, 2, 1, 2, 1, 1, 1, 1, 2],
                 [1, 1, 2, 2, 1, 2, 1, 1, 2, 1],
                 [1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
                 [2, 1, 1, 1, 2, 2, 2, 1, 1, 1],
                 [2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2]]
    fill_pages(brief2_63, 'brief2', 'mother')
##    skip('brief2')
    
##    ace10 = [[2, 2, 2, 2, 2],
##             [2, 2, 2, 2, 2]]
##    fill_pages(ace10, 'ace', 'father')
    skip('ace')

##    skip_pcq()


if __name__ == '__main__':
    main()
