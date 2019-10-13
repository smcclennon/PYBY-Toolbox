#PIP
ver=1
#github.com/smcclennon/Toolbox
import os
os.system('title PIP')
while True:
    print('Please enter a package name (e.g. "requests" or "psutil")')
    package=input(str('> '))
    print('\n>>> pip install '+package+' --user')
    os.system('pip install '+package+' --user')
    print('\n\n\n')
