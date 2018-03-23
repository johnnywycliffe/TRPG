#!/usr/bin/env python

""" otherchar.py
    
    Class representing one character's knowledge of another.
    Author: Jeremy Stintzcum
    Date Modified: 03/23/18
"""
from random import random as rand
import tags, acts

#Settings
#Penalties assigned to finding out two people are one person. 0 to 1.0
LIKEPENALTY = 0.5
LOVEPENALTY = 0.75
#How much a character can randomly start liking or disliking someone.
#Max value of 2 (-1 to 1)
OFFSET = 0.5

#Macros
MAXRANGE = 1.0
MINRANGE = -1.0

class OtherChar:
    """ OtherChar is a "mental model" of a character
        
        ID: Unique ID
        name: String associated with the ID
        fam: Bool true if related by blood
        rel: String relationship tag
    """
    #Relationship list is available to all instances
    def __init__(self, ID, name, fam, rel):
        #Attributes
        self.__ID = ID
        self._name = name #Tuple of all name bits?
        self._aTags = tags.TagList()
        self._pTags = tags.TagList()
        #Disguise vals
        self._otherIDs = []
        self._otherNames = []
        self._affiliations = []
        #Relative values
        self._chemVal = -OFFSET/2.0 + (rand()/OFFSET) #"chemestry" value
        self._family = fam
        self._relationship = rel
        self._acts = {}

    def AddActs(self, acts, importance):
        """ Adds an acts this otherchar did: Saved a puppy, killed the mayor, or
            even inhereted a fortune. Can also re-eval acts.
            
            acts: acts instance
            importance: How important that acts is to this person. -1.0 to 1.0
                        Negative means that the acts hurt rep instead of helping
        """
        imp = max(min(importance, MAXRANGE), MINRANGE)
        self._acts[acts] = imp

    def MergeOtherChars(self, newOtherChar):
        """ Adds and combines knowledge of an identity to this one, a merge
            Note that this will be char1.mergeDisguise(char2), so Char 2 is the 
            disguise. tonyStark.mergeDisguise(ironMan), not the other way around
            
            newOtherChar: OtherChar instance to be broken up and assimilated
        """
        #Tags
        #FIXME
        temp1 = self._aTags.GetList()
        temp2 = newOtherChar._aTags.GetList()
        temp1 += temp2
        temp1 = self._pTags.GetList() 
        temp2 = newOtherChar._pTags.GetList()
        temp1 += temp2
        #DisguiseVals
        self._otherIDs.append(newOtherChar.GetIDs()[0])
        for i in newOtherChar._otherIDs:
            self._otherIDs.append(i)
        self._otherNames.append(newOtherChar._name)
        for i in newOtherChar._otherNames:
            self._otherNames.append(i)
        for i in newOtherChar._affiliations:
            self._affiliations.append(i)
        #Relationship vals
        self._chemVal = (self._chemVal + newOtherChar._chemVal)/2.0
        self._family = self._family or newOtherChar._family
        #discard relationship, as the set one should be default. If not, update
        self._acts.update(newOtherChar._acts)

    #Setters and getters
    def GetIDs(self):
        return (self.__ID, self._otherIDs)

    def GetNames(self):
        return (self._name, self._otherNames)

    def GetFamily(self):
        return self._family

    def GetRelationship(self):
        return self._relationship

    def GetATags(self):
        return self._aTags.GetList()

    def GetPTags(self):
        return self._pTags.GetList()
        
    def GetActs(self):
        return self._acts

    def SetName(self, name):
        self._name = name

    def SetFamily(self, value):
        self._family = value

    def SetRelationship(self, value):
        self._relationship = value

    def AddATag(self,t,tagVal,merit,hid,vis,tch,bprt=None):
        self._aTags.AddTag(t,tagVal,merit,hid,vis,tch,bprt)

    def AddPTag(self,t,tagVal,merit,hid,vis,tch,bprt=None):
        self._pTags.AddTag(t,tagVal,merit,hid,vis,tch,bprt)
