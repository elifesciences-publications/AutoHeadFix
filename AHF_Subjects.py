#! /usr/bin/python3
#-*-coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from AHF_Base import AHF_Base

class AHF_Subjects (AHF_Base, metaclass = ABCMeta):
    """
    Base class for experimental subjects. Defines subject attributes. Subjects must be unique for ID attribute
    Subclasses may wish to define an inner class that describes an object for a single experimental subject.
    """

    @abstractmethod
    def setCurrent (self, IDnum):
        """
        Sets current individual in group of subjects based on a ID tag. The current subject id the one currently
        under test in the experimental apparatus. returns True if subject is in pool, else false
        """
        pass

    @abstractmethod
    def generator (self):
        """
        Generator function that generates all of the subjects in turn
        """
        pass

    @abstractmethod
    def add (self, IDnum, dataDict):
        """
        Adds a new subject to the pool of subjects, initializing subject fields with data from a dictionary
        returns True if subject was added, false if subjet with IDnum already exists in sibject pool
        """
        pass

    @abstractmethod
    def remove (self, IDnum):
        """
        Removes a subject from the pool of subjects, based on IDnumber. Returns true if subject with given OD was
        found and removed, returns false if no subject with IDnum was found in pool of subjects
        """
        pass

    @abstractmethod
    def userEdit (self):
        """
        Allows user interaction to add and remove subjects, maybe print out and edit individual configuration
        """
        pass

    @abstractmethod
    def show (self, IDNum = 0):
        """
        Prints out attributes for subject with given IDNum. If IDNum is 0, prints attributes for all subjects in pool.
        The attributes will be defined by subclass, results provided by stimulator, etc. Retyrns true if IDNum was found in
        pool, else False
        """

    

    


    
        
