#! /usr/bin/env python
#
# Simple PyScript to compute the median of numeric vals read from cmd args
# Written by Rohan. March 2 2015
#
import sys
import math
#
# Declare and initialize variables to store the median,
# and the list of sorted numbers
#
median = float('NaN')
valLs = [];
#
# Check that at least two arguments is provided
# Print an error message and exit, if not
#
if len(sys.argv) < 3:
    print "Usage: median n0 n1..."
    sys.exit(1)
#
# Loop through all the arguments
# If the current arg is numeric, add it to the list
#
for n in sys.argv[1:]:
    if (n.isdigit()):
        valLs.append(int(n))
#
# Sort the list of int args
# Declare an int var containing the lists mid point (i.e 1/2 x len(valLs)
#
valLs.sort()
midItm = int(math.floor(0.5*len(valLs)))
#
# Check whether the cardinality of the list is odd or even
# Then compute the median accordingly
#
if (len(valLs) % 2) == 0:
    median = 0.5*(valLs[midItm-1]+valLs[midItm+1])
else:
    median = valLs[midItm]
#
# Print output
#
print "n = %d" %(len(valLs))
print "min = %f" %(valLs[0])
print "median = %f" %(median)
print "max = %f" %(valLs[len(valLs)-1])
