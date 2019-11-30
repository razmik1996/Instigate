#!/usr/bin/env python
"""@package for Employee class
you can create and modify employers 
with own methods
"""


class Employee:
    """
    abstract class
    Contains general information about employees
    """
    workingDays = 22                              #by default working days

    def __init__(self, name, salary, position):
        """
        Constructor of Employee class
        """
        self.name = name
        self.salary = salary
        self.position = position

    def setWorkingDays(self, workingDays):
        """
        Set how many days did the 
        employee work in the current month
        from 1 to 31
        usage: emp1.setWorkingDays(numberOfDays)
        """
        if (workingDays > 0 and workingDays < 32):
            self.workingDays = workingDays
            print "Working days for", self.name, "checked to", workingDays
        else:
            print "Invalid value"

    def setSalary(self, salary):
        """
        Set how much will the employee
        receive for a month (22 days)
        usage: emp1.setSalary(salary) 
        """
        if(salary > 0):
            self.salary = salary
            print "Salary for", self.name, "checked to", salary
        else:
            print "Invalid value"

    def setPosition(self, position):
        """
        Set position of employer
        usage: emp1.setPosition(position)
        """
        print ("Position for", self.name, "checked to", position)
        self.position = position

    def getName(self):
        """
        Get name of employer
        """
        return self.name

    def getPosition(self):
        """
        Get position of employer
        """
        return self.position

    def getSalary(self):
        """
        Get salary of employer
        """
        return self.Salary

    def getEarnings(self):
        """
        Get earnings of employer
        the method considers how
        much a worker earned per month
        usage: emp1.getEarnings()
        """
        earningForDay = self.salary / 22
        salary = self.workingDays * earningForDay
        earnings = salary - (salary * 0.3)
        return earnings

    def printEarnings(self):
        """
        Print earnings
        """
        print self.position, self.name, "Earnings for", self.workingDays, "Days is", self.getEarnings()

class Engineer(Employee):
    """
    Class engineer child class of Employee
    Contains information about engineers
    """
    def __init__(self, name, salary, position):
        """
        Default constructor
        usage: obj1 = Engineer(name, salary, position)
        """
        Employee.__init__(self, name, salary, position)

    def __str__(self):
        """
        for printing
        """
        return ("Engineer " + self.name + " in position " + self.position + " for this month earnings is " + str(self.getEarnings()))

class Executive(Employee):
    """
    Class executive child class of Employee
    Contains information about executive employers
    """
    def __init__(self, name, salary, position):
        """
        Default constructor
        usage: obj1 = Executive(name, salary, position)
        """
        Employee.__init__(self, name, salary, position)

    def __str__(self):
        """
        for printing
        """
        return ("Executive employee " + self.name + " in position " + self.position + " for this month earnings is " + str(self.getEarnings()))

class Contractor(Employee):
    """
    Class Contractor child class of Employee
    Contains information about contractors
    """
    def __init__(self, name, salary, position):
        """
        Default constructor
        usage: obj1 = Contractor(name, salary, position)
        """
        Employee.__init__(self, name, salary, position)

    def __str__(self):
        """
        for printing
        """
        return ("Contractor " + self.name + " in position " + self.position + " for this contract earnings is " + str(self.getEarnings()))

    def getEarnings(self):
        """
        getEarnings overridden for contractor
        """
        return (self.salary - (self.salary * 0.2))

    def printEarnings(self):
        """
        printEarnings overridden for contractor
        """
        print self.position, self.name, "Earnings for this contract is", self.getEarnings()
