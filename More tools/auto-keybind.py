# Auto key press by Shiraz

# key: 'win, d'
key = 'f5'
initial_delay = 5
key_delay = 1.2

# buffer_range: Once every X key-press repeats, wait for buffer_delay
# buffer_delay: The same as key_delay, except it only happens once every time the buffer_range is met
# Use this to give your self a chance to cancel the operation when having a fast key_delay
# Set buffer_delay to 0 to ignore this setting
buffer_range = 0
buffer_delay = 0











# code

import os, time

try:
    import pyautogui
except:
    module='pyautogui'
    print(f'\nError: unable to import "{module}"')
    confirm=input(f'Attempt to install "{module}"? [Y/n] ').upper()
    if confirm != 'N':
        try:
            os.system(f'pip install {module} --user')
            os.system('cls')
            del module
            os.system(f'"{str(os.path.basename(__file__))}"')
            exit()
        except:
            exit()
    exit()



print("Import complete!")
print(f"Key: {key}\nInitial delay: {5} seconds\n Key delay: {key_delay}")
if buffer_delay < 0:
    print(f"\nBuffer range: {buffer_range}\nBuffer delay: {buffer_delay}")
print('\n\n\n*** Please note, to cancel the operation at any time, hover your mouse into the top right corner of your screen ***')
print(f'\n\n\nInitial Delay: {initial_delay}')
time.sleep(initial_delay)
print('\n\n')
total=0
buffer=0
while True:
    buffer=buffer+1
    if buffer >= buffer_range:
        print(f'\n[Buffer range met: {buffer_range}]')
        print(f'Buffer Delay: {buffer_delay}')
        time.sleep(buffer_delay)
        buffer=0
    pyautogui.hotkey(key)
    total=total+1
    print(f'\nKey press [#{total}]: {key} ')
    print(f'Delay: {key_delay}')
    time.sleep(key_delay)
