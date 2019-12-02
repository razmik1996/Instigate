#!/usr/bin/env python
"""@Package Date
Use it for making date variables
Add day, month or year to current date
Or take different between 2 dates
"""


class Date:
    """
    Class Date by default day = 1, year = 1990 and month = 1
    """
    __day = 1
    __year = 1990
    __month = 1
    __monthList = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        """
        Constructor for Date class set year, month and day
        using: obj1 = Date.Date(day, month, year)
        """
        self.setYear(year)
        self.setMonth(month)
        self.setDay(day)
    
    def __str__(self):
        """
        Function for casting to string 
        and printing by print python method
        using: print (obj1)
        output: d/m/y
        """
        return str(self.__day) + "/" + str(self.__month) + "/" + str(self.__year)

    def setDay(self, day):
        """
        Set day function give day from user and 
        after validation assign it to self.day
        using: obj1.setDay(day)
        """
        if (day > 0 and day < 32):
            if (day == 31):
                if (self.__month in [1, 3, 5, 7, 8, 10, 12]):
                    self.__day = day
                else:
                    print "Invalid day for that month"
                    print "day = 1"
                    self.__day = 1
            elif (day == 29 and self.__month == 2):
                if ((self.__year%4 == 0 and self.__year%100 != 0) or (self.__year%400 == 0)):
                    self.__day = day
                else:
                    print "Invalid day for that month"
                    print "day = 1"
                    self.__day = 1
            elif (day == 30 and self.__month == 2):
                    print "Invalid day for that month"
                    print "day = 1"
                    self.__day = 1
            else:
                self.__day = day
        else:
            print "Invalid day"
            print "day = 1"
            self.__day = 1


    
    def setYear(self, year):
        """
        Set year after validation
        using: obj1.setYear(year)
        """
        if (year > 0 and year < 2020):
            self.__year = year
        else:
            print "Invalid year"
            print "year = 1990"
            self.__year = 1990

    def setMonth(self, month):
        """
        Set month after validation
        using: obj1.setMonth(month)
        """
        if (month > 0 and month <= 12):
            self.__month = month
        else:
            print "Invalid month"
            print "month = 1"
            self.__month = 1
        
    def getDay(self):
        """
        Just get day from object
        using: obj1.getDay()
        """
        return self.__day

    def getYear(self):
        """
        Get year from object
        using: obj1.getYear()
        """
        return self.__year

    def getMonth(self):
        """
        Get month from object
        using: obj1.getMonth()
        """
        return self.__month

    def addDay(self, day):
        """
        Add some amount days
        using: obj1.addDay(day)
        """
        if(day > 0):
            self.__day += day
            while(self.__day > self.__monthList[self.__month]):
                if((self.__month == 2) and ((self.__year%4 == 0 and self.__year%100 != 0) or (self.__year%400 == 0))):
                    self.__day -= 29
                else:
                    self.__day -= self.__monthList[self.__month]
                    addMonth(1)

    def addYear(self, year):
        """
        Add some amount years
        using: obj1.addYear(year)
        """
        if(year > 0):
            self.__year += year
            if (self.__month == 2 and self.__day == 29):
                if not(((self.__year%4 == 0 and self.__year%100 != 0) or (self.__year%400 == 0))) :
                    self.__month += 1
                    self.__day = 1
                
        else:
            print "invalid quantity of years"

    def addMonth(self, month):
        """
        Add some amount months
        using: obj1.addMonth(month)
        """
        if(month > 0):
            self.__month += month
            while(self.__month > 12):
                self.__month -= 12
                self.__year += 1
            if (self.__month == 2 and self.__day == 29):
                if not(((self.__year%4 == 0 and self.__year%100 != 0) or (self.__year%400 == 0))):
                    self.__month += 1
                    self.__day = 1
        else:
            print "invalid quantity of months"

    def diff(self, Date):
        """
        Count different between two dates
        using: obj1.diff(obj2)
        """
        diffYear = 0
        diffDay = 0
        diffMonth = 0
        year = Date.getYear()
        day = Date.getDay()
        month = Date.getMonth()
        if(self.__year > year):
            diffYear = self.__year - year
            diffMonth = self.__month - month
            if(diffMonth < 0):
                diffMonth += 12
                diffYear -= 1
            diffDay = self.__day - day
            if(diffDay < 0):
                diffDay += self.__monthList[diffMonth - 1]
                diffMonth -= 1
                if(diffMonth <= 0):
                    diffMonth += 12
                    diffYear -= 1
        elif(self.__year < year):
            diffYear = year - self.__year
            diffMonth = month - self.__month
            if(diffMonth < 0):
                diffMonth += 12
                diffYear -= 1
            diffDay = day - self.__day
            if(diffDay < 0):
                diffDay += self.__monthList[diffMonth - 1]
                diffMonth -= 1
                if(diffMonth == 0):
                    diffMonth += 12
                    diffYear -= 1
        else:
            if(self.__month > month):
                diffMonth = self.__month - month
                diffDay = self.__day - day
                if(diffDay < 0):
                    diffDay += self.__monthList[diffMonth - 1]
                    diffMonth -= 1
            elif(self.__month < month):
                diffMonth = month - self.__month
                diffDay = day - self.__day
                if(diffDay < 0):
                    diffDay += self.__monthList[diffMonth - 1] - 1
                    diffMonth -= 1
            else:
                if(self.__day > day):
                    diffDay = self.__day - day
                elif(self.__day < day):
                    diffDay = day - self.__day
                else:
                    print "Same day"
                    print "first Date == second Date"
                    return
        print "Different is: ", diffYear, "Year ", diffMonth, "Month ", diffDay, "Day"
        return (diffYear, diffMonth, diffDay)
