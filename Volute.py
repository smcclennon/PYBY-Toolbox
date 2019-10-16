#Volute
#github.com/smcclennon
ver='1'

#import
try:
    print('Importing required libraries...')
    import os,urllib.request,json
    from ctypes import cast, POINTER; from comtypes import CLSCTX_ALL 
    os.system('title Volute v'+ver+' - Importing...')
except:
    print('\nError: unable to import one or more libraries\nVisit: github.com/smcclennon/PYBY-Toolbox for support\n\nPress enter to exit...')
    input()
    exit()
try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except:
    print('\nError: unable to import "pycaw"')
    confirm=input(str('Attempt to install "pycaw"? [Y/n] ')).upper()
    if confirm=='Y':
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
os.system('title Volute v'+ver)
os.system('cls')
print('Unmuting your system!\nTo stop, close this script.')
while True:
   volume.SetMute(0, None)

