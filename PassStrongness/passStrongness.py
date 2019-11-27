#!/usr/bin/env python

import re
import signal
import sys

#SIGINT signal handling function
def signal_handler(sig, frame):
        print('\nYou pressed Ctrl+C!')
        print("Bye!!!")
        sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler) #handling SIGINT
    print "Type exit if you want exit"
    while True:
        print"______________________________"
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

#read password from user
def readPassword():
    while True:
        password = raw_input("Enter your password for checking (length between 4 to 50): ")
        if (password == "exit"):
    	    print "Good Bye!!!"
    	    exit()
        elif (len(password) < 4 or len(password) > 50):
    	    print("Invalid length of password please retry ")
    	    continue
        else:
            return password

#check Strongest of password
def passwordCheck(password):
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
