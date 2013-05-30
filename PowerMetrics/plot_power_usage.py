#! /usr/bin/env python

import numpy as np
import sys,os
from pylab import *

filename = 'PowerData.txt'

def format_time(tstr):
    tstr = tstr.split(':')
    if float(tstr[0]) == 12.: 
        return float(tstr[1])
    else: 
        return float(tstr[1]) + 60.

Time,Min,Max,Avg = [],[],[],[]
for line in open(filename).readlines():
    if line.startswith('#'): continue
    line = line[:-2].split('\t')
    Time.append(format_time(line[1]))
    Avg.append(float(line[2])*0.110)
    Max.append(float(line[3])*0.110)
    Min.append(float(line[4])*0.110)

title("Still power Usage")
plot(Time,Avg,label='Avg')
plot(Time,Min,label='Min')
plot(Time,Max,label='Max')
legend(loc='upper left')
xlabel('Minutes since start')
ylabel('kVA')
show()

