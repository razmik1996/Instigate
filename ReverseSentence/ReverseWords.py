#!/usr/bin/env python

import sys
import signal

def main(): 
    signal.signal(signal.SIGINT, signal_handler) #handling SIGINT
    wordList = listWithWords()
    wordList = reverseList(wordList)
    wordList = fromListToString(wordList)
    print wordList                              #Print String

#SIGINT handling function
def signal_handler(sig, frame):
        print('\nYou pressed Ctrl+C!')
        print("Bye!!!")
        sys.exit(0)

#get string and return spitted string by list
def listWithWords():
    string = raw_input("Enter your string: ")
    lst = string.split(" ")
    return lst

#Get list and reverse it
def reverseList(listForReverse):
    listForReverse = listForReverse[::-1] 
    return listForReverse

#get list and return string
def fromListToString(listForToString):
    string = " ".join(listForToString)
    return string

main()
