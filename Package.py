"""
Author: Richard Wong

File: Package.py

Program Description:
Describes a Package object.
"""

class Package:
    def __init__(self, ID, recipient, contents):
        self._ID = ID
        self._recipient = recipient
        self._contents = contents

    def __str__(self):
        return str(self._recipient) + ", " + str(self._ID)

    def ID(self):
        return self._ID

    def recipient(self):
        return self._recipient

    def contents(self):
        return self._contents

    
