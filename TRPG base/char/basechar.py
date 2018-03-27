#!/usr/bin/env python

""" basechar.py
    
    Top level character class
    Author: Jeremy Stintzcum
    Date Modified: 03/24/18
"""
import tags, disguise

class char:
    """ Char class. The skeleton of any NPC and PC.
        
        ownerID: ID of owner. Can be server's ID
        name: Name for the caracter to use in game
    """
    def __init__(self, ownerID, name):
        #Attributes
        self._owner = ownerID
        self.__ID = uuid4()
        self._name = name
        
        #Physical attributes
        self._bodyParts = []
        self._aTags = tags.TagList()
        self._activeDisguise = CreateDisguise(self._name, self.__ID)
        
        #Mental attributes
        self.observance = 0.0
        self.mood = None
        #Mental lists
        self._pTags = tags.TagList()
        self.affiliations = []
        self.knownChars = []
        self.disguiseList = []

    def CreateDisguise(self, name, ID):
        self.disguiseList.append(disguise.Disguise(name,ID))

    def SetDisguise(self, disguise):
        self._activeDisguise = disguise
        if disguise not in self.disguiseList:
            self.disguiselist.append(disguise)

    def GetDisguise(self):
        return self._activeDisguise
