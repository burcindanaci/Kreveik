from kreveik import *
import logging
import numpy as num
import shelve
logging.basicConfig(level=logging.INFO)

petri = classes.Family()
motiflist = []
scores = []
degrees = []
allmotifs = network.all_conn_motifs(3)

for i in xrange(200):
    a = network.generators.random(7, network.boolfuncs.xor_masking_C,
<<<<<<< HEAD
=======
                                     network.scorers.sum_scorer_f,
>>>>>>> refs/heads/master
                                     probability=(0.2,0.5,0.5),
                                     connected=True)
    petri.add(a)
    

petri.scorer = network.scorers.sum_scorer_f
petri.selector = network.selectors.hard_threshold_with_probability
petri.mutator = network.mutators.degree_preserving_mutation
petri.killer = family.killer.random_killer

    
for i in xrange(100):
    for j in xrange(20):
<<<<<<< HEAD
        print "("+str(i+1)+"/100) ("+str(j+1)+"/20)"
        kwargs = {'motiflist':allmotifs[:],'prob':0.2,'threshold':1.28}
        genetic.genetic_iteration(petri,**kwargs)
        scores.append(num.mean([network.score for network in petri]))
        degrees.append(num.mean([element.outdegree() for element in petri]))
=======
        print "("+str(i)+"/100) ("+str(j)+"/20)"
        kwargs = {'motiflist':allmotifs[:],'prob':0.4,'threshold':0.2}
        genetic.genetic_iteration(petri,**kwargs)
        degrees.append(num.mean([element.outdegree() for element in petri]))
        scores.append(num.mean([network.score for network in petri]))
>>>>>>> refs/heads/master
    motiflist.append(family.motif_freqs(petri, 3, **kwargs))
<<<<<<< HEAD
    theshelve = shelve.open("backup"+str(i)+"of100.dat")
    theshelve["petri"] = petri
    theshelve["scores"] = scores
    theshelve["degrees"] = degrees
    theshelve["motiflist"] = motiflist
    theshelve.close()
=======


>>>>>>> refs/heads/master
    
