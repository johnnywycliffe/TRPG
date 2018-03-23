#!/usr/bin/env python

""" acts.py
    
    acts container
    Author: Jeremy Stintzcum
    Date Modified: 03/23/18
"""
from uuid import uuid4

class Act:
    """ Deed are events that happen. Who was involved, what happened, stuff like
        that is stored in this class 
        
        eventName: name of event
        actType: What type of action it is
        actorChar: Char doing the acting
        acteeChar: Char acted  upod
    """
    def __init__(self, eventName, actType, actorChar, acteeChar=None):
        self.__ID = uuid4()
        self._eventName = eventName
        self._actionType = actType
        self._actor = actorChar
        self._actee = acteeChar

    def GetID(self):
        return self.__ID

    def GetEvent(self):
        return self._eventName

    def GetActor(self):
        return self._actor

    def GetActee(self):
        return self._actee

    def GetActionType(self):
        return self._actionType

    def SetEvent(self, name):
        self._eventName = name

    def SetActor(self, char):
        self._actor = char

    def SetActee(self, char):
        self._actee = char
        
    def SetActionType(self, act):
        self.actionType = act
