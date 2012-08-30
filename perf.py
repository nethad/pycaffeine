__author__ = 'thomas'

import timeit
from pycaffeine import CafDeque

rounds = 3
repeat = 1000000

def average(list):
    return float(sum(list)) / len(list)

class PerfPush:

    def setup_py(self):
        self.pylist = list()

    def execute_py(self):
        self.pylist.append("value")

    def setup_caf(self):
        self.cafdeque = CafDeque()

    def execute_caf(self):
        self.cafdeque.push("value")

    # timeit

    def timeit_py(self):
        tpy = timeit.Timer(self.execute_py, self.setup_py)
        return tpy.repeat(rounds, repeat)

    def timeit_caf(self):
        tcaf = timeit.Timer(self.execute_caf, self.setup_caf)
        return tcaf.repeat(rounds, repeat)

    def timeit(self):
        print "python list"
        times_py = self.timeit_py()
        print times_py
        print average(times_py)

        print "caffeine deque"
        times_caf = self.timeit_caf()
        print times_caf
        print average(times_caf)

class PerfPop:

    repeat = 1000

    def setup_py(self):
        self.pylist = list()

    def execute_py(self):
        for i in range(50):
            self.pylist.append("value")
        for i in range(50):
            self.pylist.pop()

    def setup_caf(self):
        self.cafdeque = CafDeque()

    def execute_caf(self):
        for i in range(50):
            self.cafdeque.push("value")
        for i in range(50):
            self.cafdeque.pop()

    # timeit

    def timeit_py(self):
        tpy = timeit.Timer(self.execute_py, self.setup_py)
        return tpy.repeat(rounds, self.repeat)

    def timeit_caf(self):
        tcaf = timeit.Timer(self.execute_caf, self.setup_caf)
        return tcaf.repeat(rounds, self.repeat)

    def timeit(self):
        print "python list"
        times_py = self.timeit_py()
        print times_py
        print average(times_py)

        print "caffeine deque"
        times_caf = self.timeit_caf()
        print times_caf
        print average(times_caf)

print "push"
perf_push = PerfPush()
perf_push.timeit()

print "pop"
perf_pop = PerfPop()
perf_pop.timeit()