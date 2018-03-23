#!/usr/bin/env python

""" container.py
    
    Container class that holds things.
    Author: Jeremy Stintzcum
    Date Modified: 02/04/18
"""

class Item:
    def __init__(self, name, wei, vol):
        self.Name = name
        self.Weight = wei
        self.Volume = vol
        self.InContainer = False
