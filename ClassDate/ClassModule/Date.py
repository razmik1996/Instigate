#!/usr/bin/env python

class Date:
    __day = 1
    __year = 1990
    __month = 1
    __monthList = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, year, month):
        setYear(year)
        setMonth(month)
        setDay(day)
    

    def setDay(self, day):
        
    
    def setYear(self, year):
        if (year > 0 and year < 2020):
            self.__year = year
        else:
            self.__year = 1990

    def setMonth(self, month):
        if (month > 0 and month <= 12):
            self.__month = month
        else:
            self.__month = 1
        
    def getDay(self):
        return self.__day

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.__month

    def addDay(self, day):


    def addYear(self, year):


    def addMonth(self, month):


    def printDate(self):


    def diff(self, Date):
