#Terminal
build=1
#github.com/smcclennon/Toolbox
import os
os.system("title Terminal")
while True:
        cmd=input("Terminal>")
        os.system("title CMD Terminal ["+cmd+"]")
        os.system(""+cmd+"")
