verbose=True
from ..probes import *
import wildtype
import logging


class Mutator (object):
    """This is the class definition for the mutators. A mutating function must be given as an
    input
    """
    def __init__ (self, function):
        self.mutation = function
    def __call__ (self,element):
        self.mutation(element)
    
        
class Selector (object):
    """This is the class definition for the selector of the genetic iteration
    The selecting function must be supplied as an input.
    """
    def __init__ (self,function):
        self.selection = function
    def __call__ (self,element):
        self.selection(element)  

class Killer (object):
    """This is the base class definition for the killer. A killing function must be supplied, which
    will act on ensemble objects.
    """ 
    def __init__(self,function):
        self.scoring=function
    def __call__(self,ensemble):
        self.scoring(ensemble)
        

class Scorer (object):
    """This is the base class definition for the scorers. A scoring function must be supplied.
    """ 
    def __init__(self,function):
        self.scoring=function
    def __call__(self,element):
        self.scoring(element)
        

def genetic_iteration(ensemble):
    '''
    Runs one iteration of the genetic algorithm.
    It finds wildtypes of the family, mutates them, populates the family with mutants
    and assasinates as much of it has mutated. 
    '''
    if ((ensemble.scorer == None) or (ensemble.selector == None)
        or (ensemble.mutator == None) or (ensemble.killer == None)):
        raise ValueError("An element needs its scorer, killer, selector and mutator \
        defined in order to be fed into the GA")
        break
    
    killcount = 0 
    for element in ensemble:
        try:
            ensemble.scorer(element)
        except: 
            logging.error("The scoring of the element failed.")
            
        if ensemble.selector(element):
            ensemble.add(ensemble.mutator(element))
            killcount =+ 1
    
    ensemble.killer(killcount)
        

