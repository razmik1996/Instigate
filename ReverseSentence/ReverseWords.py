#!/usr/bin/env python

import sys
import signal

def main():
    """
    Main function
    """
    print "for information please read readme file"
    signal.signal(signal.SIGINT, signal_handler) #handling SIGINT
    wordList = listWithWords()
    wordList = reverseList(wordList)
    wordList = fromListToString(wordList)
    print wordList                              #Print String

def signal_handler(sig, frame):
    """
    SIGINT handling function
    """
    print('\nYou pressed Ctrl+C!')
    print("Bye!!!")
    sys.exit(0)

def listWithWords():
    """
    Get string and return spitted string by list
    """
    try:
        print"----------------------------------"
        string = raw_input("Enter your string: " )             #try block for catching ctr+d 
    except EOFError as error:
        print "\nYou pressed ctr+d"
        print "Bye"
        exit(1)
    lst = string.split(" ")
    return lst

def reverseList(listForReverse):
    """
    Get list and reverse it
    """
    listForReverse = listForReverse[::-1] 
    return listForReverse

def fromListToString(listForToString):
    """
    Get list and return string
    """
    string = " ".join(listForToString)
    return string

main()
