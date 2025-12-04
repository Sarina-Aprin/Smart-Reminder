import itertools


class IDGenerator:
    def __init__(self):
        self.counter = itertools.count(1)
    def next_id(self):
        return next(self.counter)

id_gen = IDGenerator()