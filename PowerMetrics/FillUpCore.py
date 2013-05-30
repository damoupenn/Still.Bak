#! /usr/bin/env python

from numpy import random
from time import time,sleep
import sys

tstart = time()

def ElapsedTime():
    return time() - tstart

while(ElapsedTime() < float(sys.argv[1])*60):
    x = random.uniform(1000)

print ElapsedTime()
