#! /usr/bin/env python
# 
# Simple program to calculate the factorial of numbers read from cmdline
# Uses the iterative method of factorial computation
# By Rohan. March 2 2015
#
import sys
#
# Check that at least one argument is provided
# Print an error message and exit, if not
#
if len(sys.argv) < 2:
    print "Usage: fact n"
    sys.exit(1)
#
# Loop through all arguments, attempting to parse the argument into an integer
# Check the integer is positive, inform the user, and abs(n) if not.
# If all is now good, calculate its factorial iteratively
#
for n in sys.argv[1:]:
    #
    # Try parse n
    # If we cant parse n, print err and move on
    #
    try:
        x = int(n)
    except ValueError:
        print "%s is not a valid int" %(n)
        continue
    #
    # If n is negative, tell the user
    # Then reassign x to abs(n)
    #
    if x < 0:
        print "%d is negative. Computing abs(%d)!" %(n,n)
        x = abs(x)
    #
    # If n is non-zero, compute n! by fact = 1*2...*n
    # Otherwise 0! = 1
    #
    fact = 1
    if x != 0:
        for i in range(1,x+1):
            fact *= i;
    #
    # Print answer
    #
    print "%d! = %d" %(x,fact)
# Done!