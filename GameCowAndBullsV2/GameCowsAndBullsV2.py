#!/usr/bin/env python

from random import randint

import signal
import sys

#SIGINT signal handling function
def signal_handler(sig, frame):
        print('\nYou pressed Ctrl+C!')
        print("Bye!!!")
        sys.exit(0)

#Main function
def main():
    signal.signal(signal.SIGINT, signal_handler) #handling SIGINT
    print "Welcome to the Cows and Bulls Game!" #Welcome text
    randInteger = randint(1000, 9999); #rand four digit integer
    randList = integerToList(randInteger) #from integer to list
    global countCows
    global countBulls
    global listCowsAndBulls
    listCowsAndBulls = [0, 0, 0, 0]
    print "Write exit if you want exit"
    while(True):
        yourNumber = enterYourNumber() #take number from user
        if (check(yourNumber, randInteger)): #check value is answer or not
            return 0
        else:
            print "Your Number is: ", yourNumber
            howMuchCowsBulls(yourNumber, randList) #count Cows and Bulls
            print "Cows: ", countCows
            print "Bulls: ", countBulls

#function from integer to list
def integerToList(integer):
    listRand = []
    listRand.append(integer/1000);
    listRand.append((integer%1000)/100)
    listRand.append((integer%100)/10)
    listRand.append(integer%10)
    return listRand

#read input and after validation return it
def enterYourNumber():
    yourNumber = raw_input("Enter Your four digit number: ")
    if (yourNumber == "exit"):
	print "Good Bye!!!"
	exit()
    if (yourNumber.isdigit()):
	yourNumber = int(yourNumber)
	if (yourNumber < 1000 or yourNumber > 9999):
	    print("Invalid number please enter four digit number: ")
	    yourNumber = enterYourNumber()
    else:
	print "Invalid type of number please enter four digit number: "
	yourNumber = enterYourNumber()

    return yourNumber


#check answer is correct or not
def check(yourNumber, randInteger):
    if(yourNumber == randInteger):
        print "Your Number is: ", yourNumber
        print "Awesome random number is: ", randInteger
        return True
    else:
        return False

#how much Cows And Bulls
def howMuchCowsBulls(yourNumber, listRand):
    global countCows
    countCows = 0
    global countBulls
    countBulls = 0
    if((yourNumber/1000) == listRand[0]):        #checking every digit
        listCowsAndBulls[0] = 1	                 #are digits equal or not
    elif(listCowsAndBulls[0] == 1):              #when digits equal then for that digit we have one cow
        listCowsAndBulls[0] = 2                  #when digits aren't equal but before we guessed that digit we have one bull
    if(((yourNumber%1000)/100) == listRand[1]):
        listCowsAndBulls[1] = 1
    elif(listCowsAndBulls[1] == 1):
        listCowsAndBulls[1] = 2
    if(((yourNumber%100)/10) == listRand[2]):
        listCowsAndBulls[2] = 1
    elif(listCowsAndBulls[2] == 1):
        listCowsAndBulls[2] = 2
    if((yourNumber%10) == listRand[3]):
        listCowsAndBulls[3] = 1
    elif(listCowsAndBulls[3] == 1):
        listCowsAndBulls[3] = 2

    for n in listCowsAndBulls:
        if n == 1:
            countCows+=1
        elif n == 2:
            countBulls +=1

main()
