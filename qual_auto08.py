""" Qualtrics is not an ideal data entry tool.
    It's an experience not to be missed!
    PCQ is a nightmare!
"""

import webbrowser
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
    elapsed_time = 0
    while pag.screenshot().getpixel(REDPOS) != REDCOLOR:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            raise TimeoutError(f'Timeout. {elapsed_time:.2f} s have passed.')
    if elapsed_time < 0.1:
        time.sleep(2)
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
           'maid': 6}
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

def skip_pcq():
    for i in range(41):
        wait()
        if i in [13, 20, 22, 24]:
            blank_top(n=2)
        elif i == 18:
            blank_top(n=1)
        elif i == 31:
            blank_bot(n=1)
        next_page()

def blank_top(n=2):
    pag.click(100, 100)
    if n > 0:
        pag.press(['\t', '\t', 'space'])
    if n > 1:
        pag.press(['\t', 'space'])
    if n > 2:
        raise NotImplementedError('n > 2 is not supported.')

def blank_bot(n=1):
    pag.click(100, 100)
    for _ in range(6):
        pag.hotkey('shift', '\t')
    pag.press('space')

def open_page():
    url = 'https://qau1.au1.qualtrics.com/jfe/form/SV_1UjsQDl2Rut8JZr'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)

# ========================================================================

def main():
    data = {
        'meta': [['010-21534', 'Roscoe', 1, '22/04/2019']],
##        'cbcl': [[1, '', 1, 2, 1, 1, 1, 2, 2, '', 1, 2],
##                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                 [1, 1, 1, 1, 1, 1, 2, 1, '', 2, 1],
##                 [1, 1, 2, 1, 1, 2, 1, 1, 1, '', 1],
##                 [1, 1, 1, 1, 1, '', 1, 1, 1, 1, 1],
##                 [1, 1, 1, 1, 1],
##                 [1, 1, 1, '', 1, 1, 1, 1, '', 1],
##                 [1, '', 1, 1, 1],
##                 [1, 1, 1, 1, 1, '', 1, 1, 1, 1, '', 1],
##                 [1, 1, '', 1, 1, 2, 1, '', 1, 2, '', 1, 1],
##                 [1, 1, '', 1, '', 1, '', 1, 1, 1, 1, 1, 1],
##                 [1, '', 1, 2, 1, 1, 1, 1, 1, 1, '', 1],
##                 [1, 1, 1, 1, '', 1, 1, 1, 1, 1, 1, 1, 1, nperson('mother')]],
        'sears': [[],
                  [2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3],
                  [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, nperson('mother')]],
        'pss': [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, nperson('mother')]],
        'srs': [[2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2],
                [3, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 3, 3, 3, 2, 3, 2, 3, 2, 2],
                [2, 2, 2, 3, 2, 1, 1, 2, 2, 2, 2],
                [1, 1, 2, 1, 2, 2, 2, 1, 2, 1, nperson('mother')]],
        'bsi': [[3, 2, 3, 2, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 2],
                [3, 2, 3, 2, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, nperson('mother')]],
        'mspss': [[3, 3, 4, 4, 4, 4],
                  [4, 4, 4, 4, 4, 4, nperson('mother')]],
        'les': [[1, 1, 1, 0],
                [2],
                [1, 1, 1, 1, 1, 1, '', 1],
                # [],
                [0, 1, 1, 1, 1, 1, 1, 1, 1],
                [2],
                [1, 1, 1, 1, 1, 1, 1, '', 1],
                # [],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [2],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                # [],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [3],
                [],
                [nperson('mother')]],
##        'brief2': [[],
##                   [2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
##                   [1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
##                   [1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
##                   [1, 1, 1, 2, 1, 1, 2, 2, 1, 1],
##                   [1, 1, 1, 1, 1, 2, 1, 2, 2, 2],
##                   [3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, nperson('mother')]],
        'ace': [[2, 2, 2, 1, 2],
                [2, 2, 2, 2, 2, nperson('mother')]]
##        'pcq': [[]]
    }

    open_page()
    enter_data(data)
##    skip_pcq()

if __name__ == '__main__':
    main()
