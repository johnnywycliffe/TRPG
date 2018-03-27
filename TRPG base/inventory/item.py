#!/usr/bin/env python

""" item.py
    
    Base item class
    Author: Jeremy Stintzcum
    Date Modified: 03/27/18
"""

class Item:
    def __init__(self, name, wei, vol):
        self._name = name
        self._weight = float(wei)
        self._volume = float(vol)
        self._visible = True

    def Clone(self):
        """ Create a copy of this item for use """
        return Item(self._name,self._weight,self._volume)

    def GetName(self):
        return self._name

    def GetWeight(self):
        return self._weight

    def GetVol(self):
        return self._volume

    def GetVisable(self):
        return self._visible

    def SetName(self, val):
        self._name = val

    def SetWeight(self, val):
        self._weight = val

    def SetVol(self, val):
        self._volume = val

    def SetVis(self, val):
        self._visible = val
