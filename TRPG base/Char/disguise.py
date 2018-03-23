#!/usr/bin/env python

""" disguise.py
    
    Disguise class for containing information related to disguises
    Author: Jeremy Stintzcum
    Date Modified: 03/23/18
"""
from uuid import uuid4
import tags

class Disguise:
    """ Visual and personality information to replace/augment base char
        
        name: String used to identify character in universe.
        aTags: dict of traits relating to appearance
        pTags: dict of traits relating to personality
    """
    def __init__(self, name):
        self.__ID = uuid4()
        self._name = name
        self._aTags = tags.TagList()
        self._pTags = tags.TagList()

    #setters and getters
    def GetID(self):
        return self.__ID

    def GetName(self):
        return self._name

    def GetATags(self):
        return self._aTags.GetList()

    def GetPTags(self):
        return self._pTags.GetList()

    def SetName(self, name):
        self._name = name
