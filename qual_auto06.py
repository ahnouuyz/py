""" Qualtrics is not an ideal data entry tool.
    It's an experience not to be missed.
"""

import time
import pyautogui as pag

pag.PAUSE = 0.02
pag.FAILSAFE = True
REDCOLOR = (195, 36, 50)
REDPOS = (1, 94)
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
        pag.hotkey('shift', 'tab')
    pag.press('enter')

def activate_page():
    wait()
    pag.click(100, 100)
    pag.press('tab', presses=2)

def fill_page(page):
    activate_page()
    for val in page:
        if isinstance(val, int):
            if val == 0:
                continue
            elif val == 1:
                pag.press('space')
            else:
                pag.press('right', presses=val - 1)
        elif isinstance(val, str):
            pag.typewrite(val)
        else:
            raise TypeError('Only int and str types recognized.')
        pag.press('tab')

def person_filling(person=None):
    if person == 'mother':
        pag.press('space')
    elif person == 'father':
        pag.press('right')
    elif person == 'maid':
        pag.press('right', presses=6)
    elif person == None:
        return
    else:
        raise ValueError('Unrecognized person filling in.')



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
    """ meta
        cbcl
        sears
        pss
        srs
        bsi
        mspss
        les
        brief2
        ace
    """
    for i, page in enumerate(pages):
        fill_page(page)
        if i == len(pages) - 1:
            person_filling(person)
        next_page()

def pcq():
    pass

def skip_pcq_13():
    for i in range(13):
        wait()
        if i in [9]:
            time.sleep(3)
        next_page()

# ========================================================================

def test():
    skip_pcq_13()

def main():
    metadata = [['010-21231', 'Roscoe', 1, '18/04/2019']]
    fill_pages(metadata, 'meta', None)

##    cbcl112 = [[2, '', 1, 3, 2, 1, 2, 2, 2, '', 2, 2],
##               [2, 1, 1, 2, 1, 1, 2, 1, 2, 2],
##               [2, 2, 1, 1, 2, 1, 1, 2, '', 2, 1],
##               [2, 1, 3, 2, 2, 3, 2, 2, 2, '', 1],
##               [2, 2, 2, 3, 2, 'Peel nails', 3, 2, 2, 1, 2],
##               [1, 2, 2, 2, 1],
##               [2, 2, 2, 'Redness around eyes', 3, 3, 2, 2, '', 1],
##               [2, 'Peel skin around nails', 3, 1, 1],
##               [1, 2, 2, 2, 1, '', 1, 1, 1, 1, '', 1],
##               [2, 1, '', 1, 2, 2, 2, '', 1, 2, '', 1, 2],
##               [1, 1, '', 1, '', 1, '', 1, 2, 2, 2, 1, 2],
##               [1, '', 1, 2, 2, 2, 1, 1, 1, 1, '', 1],
##               [1, 1, 1, 2, '', 1, 1, 2, 2, 2, 1, 1, 2]]
    try:
        fill_pages(_cbcl112, 'cbcl', 'mother')
    except NameError:
        skip('cbcl')

    sears39 = [[],
               [4, 3, 3, 3, 3, 4, 2, 4, 4, 4, 2, 2, 2],
               [2, 3, 4, 4, 4, 4, 4, 4, 2, 2, 3, 2, 2],
               [2, 4, 1, 3, 3, 2, 2, 4, 3, 3, 3, 3, 3]]
    try:
        fill_pages(sears39, 'sears', 'mother')
    except NameError:
        skip('sears')
    
    pss10 = [[4, 4, 4, 1, 2, 4, 2, 2, 4, 5]]
    try:
        fill_pages(pss10, 'pss', 'mother')
    except NameError:
        skip('pss')
    
    srs65 = [[1, 1, 4, 2, 2, 1, 2, 1, 1, 1, 3],
             [3, 1, 1, 3, 1, 3, 1, 2, 2, 2, 4],
             [1, 2, 2, 4, 1, 2, 1, 2, 2, 3, 1],
             [1, 1, 1, 1, 4, 2, 2, 1, 1, 2, 1],
             [2, 1, 1, 3, 1, 1, 1, 2, 1, 1, 2],
             [2, 1, 2, 1, 1, 1, 1, 1, 1, 1]]
    try:
        fill_pages(srs65, 'srs', 'mother')
    except NameError:
        skip('srs')
    
    bsi53 = [[4, 1, 4, 4, 2, 4, 3, 3, 5, 5],
             [5, 4, 5, 5, 2, 5, 5, 5, 5, 5],
             [5, 5, 4, 2, 5, 3, 5, 5, 4, 4],
             [5, 5, 4, 5, 5, 5, 5, 5, 5, 2],
             [3, 3, 5, 5, 5, 4, 5, 4, 5, 5, 5, 5, 5]]
    try:
        fill_pages(bsi53, 'bsi', 'mother')
    except NameError:
        skip('bsi')
    
    mspss12 = [[3, 3, 3, 4, 3, 4],
               [4, 3, 4, 3, 3, 3]]
    try:
        fill_pages(mspss12, 'mspss', 'mother')
    except NameError:
        skip('mspss')

    les47 = [[3, 1, 1, 0],
             [3, 1],
             [1, 1, 1, 1, 1, 1, '', 0],
             ['', 0],
             [2, 2, 1, 1, 1, 1, 1, 1, 1],
             [1, 4],
             [1, 1, 1, 1, 1, 1, 1, '', 0],
             ['', 0],
             [1, 1, 1, 1, 2, 1, 1, 2, 2, 1],
             [1, 1, 1],
             [2, 0, 1, 2, 2, 0, 1, 1, 1, 1],
             [1, 0, 1, 1, 0],
             [1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1],
             [1, 0],
             [],
             []]
    try:
        fill_pages(les47, 'les', 'mother')
    except NameError:
        skip('les')

##    brief2_63 = [[],
##                 [2, 2, 2, 2, 3, 2, 2, 2, 2, 2],
##                 [1, 2, 2, 2, 2, 2, 2, 1, 1, 2],
##                 [3, 2, 2, 2, 2, 2, 1, 1, 2, 2],
##                 [2, 2, 3, 2, 2, 1, 2, 2, 2, 2],
##                 [2, 3, 2, 1, 2, 2, 2, 2, 2, 2],
##                 [2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2]]
    try:
        fill_pages(_brief2_63, 'brief2', 'mother')
    except NameError:
        skip('brief2')
    
    ace10 = [[1, 1, 1, 1, 1],
             [2, 1, 1, 2, 2]]
    try:
        fill_pages(ace10, 'ace', 'mother')
    except NameError:
        skip('ace')

##    skip_pcq()


if __name__ == '__main__':
    main()
##    test()
