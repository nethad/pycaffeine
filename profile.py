__author__ = 'thomas'

import pstats, cProfile

#import pyximport
#pyximport.install()

from pycaffeine import CafDeque

def run_profiling():
    deque = CafDeque()
    for i in xrange(1000000):
        deque.push("value")
        deque.pop()

cProfile.runctx("run_profiling()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()