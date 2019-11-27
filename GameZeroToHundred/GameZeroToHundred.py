#!/usr/bin/env python
from random import randrange
import sys, signal
randNumber = randrange(101)                              #take integer from 0 to 100

#SIGINT handling function
def signal_handler(sig, frame):
        print('\nYou pressed Ctrl+C!')
        print("Bye!!!")
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)             #handling SIGINT

counter = 1                                              #counter of attempts
print "type exit if you want exit"
while(1==1):                                             #infinite loop
    number = raw_input("Enter a number from 0 to 100: ") #get input from user
    if (number == "exit"):                               #when user type exit game exit with code 0
        print "Bye!!!"
        exit(0)
    elif (number.isdigit()):                             #check input is number or not
        number = int(number)                             #logic when it's number
        if (number < 0 or number > 100):
            print "Invalid value please enter number in range 0 to 100"
        elif (number == randNumber):
            print "You are right"
            print "Attempts: ", counter
            break
        elif (number < randNumber):
            print "More"
            counter += 1
        else: 
            print "Less"
            counter += 1
    else:                                                #logic when it's string
        print "invalid value please enter number in range 0 to 100"
