#!/usr/bin/env python

""" attraction.py
    
    Class to allow for determination of like and love
    Author: Jeremy Stintzcum
    Date Modified: 03/24/18
"""
import tags, otherchar

#Macros
#Min and Max values for looks vs personality ratios
RATIOMIN = 0.0
RATIOMAX = 1.0
#For tags
TAG = 0
TVAL = 1
MERIT = 2
BPART = 6
#Max values for like and love
LIKEMAX = 1.0
LIKEMIN = -1.0

class Attraction:
    """ Detemines how liked/dislike or loved/hated a character is. this class is
        part of CharSocial, both a like and love version
        
        ratio: Ratio of looks to personality
    """
    def __init__(self, ratio):
        self._ratio = ratio
        self._aTags = tags.TagList()
        self._pTags = tags.TagList()

    def SetRatio(self, ratio):
        """ Sets appearance-personality importance ratios
        
            ratio: New value. 1 is only cares about appearance, 0 only 
                   personality
        """
        if ratio is not None:
            if ratio > RATIOMAX:
                self._ratio = RATIOMAX
            elif ratio < RATIOMIN:
                self._ratio = RATIOMIN
            else:
                self._ratio = ratio

    def GetRatio(self):
        return self._ratio

    def AddATag(self,t,tagVal,merit,hid,vis,tch,bprt=None):
        self._aTags.AddTag(t,tagVal,merit,hid,vis,tch,bprt)

    def AddPTag(self,t,tagVal,merit,hid,vis,tch,bprt=None):
        self._pTags.AddTag(t,tagVal,merit,hid,vis,tch,bprt)

    def GetATags(self):
        return self._aTags.GetList()

    def GetPTags(self):
        return self._pTags.GetList()

    def Evaluate(self, oc):
        """ Evaluates a character against their tags and returns a value
            
            oc: otherchar instance to be evaluated
        """
        percA = self.CompareLists(self.GetATags(), oc.GetATags())
        percP = self.CompareLists(self.GetPTags(), oc.GetPTags())
        percD = 0.0
        l = oc.GetActs()
        for i in range(len(l)):
            percD += l[i][1]
        total = ((self._ratio*percA)-(self._ratio*percP))+percD
        return (percA, percP, percD, total)

    def CompareLists(self, charList, ocList):
        """ Compares two lists of tags and spits out percent
            
            charList: List of tags evaluating character likes
            ocList: List of tags the other character has
        """
        val = 0.0
        posVal = 0.0
        negVal = 0.0
        for i in range(len(charList)):
            t1 = charList[i]
            if t1.Get(MERIT) > 0.0:
                posVal += t1.Get(MERIT)
            if t1.Get(MERIT) < 0.0:
                negVal += t1.Get(MERIT)
            for j in range(len(ocList)):
                t2 = ocList[j]
                if (t1.Get(BPART) is t2.Get(BPART) 
                    and t1.Get(TAG) is t2.Get(TAG) 
                    and t1.Get(TVAL) is t2.Get(TVAL)):
                    val += t1.Get(MERIT)
        if val is 0.0:
            percent = 0.0
        elif val > 0.0:
            percent = val / posVal
        elif val < 0.0:
            percent = 0.0 - (val / negVal)
        return percent
