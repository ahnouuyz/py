""" Qualtrics is not an ideal data entry tool.
    It's an experience not to be missed!
    PCQ is a nightmare!
"""

import time
import pyautogui as pag

pag.PAUSE = 0.02
pag.FAILSAFE = True
REDCOLOR = (195, 36, 50)
REDPOS = (1, 94)

def wait(delay=0.5, timeout=60):
    """ Wait until the red bar appears at the top-left corner.
        This may not work properly for pages that are too short.
    """
    start_time = time.time()
    while pag.screenshot().getpixel(REDPOS) != REDCOLOR:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            raise TimeoutError(f'Timeout. {elapsed_time:.2f} s have passed.')
    time.sleep(delay)

def next_page():
    pag.click(100, 100)
    for _ in range(4):
        pag.hotkey('shift', 'tab')
    pag.press('enter')

def nperson(person):
    dct = {None: 0, 
           'mother': 1, 
           'father': 2, 
           'maid':, 6}
    return dct[person]

def fill_page(page):
    wait()
    pag.click(100, 100)
    pag.press('tab')
    for val in page:
        pag.press('tab')
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

def enter_data(data):
    saqs = ['meta', 
            'cbcl', 
            'sears', 
            'pss', 
            'srs', 
            'bsi', 
            'mspss', 
            'les', 
            'brief2', 
            'ace']
#            , 
#            'pcq']
    for saq in saqs:
        try:
            for page in data[saq]:
                fill_page(page)
                next_page()
        except KeyError:
            skip(saq)

def skip(saq):
    skip_pages = {'meta': 1, 
                  'cbcl': 13, 
                  'sears': 4, 
                  'pss': 1, 
                  'srs': 6, 
                  'bsi': 5, 
                  'mspss': 2, 
                  'les': 16, 
                  'brief2': 7, 
                  'ace': 2}
    for _ in range(skip_pages[saq]):
        wait()
        next_page()

# ========================================================================

def main():
    data = {
        'meta': [['010-21231', 'Roscoe', 1, '18/04/2019']],
#        'cbcl': [[2, '', 1, 3, 2, 1, 2, 2, 2, '', 2, 2],
#                 [2, 1, 1, 2, 1, 1, 2, 1, 2, 2],
#                 [2, 2, 1, 1, 2, 1, 1, 2, '', 2, 1],
#                 [2, 1, 3, 2, 2, 3, 2, 2, 2, '', 1],
#                 [2, 2, 2, 3, 2, 'Peel nails', 3, 2, 2, 1, 2],
#                 [1, 2, 2, 2, 1],
#                 [2, 2, 2, 'Redness around eyes', 3, 3, 2, 2, '', 1],
#                 [2, 'Peel skin around nails', 3, 1, 1],
#                 [1, 2, 2, 2, 1, '', 1, 1, 1, 1, '', 1],
#                 [2, 1, '', 1, 2, 2, 2, '', 1, 2, '', 1, 2],
#                 [1, 1, '', 1, '', 1, '', 1, 2, 2, 2, 1, 2],
#                 [1, '', 1, 2, 2, 2, 1, 1, 1, 1, '', 1],
#                 [1, 1, 1, 2, '', 1, 1, 2, 2, 2, 1, 1, 2, nperson('mother')]],
        'sears': [[],
                  [4, 3, 3, 3, 3, 4, 2, 4, 4, 4, 2, 2, 2],
                  [2, 3, 4, 4, 4, 4, 4, 4, 2, 2, 3, 2, 2],
                  [2, 4, 1, 3, 3, 2, 2, 4, 3, 3, 3, 3, 3, nperson('mother')]],
        'pss': [[4, 4, 4, 1, 2, 4, 2, 2, 4, 5, nperson('mother')]],
        'srs': [[1, 1, 4, 2, 2, 1, 2, 1, 1, 1, 3],
                [3, 1, 1, 3, 1, 3, 1, 2, 2, 2, 4],
                [1, 2, 2, 4, 1, 2, 1, 2, 2, 3, 1],
                [1, 1, 1, 1, 4, 2, 2, 1, 1, 2, 1],
                [2, 1, 1, 3, 1, 1, 1, 2, 1, 1, 2, nperson('mother')],
                [2, 1, 2, 1, 1, 1, 1, 1, 1, 1]],
        'bsi': [[4, 1, 4, 4, 2, 4, 3, 3, 5, 5],
                [5, 4, 5, 5, 2, 5, 5, 5, 5, 5],
                [5, 5, 4, 2, 5, 3, 5, 5, 4, 4],
                [5, 5, 4, 5, 5, 5, 5, 5, 5, 2],
                [3, 3, 5, 5, 5, 4, 5, 4, 5, 5, 5, 5, 5, nperson('mother')]],
        'mspss': [[3, 3, 3, 4, 3, 4],
                  [4, 3, 4, 3, 3, 3, nperson('mother')]],
        'les': [[3, 1, 1, 0],
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
                [nperson('mother')]],
#        'brief2': [[],
#                   [2, 2, 2, 2, 3, 2, 2, 2, 2, 2],
#                   [1, 2, 2, 2, 2, 2, 2, 1, 1, 2],
#                   [3, 2, 2, 2, 2, 2, 1, 1, 2, 2],
#                   [2, 2, 3, 2, 2, 1, 2, 2, 2, 2],
#                   [2, 3, 2, 1, 2, 2, 2, 2, 2, 2],
#                   [2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, nperson('mother')]],
        'ace': [[1, 1, 1, 1, 1],
                [2, 1, 1, 2, 2, nperson('mother')]],
#        'pcq': [[]]
    }

    enter_data(data)

if __name__ == '__main__':
    main()
