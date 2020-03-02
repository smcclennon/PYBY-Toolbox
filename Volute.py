#Volute
#github.com/smcclennon/PYBY-Toolbox
ver='1.2.0'

THREADS_TO_CREATE = 4

#import
try:
    print('Importing required libraries...')
    import os
    from threading import Thread
    from ctypes import cast, POINTER
    os.system('title Volute v'+ver+' - Importing...')
except:
    print('\nError: unable to import one or more libraries\nVisit: github.com/smcclennon/PYBY-Toolbox for support\n\nPress enter to exit...')
    input()
    exit()

try:
    from comtypes import CLSCTX_ALL
except:
    print('\nError: unable to import "comtypes"')
    confirm=input(str('Attempt to install "comtypes"? [Y/n] ')).upper()
    if confirm!='N':
        try:
            os.system('pip install comtypes --user')
            os.system('cls')
            os.system('"'+str(os.path.basename(__file__))+'"')
            exit()
        except:
            print('Failed to install "pycaw"\nPress enter to exit...')
        input()
        exit()
try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except:
    print('\nError: unable to import "pycaw"')
    confirm=input(str('Attempt to install "pycaw"? [Y/n] ')).upper()
    if confirm!='N':
        try:
            os.system('pip install pycaw --user')
            os.system('cls')
            os.system('"'+str(os.path.basename(__file__))+'"')
            exit()
        except:
            print('Failed to install "pycaw"\nPress enter to exit...')
        input()
        exit()




devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

run = True

def unmuteThread():
    while run == True:
        volume.SetMute(0, None)

os.system('title Volute v'+ver)
print(f'Creating {THREADS_TO_CREATE} threads...')

for i in range(0, THREADS_TO_CREATE):
    Thread(target = unmuteThread).start()
    print('Created thread')

os.system('cls')
print(f'Unmuting your system with {THREADS_TO_CREATE} threads!\n\nPress ENTER to stop')
input()
print(f'Stopping {THREADS_TO_CREATE} threads...')
run = False