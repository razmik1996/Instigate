#!/usr/bin/env python

from EmployeePack import Employee

"""______________________________________________________TEST________________________________________________"""
def main():
    en = Employee.Engineer("Jake", 96000, "Web developer")          #created object of engineer named en
    en.printEarnings()                                              #print earnings for en
    en.setWorkingDays(28)                                           #set working days to 28 for en
    print (en)                                                      #print by function print
    ex = Employee.Executive("Karen", 200000, "SEO Specialist")      #created object of executive named ex
    ex.printEarnings()                                              #print earnings for ex
    ex.setSalary(600000)                                            #set salary to 600000
    print (ex)                                                      #print by function print
    ct = Employee.Contractor("Natalie", 36000, "Python Developer")  #created object of Contractor named ct
    ct.printEarnings()                                              #print earnings for ct
    ct.setSalary(45000)                                             #set salary to 45000
    print (ct)                                                      #print by function print

if __name__ == "__main__":
    main()
