#!/usr/bin/env python

""" disguise.py
    
    Disguise class for containing information related to disguises
    Author: Jeremy Stintzcum
    Date Modified: 03/24/18
"""
from uuid import uuid4
import tags

#TODO: Add apparel class to import, and handle it

#Macros
MINQUAL = 0.0
MAXQUAL = 1.0

class Disguise:
    """ Visual and personality information to replace/augment base char
        
        name: String used to identify character in universe.
        ID: ID number to use. Only set with default "disguises"
    """
    def __init__(self, name, ID=uuid4()):
        self.__ID = ID
        self._name = name
        self._quality = 0.0
        self._affiliation = None
        self._aTags = tags.TagList()
        self._pTags = tags.TagList()
        self._clothesList = []

    #setters and getters
    def GetID(self):
        return self.__ID

    def GetName(self):
        return self._name

    def GetQuality(self):
        return self._quality

    def GetAff(self):
        return self._affiliation

    def GetClothes(self):
        return self._clothesList

    def GetATags(self):
        return self._aTags.GetList()

    def GetPTags(self):
        return self._pTags.GetList()

    def SetName(self, name):
        self._name = name

    def SetQuality(val):
        self._quality = max(min(val,MAXQUAL),MINQUAL)

    def SetAff(self, val):
        self._affiliation = val

    def SetClothes(self):
        pass #FIXME

    def AddATag(self,t,tagVal,merit,hid,vis,tch,bprt=None):
        self._aTags.AddTag(t,tagVal,merit,hid,vis,tch,bprt)

    def AddPTag(self,t,tagVal,merit,hid,vis,tch,bprt=None):
        self._pTags.AddTag(t,tagVal,merit,hid,vis,tch,bprt)
