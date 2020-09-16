"""
rankedpairs

This is a module that implements a lightweight ranked pairs voting algorithm. 

There are two main components to this, the Ranked Pairs module (rp) and the
Election class (Election). rp contains all the logic for Ranked Pairs, and 
Election is a wrapper class to make working with the data a bit easier. 

There is more documentation in each module (ie help(rankedpairs.Election))

Written by Simon Lequar, Dabney '22
"""
from .rp import *
from .election import Election
