#!/usr/bin/env python

from random import randint

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
    signal.signal(signal.SIGINT, signal_handler)              #handling SIGINT
    print "Welcome to the Cows and Bulls Game!"               #Welcome text
    print "For more information read readme.txt file"
    randInteger = randint(1000, 9999);                        #rand four digit integer
    randList = integerToList(randInteger)                     #from integer to list
    print "Type exit if you want exit"
    while(True):
        yourNumber = enterYourNumber()                        #take number from user
        if (check(yourNumber, randInteger)):                  #check value is answer or not
            return 0
        else:
            print "Your Number is: ", yourNumber
            howMuchCowsBulls(yourNumber, randList)            #count Cows and Bulls

def integerToList(integer):
    """
    function from integer to list
    """
    listRand = []
    listRand.append(integer/1000);
    listRand.append((integer%1000)/100)
    listRand.append((integer%100)/10)
    listRand.append(integer%10)
    return listRand

def enterYourNumber():
    """
    read input and after validation return it
    """
    try:
        print"----------------------------------"
        yourNumber = raw_input("Enter Your four digit number: ")  #try block for catching ctr+d 
    except EOFError as error:
        print "\nYou pressed ctr+d"
        print "Bye"
        exit(1)
    if (yourNumber == "exit"):
        print "Good Bye!!!"                                       #when user want exit
        exit(0)
    if (yourNumber.isdigit()):                                    #when input is number
        yourNumber = int(yourNumber)
        if (yourNumber < 1000 or yourNumber > 9999):
            print("Invalid number please enter four digit number: ")
            yourNumber = enterYourNumber()
    else:
        print "Invalid type of number please enter four digit number: "
        yourNumber = enterYourNumber()
    
    return yourNumber


def check(yourNumber, randInteger):
    """
    check answer is correct or not
    """
    if(yourNumber == randInteger):
        print "Your Number is: ", yourNumber
        print "Awesome random number is: ", randInteger
        return True
    else:
        return False

def howMuchCowsBulls(yourNumber, listRand):
    """
    how much Cows And Bulls
    """
    countCows = 0                                   #Game Cows and Bulls
    countBulls = 0                                  #For every digit that the user guessed correctly
    customerList = integerToList(yourNumber)        #In the correct place, they have a "cow"
    for x in range(0, 4):                           #For every digit the user guessed correctly
        if customerList[x] == listRand[x]:          #In the wrong place is a "bull"
            countCows += 1
        elif customerList[x] in listRand:
            countBulls +=1
    print("Cows: " + str(countCows) + " Bulls: " + str(countBulls)) #print count of Cows and Bulls

main()
