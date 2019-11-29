#!/usr/bin/env python
from ClassModule import Date
import re
import sys
import signal

def signal_handler(sig, frame):
    """
    SIGINT signal handling fuction
    """
    print('\nYou pressed Ctrl+C!')
    print("Bye!!!")
    sys.exit(0)

def main():
    """
    Main function for count different
    between two days program
    """
    print "Type exit if you want exit"
    while True:
        print "----------------------------------------"
        while True:
            date1 = raw_input("Input first Day (%d, %m, %y): ")
            if (date1 == "exit"):
                print ("Bye!!!")
                exit(0)
            listDate1 = map(int, re.findall(r"\d+", date1))
            if(len(listDate1) == 3):
                p1 = Date.Date(listDate1[0], listDate1[1], listDate1[2])
                break
            else:
                print ("Invalid input retry")
                continue
        while True:
            date2 = raw_input("Input second Day (%d, %m, %y): ")
            if (date2 == "exit"):
                print ("Bye!!!")
                exit(0)
            listDate2 = map(int, re.findall(r"\d+", date2))
            if(len(listDate2) == 3):
                p2 = Date.Date(listDate2[0], listDate2[1], listDate2[2])
                break
            else:
                print ("Invalid input retry")
                continue
        p1.diff(p2)

if __name__ == "__main__":
    """
    Main call
    """
    signal.signal(signal.SIGINT, signal_handler)              #handling SIGINT
    try:
        main()
    except EOFError as error:
        print "\nYou pressed ctr+d"
        print "Bye!!!"
        exit(1)

