#the start
# !/usr/bin/env python3
import os
from colorama import init, Fore
import shutil
import subprocess
import urllib.request
import time
import platform
import pathlib
from pystyle import *
init()
####################################################

while True:
    v7x = input("Do you love various 7x (y/n): ")
    if v7x.lower() == 'y':
        print(Fore.LIGHTMAGENTA_EX + "Loading......")
        time.sleep(4)
        break

    elif v7x.lower() == 'n':
        print(Fore.YELLOW + "Exiting...")
        time.sleep(2)
        exit()
    else:
        print(Fore.RED + "Invalid input! Please enter 'y' or 'n'.")

if platform.system() == "Windows":
    os.system("cls")
    print("Please run tool in administrator mood because do not there a proplem")
else:
    os.system("clear")

os.system('clear')
v7x ='''



               ,--.                             ,-----.             
,--.  ,--,--,--`--,--.--.,---.,--.,--.,---.     '--,  ,--.  ,--.    
 \  `'  ' ,-.  ,--|  .--| .-. |  ||  (  .-'      .'  / \  `'  /     
  \    /\ '-'  |  |  |  ' '-' '  ''  .-'  `)    /   /  /  /.  \     
   `--'  `--`--`--`--'   `---' `----'`----'     `--'  '--'  '--'    




'''


Write.Print(v7x,Colors.red,interval=0.01)


print(Fore.GREEN + "This tool was created by FARES MOHAMED")

print(Fore.YELLOW + '-' * 40)

print(f"{Fore.GREEN}Welcome to the APKTool installation script!")

print(Fore.YELLOW + '-' * 40)
#########################################################################
if platform.system() == "Windows":
    print("Please run tool in administrator mood because do not there a proplem")
while True:
    if platform.system() == "Windows":
        java = input("do you have java in your pc? y/n: ")
        if java == 'y':
            print("wait .....")
            break
        elif java == 'n':
            print("waiting for installation.......")
            download_java = 'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=248737_8c876547113c4e4aab3c868e9e0ec572'
            desktop_path = pathlib.Path.home() / 'Desktop'
            path_java = desktop_path / 'java_installer.exe'
            urllib.request.urlretrieve(download_java, str(path_java))
            break
        else:
            print(Fore.RED + "Invalid input! Please enter 'y' or 'n'.")
    else:
        print("----------------------------------------")
        break
####################################################################
print("Please select an option:")

print(Fore.CYAN + "1. Install APKTool in Linux")

print(Fore.CYAN + "2. Install APKTool in Windows")

print(Fore.CYAN + "3. Install APKTool in Mac")

print(Fore.CYAN + "4. install apktool in Termux")

print(Fore.LIGHTBLACK_EX + "0. Exit")


while True:
    inputs = input("Enter your choice: ")

    if inputs == "1":
        print(Fore.BLUE + "Installing APKTool in Linux, wait.....")
        apktooljar = 'https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.8.1.jar'
        path = '/usr/local/bin/apktool.jar'
        urllib.request.urlretrieve(apktooljar, path)
        os.chmod(path, 0o755)
        apktool = "https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool"
        path = '/usr/local/bin/apktool'
        urllib.request.urlretrieve(apktool, path)
        os.chmod(path, 0o755)
        os.system('apt-get install zipalign')
        print(Fore.GREEN + "APKTool and Zipalign has been installed successfully in Linux!")
        break



    elif inputs == "2":
        print(Fore.BLUE + "Installing APKTool in Windows, wait.....")
        apktool_url = 'https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/windows/apktool.bat'

        apktool_path = r'C:\Windows\apktool.bat'

        apktool2_url = 'https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.8.1.jar'

        apktool2_path = r'C:\Windows\apktool.jar'

        urllib.request.urlretrieve(apktool_url, apktool_path)

        urllib.request.urlretrieve(apktool2_url, apktool2_path)

        print(Fore.GREEN + "APKTool has been installed successfully in Windows!")

        break

    elif inputs == "3":

        print(Fore.BLUE + "Installing APKTool on Mac, please wait...")

        apm_url1 = 'https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/osx/apktool'

        apm_path1 = '/usr/local/bin/apktool'

        apm_url2 = 'https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.8.1.jar'

        apm_path2 = '/usr/local/bin/apktool.jar'

        os.system('sudo curl -L ' + apm_url1 + ' -o ' + apm_path1)

        os.system('sudo chmod +x ' + apm_path1)

        os.system('sudo curl ' + apm_url2 + ' -o ' + apm_path2)

        print(Fore.GREEN + "APKTool has been successfully installed on Mac!")

        break
    elif inputs == "4":
        print(Fore.BLUE + "Installing APKTool in Termux, please wait.....")
        os.system('pkg update && pkg upgrade -y')
        os.system('pkg install -y wget')
        os.system('pkg install openjdk-17')
        try:
            subprocess.check_output(['wget', 'https://github.com/iBotPeaches/Apktool/releases/download/v2.8.1/apktool_2.8.1.jar', '-O', '$PREFIX/bin/apktool.jar'])
            subprocess.check_output(['wget', 'https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool', '-O', '$PREFIX/bin/apktool'])
            subprocess.check_output(['chmod', '+x', '$PREFIX/bin/apktool'])
            print(Fore.GREEN + "APKTool has been installed successfully in Termux!")
        except subprocess.CalledProcessError:
            print(Fore.RED + "Failed to install APKTool in Termux!")
            break
    elif inputs == "0":
        print(Fore.YELLOW + "Exiting...")
        time.sleep(2)
        exit()
    else:
        print(Fore.RED + "Invalid choice! Please choose a valid option.")
