#!/usr/bin/env python

""" container.py
    
    Container class that holds things.
    Author: Jeremy Stintzcum
    Date Modified: 02/04/18
"""
from item import Item

class Container:
    """ Container class
        
        mcw: Maximum Carry Weight
        vol: Maximum Volume
        name: String containing identifier
        closable: Bool representing latch/zipper
    """
    def __init__(self, mcw, vol, name = "Container", closable = False):
        self.Name = name
        self.MaxWeight = mcw
        self.MaxVolume = vol
        self.Items = []
        self.CurrWeight = 0.0
        self.CurrVol = 0.0
        self.Closable = closable
        self.Closed = False
        
    def addItem(self, item):
        """ Adds an item to the container
            
            item: item class to be added
        """
        if (self.CurrWeight + item.Weight) > self.MaxWeight:
            return 1 #Too heavy
        if (self.CurrVol + item.Volume) > self.MaxVolume:
            return 2 #Won't fit
        if self.Closed is True:
            return 3 #Container closed
        else:
            self.Items.append(item)
            self.CurrWeight += item.Weight
            self.CurrVol += item.Volume
            item.InContainer = True
            return 0 #Succesful add
        
    def listItems(self):
        """Returns list of items"""
        return self.Items
        
    def delItem(self, item):
        """ Removes item 
        
            item: item class to be removed
        """
        if item in self.Items:
            self.Items.remove(item)
            item.InContainer = False
            return item
        else:
            return 1 #No item in list
