#!/usr/bin/env python

""" CharSocial.py
    
    Character class used to represent a sapient entity
    Author: Jeremy Stintzcum
    Date Modified: 03/14/18
"""
from uuid import uuid4
from random import random as rand

#TODO: Add in evaluation process for like and love
#TODO: add way to talk about a third person, verbal and written
#TODO: Body parts: Generated by race, gender
#TODO: Add mood adder/rmer func
#TODO: Add reletionship adder/rmer func

#This is a class variable for highest level char class, unless race specific
sightTags = ["blue","red","green"]


# Special tags to concatenate
# ">body part<" for touching someone - EG, ">skin<":"smooth". Generated by 
# default once race and gender picked
# ">hidden<" added before the rest of the tag, excluded from certain results

#Settings
#Min and max values for like and love tags
MINVAL = -1.0 
MAXVAL = 1.0
#How much a character can randomly start liking or disliking someone.
#Max value of 2 (-1 to 1)
OFFSET = 0.5 
#Penalties assigned to finding out two people are one person. 0 to 1.0
LIKEPENALTY = 0.5
LOVEPENALTY = 0.75
#Observance levels
OB_LOW = 0.2
OB_MED = 0.4
OB_HI = 0.7
OB_PERF = 0.9

#Macros
#Min and Max values for looks vs personality ratios
RATIOMIN = 0.0
RATIOMAX = 1.0
#Type of interactions
TO_SEE = 1
TO_TALK = 2
TO_TOUCH = 3

#===============================================================================
class CharSocial:
    """ Character class used for interacting with things
        
        name = String containing name of character
        ownerID: the owner of the character
    """
    #All Chars have these options - Class, not instance
    relationships = ["Mother","Father","Brother","Sister","Friend","Enemy"]
    moods = ["Happy","Sad","Angry","Depressed"]
    def __init__(self, name, ownerID):
        #Attributes
        self.owner = ownerID #Hopefully, unique to a player/server/dm/whatever
        self.name = name
        self.ID = uuid4() #Unique!
        
        #State
        self.mood = 0 #TODO
        self.ActiveDisguise = None
        self.observance = 0.5 # how likely this char is to learn new things
        self.apparentAffiliation = None
        
        #lists
        self.aTags = {} #Physical appearance
        self.pTags = {} #Personality traits (Easily angered, happy go 
                                  #lucky, etc)
        self.known = [] #Known characters list (list of OtherChars)
        self.disguiseList = []
        self.affiliations = []
        self.bodyParts = []
        
        #like
        self.likeAppearanceRatio = 0.5 #How much looks matter over personality
        self.aLikedTags = {}
        self.aDislikedTags = {}
        self.pLikedTags = {}
        self.pDislikedTags = {}
        
        #love
        self.loveAppearanceRatio = 0.5 #How much looks matter over personality
        self.aLoveTags = {}
        self.aHateTags = {}
        self.pLoveTags = {}
        self.pHateTags = {}

    def ratios(self, like = None, love = None):
        """ Sets appearance-personality importance ratios
        
            like: float to overwrite old like ratio
            love: float to overwrite old love ratio
        """
        if like is not None:
            if like > RATIOMAX:
                self.likeAppearnceRatio = RATIOMAX
            elif like < RATIOMIN:
                self.likeAppearnceRatio = RATIOMIN
            else:
                self.likeAppearnceRatio = like
        if love is not None:
            if love > RATIOMAX:
                self.loveAppearnceRatio = RATIOMAX
            elif love < RATIOMIN:
                self.loveAppearnceRatio = RATIOMIN
            else:
                self.loveAppearnceRatio = love
    
    def addLikeTags(self, tag, tagVal, value, appearance, anti):
        """ Adds a like tag, its value, and deletes the tag from the dislike 
            dict.
        
            tag: String of trait to add
            tagVal: String describing tag (hair:blue or temperment:calm)
            value: float value of importance of trait
            appearance: bool to switch between personality (False) and 
                        appearance (True)
            anti: False means like, True means dislike
        """
        value = max(min(MAXVAL,value),MINVAL)
        tup = (tagVal, value)
        if appearance:
            if anti:
                if tag not in self.aDislikeTags:
                    self.aDislikeTags[tag] = tup
                while tag in self.aLikeTags:
                    self.aLikeTags.pop(tag, None)
            else:            
                if tag not in self.aLikeTags:
                    self.aLikeTags[tag] = tup
                while tag in self.aDislikeTags:
                    self.aDislikeTags.pop(tag, None)
        else:
            if anti:
                if tag not in self.pDislikeTags:
                    self.pDislikeTags[tag] = tup
                while tag in self.pLikeTags:
                    self.pLikeTags.pop(tag, None)
            else: 
                if tag not in self.pLikeTags:
                    self.pLikeTags[tag] = tup
                while tag in self.pDislikeTags:
                    self.pDislikeTags.pop(tag, None)
        
    def rmLikeTags(self, tag, appearance):
        """Remove tag from like dict
        
            tag: Value to remove
            appearance: bool to switch between personality (False) and 
                        appearance (True)
        """
        if appearance:
            while tag in self.aLikeTags:
                self.aLikeTags.pop(tag, None)
        else:
            while tag in self.pLikeTags:
                self.pLikeTags.pop(tag, None)
    
    def addLoveTags(self, tag, value, appearance):
        """ Adds a love tag, its value, and deletes the tag from the hate dict.
        
            tag: String of trait to add
            tagVal: String describing tag (hair:blue or temperment:calm)
            value: float value of importance of trait
            appearance: bool to switch between personality (False) and 
                        appearance (True)
            anti: False means love, True means hate
        """
        value = max(min(MAXVAL,value),MINVAL)
        tup = (tagVal, value)
        if appearance:
            if anti:
                if tag not in self.aHateTags:
                    self.aHateTags[tag] = tup
                while tag in self.aLoveTags:
                    self.aLoveTags.pop(tag, None)
            else:            
                if tag not in self.aLoveTags:
                    self.aLoveTags[tag] = tup
                while tag in self.aHateTags:
                    self.aHateTags.pop(tag, None)
        else:
            if anti:
                if tag not in self.pHateTags:
                    self.pHateTags[tag] = tup
                while tag in self.pLoveTags:
                    self.pLoveTags.pop(tag, None)
            else: 
                if tag not in self.pLoveTags:
                    self.pLoveTags[tag] = tup
                while tag in self.pHateTags:
                    self.pHateTags.pop(tag, None)
        
    def rmLoveTags(self, tag, appearance):
        """Remove tag from love dict
        
            tag: Value to remove
            appearance: bool to switch between personality (False) and 
                        appearance (True)
        """
        if appearance:
            while tag in self.aLoveTags:
                self.aLoveTags.pop(tag, None)
        else:
            while tag in self.pLoveTags:
                self.pLoveTags.pop(tag, None)
                
    def getLikeTags(self, appearance, anti, tag=None):
        """ Get like or dislike tag

            Appearance: bool to switch between personality (False) and 
                        appearance (True)
            anti: Bool, like/dislike
            tag: to grab a specific tag
        """
        if tag:
            if appearance:
                if anti:
                    return aDislikeTags[tag]
                else:
                    return aLikeTags[tag]
            else:
                if anti:
                    return pDislikeTags[tag]
                else:
                    return pLikeTags[tag]
        else:
            if appearance:
                if anti:
                    temp = aDislikeTags
                    return temp
                else:
                    temp = aLikeTags
                    return temp
            else:
                if anti:
                    temp = pDislikeTags
                    return temp
                else:
                    temp = pLikeTags
                    return temp
        
    def getLoveTags(self, appearance, anti, tag=None):
        """ Get like or dislike tag

            Appearance: bool to switch between personality (False) and 
                        appearance (True)
            anti: Bool, love/hate
            tag: to grab a specific tag
        """
        if tag:
            if appearance:
                if anti:
                    return aHateTags[tag]
                else:
                    return aLoveTags[tag]
            else:
                if anti:
                    return pHateTags[tag]
                else:
                    return pLoveTags[tag]
        else:
            if appearance:
                if anti:
                    temp = aHateTags
                    return temp
                else:
                    temp = aLoveTags
                    return temp
            else:
                if anti:
                    temp = pHateTags
                    return temp
                else:
                    temp = pLoveTags
                    return temp    
        
    def createDisguise(self, name, aTags, pTags):
        """ Create a new disguise 
            
            name: String to attach to the disguise
        """
        #Quits if disguise already exists (can't be two different Batmans)
        for i in range(self.disguiseList):
            if name is self.disguiseList[i].name:
                break
        #append to list of disguises
        self.disguiseList.append(disguise(name, aTags, pTags))  
    
    def setDisguise(self, name=None):
        """ Sets the active disguise
        
            name: Name of the disguise to set. if None, remove disguise
        """
        if name is None:
            self.activeDisguise = None
            break
        #Check if disguise exists and set it if it does
        for i in range(self.disguiseList):
            if name is self.disguiseList[i].name:
                self.activeDisguise = self.disguiseList[i]
        
    def updateOtherChar(self, newID, name, aff, newATags=None, 
        newPTags=None):
        """ Adds a known entity to the list
        
            newID: ID of other char, to avoid duplicates
            name: Name of new Otherchar
            aff: Apparent affiliation
            newATags: appearance tags to add. tuple (tag, tagval)
            newPTags: Personality tags to add. tuple (tag, tagval)
        """
        #Quit if already a made character
        for i in range(self.known):
            if newID is self.known[i].ID:
                break #FIXME: update preexisting characters
        #Instantiate
        newOtherClass = OtherClass(newID, name)
        #add affiliation
        if aff is not None:
            otherClass.addAffiliation(aff)
        #add appearnce tags
        for i in newATags:
            newOtherClass.aTags[newATags[i][0]] = newATags[i][1]
        #add personality tags
        for i in newPTags:
            newOtherClass.pTags[newPTags[i][0]] = newPTags[i][1]
        self.known.append(newOtherClass)
        
    def isObserved(self, charTwo, length, typeof, touchPoint=""):
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
            if typeof is TO_SEE #Only non-hidden stuff
                aff = self.apparentAffiliation
                #get tags
                aTags = self.aTags
                tags = aTags.keys() 
                for tag in tags:
                    if ">hidden<" in tag:
                        aTags.pop(tag)
            if typeof is TO_TALK:
                aff = self.apparentAffiliation
                #get tags
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
            if typeof is TO_TOUCH:
                aff = None
                aTags = self.aTags
                tags = aTags.keys() 
                for i in tags:
                    if i not in bodyParts:
                        continue
                    for j in sightTags:
                        if j in i:
                            aTags.pop(i)
        else:
            ID = self.activeDisguise.ID
            name = self.activeDisguise.name
            if typeof is TO_SEE #Only non-hidden stuff
                aff = self.activeDisguise.apparentAffiliation
                #get tags
                aTags = self.activeDisguise.aTags
                tags = aTags.keys() 
                for tag in tags:
                    if ">hidden<" in tag:
                        aTags.pop(tag)
            if typeof is TO_TALK:
                aff = self.activeDisguise.apparentAffiliation
                #get tags
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
            if typeof is TO_TOUCH:
                aff = None
                aTags = self.activeDisguise.aTags
                tags = aTags.keys() 
                for i in tags:
                    if i not in bodyParts:
                        continue
                    for j in sightTags:
                        if j in i:
                            aTags.pop(i)
        #if-else with no info, low info, medium, high, perfect
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
                 
#===============================================================================    
#Disguise class
class disguise:
    """ Visual and personality information to replace/augment base char
    
        name: String used to identify character in universe.
        aTags: dict of traits relating to appearance
        pTags: dict of traits relating to personality
    """
    def __init__(self, name, aTags, pTags):
        self.ID = uuid4()
        self.name = name
        self.aTags = aTags
        self.pTags = pTags
        
#===============================================================================        
# OtherChar class
class OtherChar:
    def __init__(self, ID, name):
        """ OtherChar is a "mental model" of a character
        
            ID: Unique ID
            Name: String associated with the ID
        """
        #Attributes
        self.ID = ID
        self.name = name
        self.otherIDs = [] #alias, pen names, known alter egos, disguises, etc
        self.otherNames = []
        self.affiliations = [] #affiliations. Organizations, other identities
        
        #tag lists
        self.aTags = {} #Physical appearance
        self.hTags = {} #Hidden attributes (moles, repressed personality bits)
        self.pTags = {} #Personality traits (Easily angered, happy go 
                                  #lucky, etc)
        
        #Relationship
        self.family = False
        self.relationship = 0
        self.like = -OFFSET/2.0 + (rand()/OFFSET) #Random to have a variance in new 
        self.love = -OFFSET/2.0 + (rand()/OFFSET) #people encountered. Covers having
                                           #"chemestry" with someone
    
    def setFamily(self, value):
        """ Set the family status of OtherChar in relation to the calling 
            character
        
            value: bool representing if two people are blood related
        """
        self.family = value
        
    def setRelationship(self, value):
        """ Set the relationship status of OtherChar in relation to the calling 
            character
        
            value: integer value
        """
        self.relationship = value
    
    def setLike(self, value):
        """ Set the like value
        
            value: integer value
        """
        if (self.like + value) > 1.0:
            self.like = 1.0
        elif (self.like + value) < -1.0:
            self.like = -1.0
        else:
            self.like += value
        
    def setLove(self, value):
        """ Set the love value
        
            value: integer value
        """
        if (self.love + value) > 1.0:
            self.love = 1.0
        elif (self.love + value) < -1.0:
            self.love = -1.0
        else:
            self.love += value
        
    def addDisguise(self, newOtherChar):
        """ Adds and combines knowledge of an identity to this one, a merge
        
            newOtherChar: OtherChar instance to be broken up and assimilated
        """
        #Append all IDs and Names from new to old OtherChar
        self.otherIDs.append(newOtherChar.ID)
        for i in newOtherChar.otherIDs:
            self.otherIDs.append(newOtherChar.otherIDs[i])
        self.otherNames.append(newOtherChar.name)
        for i in newOtherChar.otherNames:
            self.otherNames.append(newOtherChar.otherNamess[i])
        #Update family status
        self.family = self.family or newOtherChar.family
        #Add affiliations
        for i in newOtherChar.affiliations:
            self.affiliations.append(newOtherChar.affiliations[i])
        #Update like and love values. Note that these might get recalculated 
        #in the main char anyway
        self.like = ((newOtherChar.like + self.like)/2.0 
                    - abs(newOtherChar.like - self.like)*LIKEPENALTY)
        self.love = ((newOtherChar.love + self.love)/2.0 
                    - abs(newOtherChar.love - self.love)*LOVEPENALTY)
                    
                    
#===============================================================================
#Shared Functions
def addTag(self, appearance, tag, tagVal):
    """ Adds a tag to the correct list
    
        appearance: If the value is appearance (true) or personality (false)
        tag: String to add as a tag
    """
    if appearance and (tag not in self.aTags):
        self.appearanceTag[tag] = tagVal
    elif tag not in self.pTags:
        self.pTagstag] = tagVal

def rmTag(self, appearance, tag):
    """ removes a tag to the correct list
    
        appearance: If the value is appearance (true) or personality (false)
        tag: String to add as a tag
    """
    if appearance:
        while tag in self.aTags:
            self.apearanceTags.pop(tag)
    else:
        while tag in self.pTags:
            self.pTags.pop(tag)

def getTags(self, appearance):
    """ returns a list of tags for viewing or use
    
        appearance: Boolean switching between appearance (true) and 
        personality (false)
    """
    if appearance:
        newdict = self.aTags
    else:
        newlist = self.pTags
    return newdict

def addAffiliation(self, affTag):
    """ Adds a new affiliation to the list of known affiliations
    
        affTag: Affiliation string to add
    """
    if affTag not in self.affiliations:
        self.affiliations.append(affTag)

def rmAffiliation(self, affTag):
    """ Removes a new affiliation to the list of known affiliations
    
        affTag: Affiliation string to remove
    """
    while affTag in self.affiliations:
        self.affiliations.remove(affTag)
        
