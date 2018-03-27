#!/usr/bin/env python

""" container.py
    
    Container class that holds things.
    Author: Jeremy Stintzcum
    Date Modified: 03/27/18
"""

#Macros
CLOSED = 1
TOO_HEAVY = 2
TOO_LARGE = 3
NOT_IN_CONTAINER = 1

class Container:
    """ Container class
        
        mcw: Maximum Carry Weight
        vol: Maximum Volume
        name: String containing identifier
        closable: Bool representing latch/zipper
    """
    def __init__(self, mw, vol, name = "Bucket", closable = False):
        self._name = name
        self._maxWeight = mw
        self._maxVol = vol
        self._items = []
        self._cWeight = 0.0
        self._cVol = 0.0
        self._closable = closable
        self._closed = False

    def GetList(self):
        return self._items

    def AddItem(self, it):
        """ Add an item to the container if it fits
        
            it: Item instnace to add
        """
        if (self._cWeight + it.GetWeight()) > self._maxWeight:
            return TOO_HEAVY
        if (self._cVol + it.GetVol()) > self._maxVol:
            return TOO_LARGE
        if self._closed is True:
            return CLOSED
        else:
            self._items.append(it.Clone())
            self._cWeight += it.GetWeight()
            self._cVol += it.GetVol()
            it.SetVis(False)
            return

    def RemoveItem(self, name):
        """ Removes an item from the container if it exists
            
            name: Name of the item to be removed
        """
        for i in range(len(self._items)):
            if self._items[i].GetName() is name:
                self._cWeight = self._cWeight - self._items[i].GetWeight()
                self._cVol = self._cVol - self._items[i].GetVol()
                return self._items.pop(i)
        return NOT_IN_CONTAINER
