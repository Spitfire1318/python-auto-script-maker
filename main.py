import os
import sys
import time
import colorama
from colorama import init, Fore, Back, Style

init()

myCoolTitle = 'Python Auto Script Maker'
from os import system
system("title " + myCoolTitle)

os.system('cls')

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.035)

print(Fore.CYAN + "Made by Spitfire1318")
print("")

file_name_with_ext = input(Fore.CYAN + "Enter your file name [including .py] ")
print("")

print_slow(Fore.BLUE + "File Options" + Fore.GREEN + " [1] Basic Modules " + Fore.YELLOW + "    [2] Selenium Setup" + Fore.MAGENTA + "    [3] Tkinter Basic "+Fore.RED + "  MySQL Database Sample [4]")
print("")
print("")
file_option = int(input(Fore.CYAN + "Select an option from the list above: "))

mydirectory = input("Enter your desired name of the output folder [created in the same directory] : ")
os.mkdir(mydirectory)
print("")
print(Fore.LIGHTGREEN_EX + '[!] Output Folder Created')
print("")
print(Fore.RED + "Writing to file in progress...")

if file_option == 1:
    with open(os.path.join(mydirectory, file_name_with_ext), 'w') as f:
        f.write("import os\n")
        f.write("import sys\n")
        f.write("import time\n")
        f.write("import webbrowser\n")
        f.write("import numpy\n")
        f.write("import random\n")
        print("")
        print(Fore.LIGHTGREEN_EX + "[!] Successfully written to file!")
        f.close()
        print("")
        
if file_option == 2:
    with open(os.path.join(mydirectory, file_name_with_ext), 'w') as f:
        f.write("from selenium import webdriver\n")
        f.write("from selenium.webdriver.common.by import By\n")
        f.write("from selenium.webdriver.common.keys import Keys\n")
        f.write("from selenium.common.exceptions import NoSuchElementException\n")
        f.write("from selenium.webdriver import ActionChains\n")
        f.write("import os\n")
        f.write("\n")
        f.write("driver = webdriver.Chrome('./chromedriver')\n")
        f.write("\n")
        f.write("url = ''\n")
        f.write("driver.get(url)\n")
        print("")
        print(Fore.LIGHTGREEN_EX + "[!] Successfully written to file!")
        f.close()
        print("")

if file_option == 3:
    with open(os.path.join(mydirectory, file_name_with_ext), 'w') as f:
        f.write("from tkinter import *\n")
        f.write("\n")
        f.write("window = Tk()")
        f.write("\n")
        f.write("window.title('My Application Title')\n")
        f.write("\n")
        f.write("window.mainloop()\n")
        print("")
        print(Fore.LIGHTGREEN_EX + "[!] Successfully written to file!")
        f.close()
        print("")

if file_option == 4:
    with open(os.path.join(mydirectory, file_name_with_ext), 'w') as f:
        f.write("import mysql.connector\n")
        f.write("\n")
        f.write("mydb = mysql.connector.connect(\n")
        f.write('   host="localhost",\n')
        f.write('   user="yourusername",\n')
        f.write('   password="yourpassword"\n')
        f.write("window.mainloop()\n")
        f.write(")\n")
        f.write("\n")
        f.write("mycursor = mydb.cursor()\n")
        f.write('mycursor.execute("CREATE DATABASE mydatabase")\n')
        print("")
        print(Fore.LIGHTGREEN_EX + "[!] Successfully written to file!")
        f.close()
        print("")