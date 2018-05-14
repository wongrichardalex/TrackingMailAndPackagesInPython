"""
Author: Richard Wong

File: Boxholder.py

Program Description:
Describes a Boxholder object.
"""

import queue

from Package import *
from Mailbox import *
from Queue import *

class Boxholder:
    
    def __init__(self, name):
        
        self._name = name
        self._phone = None
        self._email = None
        
        self._mailbox = None
        self._messages = Queue()


        self._dues = 0
        self._amountDue = 0
        self._late = False
        
        
        self._hasMail = False
        self._hasPackage = False


        self.late_message = "You have an overdue payment. "
        self.mail_message = "You've got mail!"
        self.package_message = "You have a package/packages."
        

    def name(self):
        return self._name

    def mailbox(self):
        return self._mailbox.number()

    def returnBox(self):
        return self._mailbox

    def phone(self):
        return self._phone

    def email(self):
        return self._email

    def dues(self):
        return self._dues

    def amountDue(self):
        return self._amountDue

    

    def assignMailbox(self, mailbox_object):
        
        self._mailbox = mailbox_object
        self._mailbox.addBoxholder(self)
        self._dues += 20
        

    def updateContact(self):
        print("-----------------------------------------------------------------")
        print("                   Update Contact Information ")
        print("-----------------------------------------------------------------")
        print()
        print()
        choice = input("            Press 1 for phone, 2 for email, 3 to exit: ")
        print()
        
        if choice == "1":
            self._phone = input("                    Please enter phone number: ")
            print()
            print("                    Phone number updated successfully.")
            print()
            print()
            
        elif choice == "2":
            self._email = input("                    Please enter email: ")
            print()
            print("                    Email updated successfully.")
            print()
            print()
            
        elif choice == "3":
            return
        
        else:
            print("                    Invalid entry.")

        self.updateContact()


    def overdue(self):
        self._late = True
        self._amountDue += 5
        self._messages.enqueue(self.late_message)
        

    def isLate(self):
        return self._late
    

    def pay(self):

        print("-----------------------------------------------------------------")
        print("                       Make a Payment")
        print("-----------------------------------------------------------------")
        print()

        print()
        print("                    Amount Due: $" + str(self._amountDue))
        print()

        payment = int(input("                    How much would you like to pay?"))

        print()
        
        if payment >= self._amountDue:
            
            self._amountDue = 0
            
            if self._late == True:
                self._late = False
                self._messages.remove(self.late_message)
        else:
            self._amountDue -= payment


            
    def recieveMail(self):

        self._hasMail = True
        
        if self.mail_message not in self._messages:
            self._messages.enqueue(self.mail_message)
        

    def recievePackage(self):
        
        self._hasPackage = True
        
        if self.package_message not in self._messages:
            self._messages.enqueue(self.package_message)

        

    def retrieveMail(self):
        print("-----------------------------------------------------------------")
        print("                   Retrieve Mail")
        print("-----------------------------------------------------------------")
        print()
        print()
        print("         Press 1 to retrieve mail from mailbox.")
        key = input("                          ")
        
        if key == "1":
            self._mailbox.dispenseMail(self)
            self._hasMail = False
            self._messages.remove(self.mail_message)
            print()
            print("                Mail has been retrieved.")
            
        else:
            return


    def retrievePackage(self):

        print("-----------------------------------------------------------------")
        print("                  Retrieve Single Package")
        print("-----------------------------------------------------------------")
        print()
        print()
        print("           Press 1 to retrieve single package from mailbox.")
        print("                   Press any other key to exit.")
        key = input("                          ")
        

        if key == "1":
            
            print()
            print("                      Enter Package ID:")
            packageID = input("                          ")
        
            package = self._mailbox.dispensePackage(packageID)
            

            if package != None:

                print()
                print("                {} has been retrieved.".format(package.contents()))
                
                if self._mailbox.packages() == "":
                    self._hasPackage = False
                    self._messages.remove(self.package_message)
            

            else:

                print()
                print("                      Invalid Package ID.")
                print()
                print("         Press 1 to try again, any other key to exit.")
                prompt = input("                                ")
                
                if prompt == "1":
                    
                    self.retrievePackage()

                
        else:
            return
            

    def retrievePackages(self):

        print("-----------------------------------------------------------------")
        print("                   Retrieve Packages")
        print("-----------------------------------------------------------------")
        print()
        print()
        print(" Press 1 to retrieve packages from mailbox, any other key to exit")
        key = input("                          ")
        
        if key == "1":
        
            self._mailbox.dispensePackages(self)
            self._hasPackage = False
        
            try:

                self._messages.remove(self.package_message)
                
                print()
                print("                Packages have been retrieved.")

            except:

                print()
                print("                        No Packages.")
                

        

    def hasMail(self):
        return self._hasMail
        

    def hasPackage(self):
        return self._hasPackage

    def readMessages(self):
        
        print("          + ------------------------------------------- +")
        print("          |                Message Center               |")
        print("          + ------------------------------------------- +")
        print()
        
        if len(self._messages.toList()) == 0:
            print("          No messages.")
            print()
            
        for item in self._messages.toList():
            print("          " + item)
            print()



    def move_boxes(self, mailbox_object):
        
        if self._mailbox.isEmpty():
            
            self._mailbox.removeBoxholder(self)
            
            self._mailbox = mailbox_object
            self._mailbox.addBoxholder(self)
            
        else:
            print("Cannot move boxes until all mail is taken and all packages are retrieved.")


    def close(self):
        
        if self._mailbox.isEmpty():
            self._mailbox.removeBoxholder(self)
            
        else:
            print("Cannot close account until all mail is taken and all packages are retrieved.")
        
def test():
    bob = Boxholder("bob")
    mailbox = Mailbox(123)
    bob.assignMailbox(mailbox)
    package = Package("123421341234", "bob", "thing")
    mailbox.addPackage(package)
    
    bob.retrievePackage()

