#Terminal
ver='1.0.0'
#github.com/smcclennon/Toolbox
import os
os.system("title Terminal")
while True:
        cmd=input("Terminal>")
        os.system(f"title CMD Terminal [{cmd}]")
        os.system(f"{cmd}")
