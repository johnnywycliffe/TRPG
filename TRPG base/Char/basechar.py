#!/usr/bin/env python

""" basechar.py
    
    Top level character class
    Author: Jeremy Stintzcum
    Date Modified: 03/17/18
"""

#TODO: Set up container properly... so, like, everything

class char:
    def __init__(self):
        #Attributes
        #All values that define a character.
        self.owner = ownerID #Hopefully, unique to a player/server/dm/whatever
        self.ID = uuid4() #Unique!
        self.name = name
        self.bodyParts = []
        self.observance = 0.5 # how likely this char is to learn new things
        
        # Apparel
        # Needed for mechanical and social. 
        
        #Social
        #
        
        #Mechanical/combat
        #All non-character to character interctions. PvE, fighting (excluding 
        #things like taunts) movement values. All fighting moves and stuff 
        #should be in here.
