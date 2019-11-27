#!/usr/bin/env python

import re
import signal
import sys

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
    signal.signal(signal.SIGINT, signal_handler)                                    #handling SIGINT
    print "Please read readme file for more information"
    print "Type exit if you want exit"
    while True:
        password = readPassword()
        passStrongest = passwordCheck(password)                                     #Strongest value
        print "Strongest value is: ", passStrongest
        if (passStrongest < 20):                                                    #when value less than 20 print weak
            print "password is weak"
        elif (passStrongest >= 20 and passStrongest < 38):                          #when value less than 37 and up to 20 print medium
            print "password is medium"
        elif (passStrongest >= 38):                                                 #when value is up to 38 print strong
            print "password is strong"
        else:
            print "it's impossible)) who are you?"

def readPassword():
    """
    read password from user
    """
    while True:
        try:
            print"------------------------------------------------------------------------"
            password = raw_input("Enter your password for checking (length between 4 to 50): ") #try block for catching ctr+d 
        except EOFError as error:
            print "\nYou pressed ctr+d"
            print "Bye"
            exit(1)
        if (password == "exit"):
            print "Good Bye!!!"
            exit()
        elif (len(password) < 4 or len(password) > 50):
            print("Invalid length of password please retry ")
            continue
        else:
            return password

def passwordCheck(password):
    """
    check Strongest of password
    """
    passStrongest = 0
    passStrongest += len(password)
    if(re.search(r'\d', password)):
        passStrongest += 5
    if(re.search(r'[A-Z]', password)):
        passStrongest += 10
    if(re.search(r'[a-z]', password)):
        passStrongest += 5
    if(re.search(r'\W', password)):
        passStrongest += 10
    return passStrongest

main()
