#Task Killer
ver='1.0.0'
#github.com/smcclennon/Toolbox
import os
while True:
        os.system("title Task Killer [Scanning]")
        os.system("color c")
        os.system("cls")
        os.system("tasklist")
        os.system("color e")
        os.system("title Task Killer")
        print("\nPlease enter the task that you would like to kill")
        print("Example: 'notepad.exe'")
        print("To refresh the tasklist, type '.refresh'")
        while True:
                print("===")
                term=input("> ")
                if term==".refresh":
                        break
                os.system("taskkill /f /im "+term+" /t")
                print("")
                print("To refresh the tasklist, type '.refresh'")
                
