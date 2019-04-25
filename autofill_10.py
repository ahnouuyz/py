""" Reference (for person filling in):
    'mother': 1,
    'father': 2,
    'maternal grandmother': 3,
    'maternal grandfather': 4,
    'paternal grandfather': 5,
    'paternal grandfather': 6,
    'maid': 7,
    'childcare teacher': 8,
    'others': 9
"""

import os
import csv
import time
import pyautogui
import webbrowser

pyautogui.PAUSE = 0.02
pyautogui.FAILSAFE = True

def wait(ref_pos=(1, 94), ref_val=(195, 36, 50), delay=0.3, timeout=60):
    """ Wait until the red bar appears at the top-left corner.
        This may not work properly for pages that are too short.
    """
    start_time = time.time()
    elapsed_time = 0
    while pyautogui.screenshot().getpixel(ref_pos) != ref_val:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            raise TimeoutError(f'Timeout: {elapsed_time:.2f} s have passed.')
##    if elapsed_time < 0.1:
##        time.sleep(2)
    time.sleep(delay)

def open_incognito_tab():
    url = 'https://qau1.au1.qualtrics.com/jfe/form/SV_1UjsQDl2Rut8JZr'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)

def get_data(filepath):
    with open(filepath) as f:
        reader = csv.reader(f)
        pages = [[val.strip() for val in line] for line in reader if line]
    return pages

def next_page():
    pyautogui.click(100, 100)
    for _ in range(4):
        pyautogui.hotkey('shift', 'tab')
    pyautogui.press('enter')

def skip_pcq():
    for i in range(41):
        wait()
        pyautogui.click(100, 100)
        if i in [13, 20, 22, 24]:
            pyautogui.press(['\t', '\t', 'space', '\t', 'space'])
        elif i == 18:
            pyautogui.press(['\t', '\t', 'space'])
        elif i == 31:
            for _ in range(6):
                pyautogui.hotkey('shift', '\t')
            pyautogui.press('space')
        next_page()

def enter_response(response):
    try:
        response = int(response)
        if response == 0:
            pass
        elif response == 1:
            pyautogui.press('space')
        else:
            pyautogui.press('right', presses=response - 1)
    except ValueError:
        pyautogui.typewrite(response)

def fill_page(page):
    wait()
    pyautogui.click(100, 100)
    pyautogui.press('\t', presses=2)
    for val in page:
        if val == 'next_page':
            next_page()
            return
        enter_response(val)
        pyautogui.press('\t')

# ========================================================================

def main():
    current_id = '010-21795'
    folder = 'C:/Users/tp-laizy/Downloads/saq_box2'
    filepath = os.path.join(folder, current_id + '.txt')
    pages = get_data(filepath)
    
    open_incognito_tab()
    for page in pages:
        fill_page(page[1:])

    message = f'All done except for PCQ!\nGood luck!\nCurrently on ID: {current_id}'    
    pyautogui.alert(text=message)

if __name__ == '__main__':
    main()
