"""
Author: Richard Wong

File: Mailbox.py

Program Description:

Describes a Mailbox object

import MailBoxes

import Boxholder
"""

from Mail import *
from Boxholder import *
from Package import *

class Mailbox:
    def __init__(self, number):
        self._number = number
        
        self._boxholderDict = {}
        self._mailList = []
        self._packageDict = {}

    def number(self):
        return self._number
    

    def boxholders(self):
        
        boxholders = ""
        
        for key in self._boxholderDict:

            boxholders += key + ", "

        return boxholders
    

    def packages(self):

        packages = ""
        for key in self._packageDict:

            packages += key + ", "

        return packages


    def addBoxholder(self, boxholder):
        self._boxholderDict[boxholder.name()] = boxholder
        

    def removeBoxholder(self, boxholder):
        try:
            self._boxholderDict.pop(boxholder.name())

        except KeyError:
            print("          Boxholder not found.")


    def addPackage(self, packageObject):
        
        if packageObject.recipient() in self._boxholderDict:

            self._packageDict[packageObject.ID()] = packageObject
            
            guest = packageObject.recipient()

            boxholder = self._boxholderDict[guest]

            boxholder.recievePackage()
            
        else:

            print("          Incorrect mailbox/recipient.")
            

    def addMail(self, mailObject):
        
        self._mailList.append(mailObject)
        
        guest = mailObject.recipient()

        boxholder = self._boxholderDict[guest]

        boxholder.recieveMail()
            

    def dispensePackage(self, packageID):
        
        try:

            package = self._packageDict.pop(packageID)
            
            return package

        except KeyError:
            print("          Package not in mailbox.")
            

    def dispensePackages(self, guestObject):

        newDict = {}

        for key in self._packageDict:

            if self._packageDict[key].recipient() != guestObject.name():
                newDict[key] = self._packageDict[key]
        

            

    def dispenseMail(self, guestObject):
        
        for item in self._mailList:

            if item.recipient() == guestObject.name():
                self._mailList.remove(item)


    def isEmpty(self):
        
        if len(self._mailList) ==0 and len(self._packageDict) == 0:
            return True
        else:
            return False

    
