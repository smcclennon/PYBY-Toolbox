#PIP
ver='1.0.0'
#github.com/smcclennon/Toolbox
import os
os.system('title PIP')
while True:
    print('Please enter a package name (e.g. "requests" or "psutil")')
    package = input('> ')
    print('\n>>> pip install '+package+' --user')
    os.system(f'pip install {package} --user')
    print('\n\n\n')
