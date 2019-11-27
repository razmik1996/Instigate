#!/usr/bin/env python

import random
import string
import signal
import sys
import pyperclip                                                         #for copy to clipboard

#SIGINT signal handling function
def signal_handler(sig, frame):
        print('\nYou pressed Ctrl+C!')
        print("Bye!!!")
        sys.exit(0)

def main(): 
    signal.signal(signal.SIGINT, signal_handler)                         #handling SIGINT
    print "Type exit if you want exit"
    upper = string.ascii_uppercase                                       #string with uppercase
    lower = string.ascii_lowercase                                       #string with lowercase
    digits = string.digits                                               #string with digits
    symbol = string.punctuation                                          #string with symbols
    while True:
        password = ""
        print "--------------------------------"
        print "How strong password do you want?"
        passwordLvl = raw_input("e for easy, m for middle, h for hard: ")
        if(passwordLvl == "exit"):
            print "Bye!!!"
            exit(0)
        elif(passwordLvl == "e" or passwordLvl == "E"):
            password = easyPassword(digits, lower)                       #call function for easy password
        elif(passwordLvl == "m" or passwordLvl == "M"):
            password = midlePassword(digits, lower, upper)               #call function for middle password
        elif(passwordLvl == "h" or passwordLvl == "H"):
            password = hardPassword(digits, lower, upper, symbol)        #call function for hard password
        else:
            print "Invalid strongest"
            continue
        print "Your password is: ", password
        print ("Password copied to clipboard!!!")

#this function generate easy password using lower case letters and digits
def easyPassword(digits, lower):
    pwd = ""
    string = digits + lower
    while True:
        count = raw_input("How many characters do you want?(4 to 30): ")
        if (count == "exit"):
            print "Good Bye!!!"
            exit()
        if (count.isdigit()):
            count = int(count)
            if (count < 4 or count > 30):
                print("Invalid number please enter number between 4 to 30: ")
                continue
            else:
                pwd = ''.join(random.choice(string) for _ in range(count))
                pyperclip.copy(pwd)
                break
        else:
            print "Invalid type of number please enter number between 4 to 30: "
            continue
    return pwd

#this function generate middle password using digits lower and upper case letters
def midlePassword(digits, lower, upper):
    pwd = ""
    string = digits + lower + upper
    while True:
        count = raw_input("How many characters do you want?(6 to 40): ")
        if (count == "exit"):
            print "Good Bye!!!"
            exit()
        if (count.isdigit()):
            count = int(count)
            if (count < 6 or count > 40):
                print("Invalid number please enter number between 6 to 40: ")
                continue
            else:
                pwd = ''.join(random.choice(string) for _ in range(count-3))
                #at least one lower and upper case letter, digit
                pwd += random.choice(digits) + random.choice(lower) + random.choice(upper)
                #shuffle
                pwd = ''.join(random.sample(pwd, count))
                pyperclip.copy(pwd)
                break
        else:
            print "Invalid type of number please enter number between 6 to 40: "
            continue
    return pwd

#this function generate hard password using digits, lower and upper case letters, symbols
def hardPassword(digits, lower, upper, symbol):
    pwd = ""
    string = digits + lower + upper + symbol
    print string
    while True:
        count = raw_input("How many characters do you want?(8 to 50): ")
        if (count == "exit"):
            print "Good Bye!!!"
            exit()
        if (count.isdigit()):
            count = int(count)
            if (count < 8 or count > 50):
                print("Invalid number please enter number between 8 to 50: ")
                continue
            else:
                pwd = ''.join(random.choice(string) for _ in range(count))
                #at least one lower and upper case letter, digit, symbol
                pwd += random.choice(digits) + random.choice(lower) + random.choice(upper) + random.choice(symbol) 
                #shuffle
                pwd = ''.join(random.sample(pwd, count))
                pyperclip.copy(pwd)
                break
        else:
            print "Invalid type of number please enter number between 8 to 50: "
            continue
    return pwd

main()
