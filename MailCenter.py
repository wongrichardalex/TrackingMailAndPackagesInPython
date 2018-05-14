"""
Author: Richard Wong

File: MailCenter.py

Program Description:

import MailBox

import Boxholder

import Package
"""

import sys
import string

from Boxholder import *
from Mail import *
from Package import *
from Mailbox import *

class MailCenter:
    def __init__(self):
        self._employees = {}
        self._mailboxes = {}
        self._boxholders = {}

    def open(self):

        print("-----------------------------------------------------------------")
        print("                 Welcome!  Let's get started.")
        print("-----------------------------------------------------------------")

        print()
        print()

        print("                     What is your name? ")
        print()

        employee = input("                              ")
        print()
        print()
        
        print("                     Please enter a password:")
        print()
        password = input("                              ")
        self._employees[employee] = password
        print()

        print()
        print("-----------------------------------------------------------------")
        print("                         Hello " + employee + ".")
        print("-----------------------------------------------------------------")
        
        print("    Please enter how many mailboxes you would like to create: ")
        print()
        try:
            size = int(input("                              "))

        except:
            print("Please enter an integer.")
            self.open()
        
        print()
        print()

        self.createMailBoxes(size)
        
        print("-----------------------------------------------------------------")
        print("      Awesome! Now we have a mail center with " + str(size)+ " mailboxes!")
        print("-----------------------------------------------------------------")


        print()
        print()

        print("*****************************************************************")
        print("                     OUR STORE IS NOW OPEN!    ")
        print("*****************************************************************")

    
    def createMailBoxes(self, n):

        
        if n == 0:
            return
        else:

            
            box = Mailbox(n)
            self._mailboxes[n] = box
            self.createMailBoxes(n-1)
    
    def assign(self):

        print("-----------------------------------------------------------------")
        print("                    Assign Boxholder to a Mailbox ")
        print("-----------------------------------------------------------------")
        print()
        
        boxholder_name = input("            Please enter boxholder name: ")
        boxholder = Boxholder(boxholder_name)
        
        if boxholder_name in self._boxholders:
            print()
            print("             Guest already in system.")
            return
        
        print()
        
        boxnumber = int(input("            Please enter mailbox number: "))
        
        try:
            mailbox = self._mailboxes[boxnumber]
            
        except KeyError:
            print()
            print("            Mailbox not at center.")
            return
    
        if boxholder_name not in mailbox.boxholders():
            
            boxholder.assignMailbox(mailbox)
            self._boxholders[boxholder_name] = boxholder
            print()
            print()
            print("                    " + str(boxholder_name) + " has been added to Box " + str(boxnumber))
            print()

            
        else:
            print("           Please choose another mailbox.")
            self.assign()
            

    def updateContact(self):

        boxholder_name = input("                    Please enter boxholder name: ")
        print()
        print()
        
        try:
            boxholder = self._boxholders[boxholder_name]
            boxholder.updateContact()

        except KeyError:
            
            print()
            print("           Guest not in system.")
            return
        
    def addEmployee(self):
        print("-----------------------------------------------------------------")
        print("                          Add Employee")
        print("-----------------------------------------------------------------")
        print()
        print("                     Please enter employee to be added: ")
        print()
        employee = input("                              ")
        print()
        print()
        
        if employee not in self._employees:
            
            print("                     Please enter a password:")
            print()
            password = input("                              ")
            self._employees[employee] = password
            print()
            print("                     Employee has been added to system.")
            print()

        else:

            print("          Employee already in system.")
            print()
            
    

    def recieveMail(self):
        #setter, notify boxholder he/she has mail, fill mailbox temporarily
        print("-----------------------------------------------------------------")
        print("                         Recieve Mail")
        print("-----------------------------------------------------------------")
        print()
        print("          Please enter mail list file: ")
        print()

        mfilename = input("                            ")
        
        try:
            raw_mfile = open(mfilename)

            mail_list = raw_mfile.readlines()

            for line in mail_list:

                if line[0] == "#":
                    pass
                
                else:

                    mail_list = line.split()
                    
                    if len(mail_list) == 2:
                        
                        recipient = mail_list[0]
                        contents = mail_list[1]

                        mail = Mail(recipient, contents)
                        

                        if recipient in self._boxholders:

                            boxholder = self._boxholders[recipient]

                            box = boxholder.returnBox()

                            box.addMail(mail)
                            

                            print()
                            print("     A {} has been added to {}'s box, Box {:d}.".format(contents, recipient, boxholder.mailbox()))
                            print()
                            
        except FileNotFoundError:
            
            print()
            print("          ERROR: File not found.")
            print()
            prompt = input("          Press 1 to try again or any other key to exit.")
            
            if prompt == "1":
                self.recieveMail()
                
            else:
                
                return

                            
    def recievePackages(self):
        #setter, notify boxholder he/she has package(s)
        print("-----------------------------------------------------------------")
        print("                       Recieve Packages")
        print("-----------------------------------------------------------------")
        print()
        print("          Please enter package list file: ")
        print()

        pfilename = input("                            ")
        
        try:
            raw_pfile = open(pfilename)

            packages = raw_pfile.readlines()

            for line in packages:

                if line[0] == "#":
                    pass
                
                else:

                    package_list = line.split()
                    
                    if len(package_list) == 3:
                        
                        ID = package_list[0]
                        recipient = package_list[1]
                        contents = package_list[2]

                        package = Package(ID, recipient, contents)
                        

                        if recipient in self._boxholders:

                            boxholder = self._boxholders[recipient]

                            box = boxholder.returnBox()

                            box.addPackage(package)
                            

                            print()
                            print("     {}: {} has been added to {}'s box, Box {:d}.".format(ID, contents, recipient, boxholder.mailbox()))
                            print()

                
            
        except FileNotFoundError:
            
            print()
            print("          ERROR: File not found.")
            print()
            prompt = input("          Press 1 to try again or any other key to exit.")
            
            if prompt == "1":
                self.recievePackages()
                
            else:
                
                return

    def retrieveMail(self):
        boxholder_name = input("          Please enter boxholder name: ")
        print()
        print()
        
        try:
            boxholder = self._boxholders[boxholder_name]
            boxholder.retrieveMail()

        except KeyError:
            
            print()
            print("           Guest not in system.")
            return

    def retrievePackage(self):
        boxholder_name = input("          Please enter boxholder name: ")
        print()
        print()
        
        try:
            boxholder = self._boxholders[boxholder_name]
            boxholder.retrievePackage()

        except KeyError:
            
            print()
            print("           Guest not in system.")
            return


    def retrievePackages(self):
        boxholder_name = input("          Please enter boxholder name: ")
        print()
        print()
        
        try:
            boxholder = self._boxholders[boxholder_name]
            boxholder.retrievePackages()

        except KeyError:
            
            print()
            print("           Guest not in system.")
            return


    def pay(self):
        
        boxholder_name = input("          Please enter boxholder name: ")
        print()
        print()
        
        try:
            boxholder = self._boxholders[boxholder_name]
            boxholder.pay()

        except KeyError:
            
            print()
            print("           Guest not in system.")
            return
        

    def search(self):
        print("-----------------------------------------------------------------")
        print("                   Search for a Boxholder")
        print("-----------------------------------------------------------------")
        print()
        
        boxholder_name = input("          Please enter boxholder name: ")
        print()
        print()
        
        try:
            boxholder = self._boxholders[boxholder_name]
            
            print()
            print("           Boxholder Name: "+ boxholder.name())
            print()
            print("           Boxholder Mailbox: " + str(boxholder.mailbox()))
            print()
            print("           Boxholder Contact: ")
            print("               Phone: " + str(boxholder.phone()))
            print("               Email: " + str(boxholder.email()))
            print()
            print("           Boxholder Dues: $" + str(boxholder.dues()) + "/month")
            print()
            print("           Boxholder Amount Due: $" + str(boxholder.amountDue()))
            print()
            
            if boxholder.isLate():
                print("           WARNING: Boxholder is late on payment.")

            print()
            print()
        
        except KeyError:
            
            print()
            print("           Guest not in system.")
            return

        forward = input("           Press 1 to continue. ")
        
        if forward == 1:
            return
        

    def terminate(self):
        
        print("-----------------------------------------------------------------")
        print("                 Remove Boxholder from a Mailbox ")
        print("-----------------------------------------------------------------")
        print()
        
        boxholder_name = input("            Please enter boxholder name: ")

        try:
            
            boxholder = self._boxholders[boxholder_name]
        
        except KeyError:
            
            print()
            print("           Guest not in system.")
            return

        boxnumber = boxholder.mailbox()
        
        self._boxholders.pop(boxholder_name)
        boxholder.close()
        print()
        print("                    " + str(boxholder_name) + " has been removed from Box " + str(boxnumber))
        

    def run(self):

        print()
        print()

        print("-----------------------------------------------------------------")

        print("                          Please Press: ")
        print("             + ------------------------------------- +")
        print("             |   1 for Boxholder, 0 for Employee     |")
        print("             |                                       |")
        print("             |  Type a letter to close the program   |")
        print("             + ------------------------------------- +")
        print()
        
        key = input("                                ")
        try:
            key = int(key)

        except ValueError:

            print()
            print()
            print("-----------------------------------------------------------------")
            print("                     Please have a nice day!")
            print("-----------------------------------------------------------------")

            sys.exit(1)
            
        print()
        print()
        
        if key == 1:

            guest = self.guestLogin()
            
            self.runGuest(guest)

        elif key == 0:

            employee = self.employeeLogin()
            
            self.runEmployee(employee)

        else:
            print("                           Invalid entry!")

            
        self.run()

    def employeePrint(self, employee):
        print("-----------------------------------------------------------------")
        
        print("                         Welcome " + employee + ".")
        print("-----------------------------------------------------------------")
        print()
        print("           + ------------------------------------------- +")
        print("           | Press 1 to assign boxholder to a mailbox.   |")
        print("           | Press 2 to remove boxholder from a mailbox. |")
        print("           | Press 3 to recieve mail.                    |")
        print("           | Press 4 to recieve packages.                |")
        print("           | Press 5 to search for a boxholder.          |")
        print("           | Press 6 to update contact information.      |")
        print("           | Press 7 to help a boxholder make a payment. |")
        print("           | Press 8 to help a boxholder retrieve mail.  |")
        print("           | Press 9 to retrieve a boxholder's package.  |")
        print("           | Press 10 to retrieve a boxholder's packages.|")
        print("           | Press 11 to add an employee                 |")
        print("           | Press 12 to exit.                           |")
        print("           + ------------------------------------------- +")

        print()
        print()

        

    def guestPrint(self, guest):
        print("-----------------------------------------------------------------")
        
        print("                         Welcome " + guest.name() + ".")
        print("-----------------------------------------------------------------")
        print()
        print("          + ------------------------------------------- +")
        print("          | Press 1 to read messages.                   |")
        print("          | Press 2 to make a payment.                  |")
        print("          | Press 3 to retrieve mail.                   |")
        print("          | Press 4 to retrieve a specific package.     |")
        print("          | Press 5 to retrieve all packages.           |")
        print("          | Press 6 to update contact information.      |")
        print("          | Press 7 to exit.                           |")
        print("          + ------------------------------------------- +")
        print()
        print()

    def employeeLogin(self):
        print("          + ------------------------------------------- +")
        print("          |          Please enter employee name:        |")
        print("          + ------------------------------------------- +")
        print()
        
        employee = input("                                ")
        
        if employee in self._employees:
            print("          + ------------------------------------------- +")
            print("          |          Please enter password:             |")
            print("          + ------------------------------------------- +")
            password = input("                                ")
            
            if self._employees[employee] == password:
                
                return employee
            
            else:
                
                print("                     Incorrect password.        ")
                print()
                print("      Press 1 to try again, press any other key to exit.")
                print()
                
                if input("                                ") == "1":
                    
                    self.employeeLogin()
                    
                else:
                    
                    self.run()
        else:
            print("          + ------------------------------------------- +")
            print("          |             Employee not in system          |")
            print("          + ------------------------------------------- +")
            self.run()


    def guestLogin(self):
        print("          + ------------------------------------------- +")
        print("          |          Please enter guest name:           |")
        print("          + ------------------------------------------- +")
        print()
        
        guest = input("                                ")
        
        if guest in self._boxholders:
            return self._boxholders[guest]
        
        else:
            print("          + ------------------------------------------- +")
            print("          |             Guest not in system             |")
            print("          + ------------------------------------------- +")
            self.run()


    def runGuest(self, guest):


        print()
        print()

        self.guestPrint(guest)
        try:
            prompt = int(input("                    What would you like to do? "))

        except ValueError:
            print("          + ------------------------------------------- +")
            print("          |                Invalid entry.               |")
            print("          + ------------------------------------------- +")
            self.runGuest(guest)

        print()
        print()

        if prompt == 1:
            guest.readMessages()

        if prompt == 2:
            guest.pay()

        if prompt == 3:
            guest.retrieveMail()

        if prompt == 4:
            guest.retrievePackage()

        if prompt == 5:
            guest.retrievePackages()

        if prompt == 6:

            guest.updateContact()
            
        if prompt == 7:
            return

        if input("                  ") != None:
            
            self.runGuest(guest)


    def runEmployee(self, employee):

        self.employeePrint(employee)

        try:
            prompt = int(input("                    What would you like to do? "))

        except ValueError:
            print("          + ------------------------------------------- +")
            print("          |                Invalid entry.               |")
            print("          + ------------------------------------------- +")
            self.run()

        print()
        print()

        if prompt == 1:
            self.assign()

        if prompt == 2:
            self.terminate()

        if prompt == 3:
            self.recieveMail()

        if prompt == 4:
            self.recievePackages()

        if prompt == 5:
            self.search()

        if prompt == 6:
            self.updateContact()

        if prompt == 7:
            self.pay()

        if prompt == 8:
            self.retrieveMail()

        if prompt == 9:
            self.retrievePackage()

        if prompt == 10:
            self.retrievePackages()

        if prompt == 11:
            self.addEmployee()

        if prompt == 12:
            return

        if input("                  ") != None:
        
            self.runEmployee(employee)

        

def main():

    sys.setrecursionlimit(10000000)
    print()
    print()
    print()
    print()

    center = MailCenter()
    center.open()
    center.run()

main()                  
                    
