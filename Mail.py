"""
Author: Richard Wong

File: Mail.py

Program Description:
Describes a Mail object.
"""

class Mail:
    def __init__(self, recipient, contents):
        self._recipient = recipient
        self._contents = contents #can either be a letter, postcard, envelope,
                                  #parcel, etc

    def __str__(self):
        return str(self._recipient) + ", " + str(self._ID)

    def recipient(self):
        return self._recipient

    def contents(self):
        return self._contents

    
