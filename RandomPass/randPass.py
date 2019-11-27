#!/usr/bin/env python

import random
import string
import signal
import sys
import pyperclip                                                         #for copy to clipboard

def signal_handler(sig, frame):
    """
    SIGINT signal handling function
    """
    print('\nYou pressed Ctrl+C!')
    print("Bye!!!")
    sys.exit(0)

def main():
    """
    Main function
    """
    signal.signal(signal.SIGINT, signal_handler)                         #handling SIGINT
    print "For more information please read readme file"
    print "Type exit if you want exit"
    upper = string.ascii_uppercase                                       #string with uppercase
    lower = string.ascii_lowercase                                       #string with lowercase
    digits = string.digits                                               #string with digits
    symbol = string.punctuation                                          #string with symbols
    while True:
        password = ""
        print "--------------------------------"
        print "How strong password do you want?"
        try: 
            passwordLvl = raw_input("e for easy, m for middle, h for hard: ")#try block for catching ctr+d
        except EOFError as error:
            print "\nYou pressed ctr+d"
            print "Bye"
            exit(1)
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

def easyPassword(digits, lower):
    """
    this function generate easy password using
    lower case letters and digits
    """
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

def midlePassword(digits, lower, upper):
    """
    this function generate middle password 
    using digits lower and upper case letters
    """
    pwd = ""
    lenght = 0
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
                while(lenght != count):
                    if(lenght % 3 == 0):
                        lenght += 1
                        pwd += random.choice(digits)
                    elif(lenght % 3 == 1):
                        lenght += 1
                        pwd += random.choice(lower)
                    elif(lenght % 3 == 2):
                        lenght += 1
                        pwd += random.choice(upper)
                pwd = ''.join(random.sample(pwd, count))
                pyperclip.copy(pwd)
                break
        else:
            print "Invalid type of number please enter number between 6 to 40: "
            continue
    return pwd

def hardPassword(digits, lower, upper, symbol):
    """
    this function generate hard password using digits,
    lower and upper case letters, symbols
    """
    pwd = ""
    lenght = 0
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
                while(lenght != count):
                    if(lenght % 4 == 0):
                        lenght += 1
                        pwd += random.choice(digits)
                    elif(lenght % 4 == 1):
                        lenght += 1
                        pwd += random.choice(lower)
                    elif(lenght % 4 == 2):
                        lenght += 1
                        pwd += random.choice(upper)
                    elif(lenght % 4 == 3):
                        lenght += 1
                        pwd += random.choice(symbol)
                pwd = ''.join(random.sample(pwd, count))
                pyperclip.copy(pwd)
                break
        else:
            print "Invalid type of number please enter number between 8 to 50: "
            continue
    return pwd

main()
