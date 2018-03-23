#!/usr/bin/env python

""" interaction.py
    
    Detail interactions between characters
    Author: Jeremy Stintzcum
    Date Modified: 03/17/18
"""
#Interaction types:
#1 Seeing
#2 Touching
#3 Talking to
#4 Talking about
#5 Reading about

def isSeen(char1, char2, length):
    """ Details information exchange when two characters see each other
        
        char1: Character to recieve information
        char2: Character to get information from
        length: How long interaction lasts
    """
    


#Depriciated
def isObserved(self, charTwo, length, typeof, touchPoints=[]):
    """ Determines what is learned from another character during an 
        interaction. Each CharSocial is calling this independantly
        For instance, Char 1 can be completely unaware Char 2 is watching 
        them from the shadows.
    
        charTwo: Other CharSocial.
        length: Time of interaction
        typeof: the type of interaction
    """
    TrueID = False
    aTags = None
    pTags = None
    obs = charTwo.observance
    amount = obs * length #FIXME: Make more realistic
    #Switch disguise data if disguised
    if self.activeDisguise is None:
        ID = self.ID
        name = self.name
        #Tags gained from seeing someone
        if typeof is TO_SEE:
            aff = self.apparentAffiliation
            aTags = self.aTags
            tags = aTags.keys() 
            for tag in tags:
                if ">hidden<" in tag:
                    aTags.pop(tag)
        #Tags gained for talking to someone
        if typeof is TO_TALK:
            aff = self.apparentAffiliation
            aTags = self.aTags
            tags = aTags.keys() 
            for tag in tags:
                if ">hidden<" in tag:
                    aTags.pop(tag)
            pTags = self.pTags
            tags = pTags.keys() 
            for tag in tags:
                if ">hidden<" in tag:
                    pTags.pop(tag)
        #tags gained from touching someone
        if typeof is TO_TOUCH:
            aff = None
            aTags = self.aTags
            tags = aTags.keys() 
            for i in tags:
                if j in touchPoints:
                    if j not in bodyParts:
                        aTags.pop(i)
                elif ">visual<" in i:
                    aTags.pop(i)
    else:
        ID = self.activeDisguise.ID
        name = self.activeDisguise.name
        #Tags gained from seeing someone
        if typeof is TO_SEE 
            aff = self.activeDisguise.apparentAffiliation
            aTags = self.activeDisguise.aTags
            tags = aTags.keys() 
            for tag in tags:
                if ">hidden<" in tag:
                    aTags.pop(tag)
        #Tags gained for talking to someone
        if typeof is TO_TALK:
            aff = self.activeDisguise.apparentAffiliation
            aTags = self.activeDisguise.aTags
            tags = aTags.keys() 
            for tag in tags:
                if ">hidden<" in tag:
                    aTags.pop(tag)
            pTags = self.activeDisguise.pTags
            tags = pTags.keys() 
            for tag in tags:
                if ">hidden<" in tag:
                    pTags.pop(tag)
        #tags gained from touching someone
        if typeof is TO_TOUCH:
            aff = None
            aTags = self.activeDisguise.aTags
            tags = aTags.keys() 
            for i in tags:
                if j in touchPoints:
                    if j not in bodyParts:
                        aTags.pop(i)
                elif ">visual<" in i:
                    aTags.pop(i)
                    
    #How much additional infor is lost due to lack of percetion
    if amount > OB_PERF:
        continue
    elif amount > OB_HI:
        if rand() > OB_HI:
            aff = None
        tags = aTags.keys() 
            for tag in tags:
                if rand() > OB_HI:
                    aTags.pop(tag)
        tags = pTags.keys() 
            for tag in tags:
                if rand() > OB_HI:
                    pTags.pop(tag)
    elif amount > OB_MED:
        if rand() > OB_MED:
            aff = None
        tags = aTags.keys() 
            for tag in tags:
                if rand() > OB_MED:
                    aTags.pop(tag)
        tags = pTags.keys() 
            for tag in tags:
                if rand() > OB_MED:
                    pTags.pop(tag)
    elif amount > OB_LOW:
        if rand() > OB_LOW:
            aff = None
        tags = aTags.keys() 
            for tag in tags:
                if rand() > OB_LOW:
                    aTags.pop(tag)
        tags = pTags.keys() 
            for tag in tags:
                if rand() > OB_LOW:
                    pTags.pop(tag)
    else: #Almost nothing, name and ID
        aff = None
        atags = None
        ptags = None
        
    #tell charTwo to update
    charTwo.updateOtherChar(ID, name, aff, aTags, pTags)
