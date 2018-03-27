#!/usr/bin/env python

""" tags.py
    
    Tags system, used for identifying traits in characters
    Author: Jeremy Stintzcum
    Date Modified: 03/24/18
"""

#Settings
#Min and max values for like and love tags. Largely arbitrary
MINVAL = -1.0
MAXVAL = 1.0

class TagList:
    """ Class to contain tags
    
        bodypart: if bodypart is True, it's associated with a part. Like hair.
    """
    def __init__(self):
        self._tagList = []

    def AddTag(self,t,tVal,merit,hid,vis,tch,bprt = None):
        """ Defines a tag
            
            t: base tag string
            tagVal: Value to be assigned to tag
            hid: If the value is hidden, not immediately apparent
            vis: If value has to be seen. Overrides tch
            tch: If value is discovered by touch. Overridden by vis
            merit: How valuable tag is
            bprt: Which body part, if any
        """
        for i in range(len(self._tagList)):
            if self._tagList[i].Get(0) == t and self._tagList[i].Get(6) is bprt:
                return
        self._tagList.append(Tag(t,tVal,merit,hid,vis,tch,bprt))

    def RemoveTag(self, t, bprt = ""):
        """ Removes a tag if it exists
            
            t: base tag string
            bprt: Body part
        """
        for i in range(len(self._tagList)):
            if self._tagList[i].Get(0) == t and self._tagList[i].Get(6) is bprt:
                self._tagList.pop(i)
                return

    def GetTag(self, index, val=None):
        """ Gets a tag or tag value
            
            index: Index of tag to get.
            val: Which value of the tag to grab (0-7)
        """
        if index > len(self._tagList):
            return
        if val is not None:
            return self._tagList[index].Get(val)
        return self._tagList[index]
        
    def GetList(self):
        """ Returns list object """
        return self._tagList

class Tag:
    """ Defines a tag
        
        t: base tag string
        tagVal: Value to be assigned to tag
        hid: If the value is hidden, not immediately apparent
        vis: If value has to be seen. Overrides tch
        tch: If value is discovered by touch. Overridden by vis
        merit: How valuable tag is
    """
    def __init__(self,t,tVal,merit,hid,vis,tch,bpart = None):
        self._t = t
        self._tVal = tVal
        self._merit = min(max(merit, -1.0),1.0)
        self._hid = hid
        self._vis = vis
        if self._vis is True:
            self._tch = False
        else:
            self._tch = tch
        self._bodypart = bpart

    def Set(self, seq, val):
        """ Set a value
            
            seq: order in sequence. t = 0, tVal = 1 ... tch = 5
            val: new value
        """
        if seq is 1:
            self._tVal = val
        elif seq is 2:
            self._merit = min(max(val, -1.0),1.0)
        elif seq is 3:
            self._hid = val
        elif seq is 4:
            self._vis = val
            if val is True:
                self._tch = False
        elif seq is 5:
            self._tch = val
            if val is True:
                self._vis = False

    def Get(self, seq):
        """ Set a value
            
            seq: order in sequence. t = 0, tVal = 1 ... tch = 5, bodypart = 6
        """
        if seq is 0:
            return self._t
        elif seq is 1:
            return self._tVal
        elif seq is 2:
            return self._merit
        elif seq is 3:
            return self._hid
        elif seq is 4:
            return self._vis
        elif seq is 5:
            return self._tch
        elif seq is 6:
            return self._bodypart
