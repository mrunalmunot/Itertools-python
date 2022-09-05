import math
import os
import random
import re
import sys
import operator
import itertools


def performIterator(tuplevalues):
    # Write your code here
    #tuplevalues > 4 tup
    l=[]
    ll=[]
    for i in itertools.cycle(tuplevalues[0]):
        ll.append(i)
        if len(ll)==4:
            break
        
    l.append(tuple(ll))
    
    l.append(tuple(itertools.repeat(tuplevalues[1][0], len(tuplevalues[1]))))
    
    l.append(tuple(itertools.accumulate(tuplevalues[2])))
    
    l.append(tuple(itertools.chain(tuplevalues[0],tuplevalues[1],tuplevalues[2],tuplevalues[3])))
    
    
    l.append(tuple(itertools.filterfalse(filterfalse, l[-1])))
    
    return tuple(l)
    
def filterfalse(n):
    if n%2==0:
        return n
    
if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
