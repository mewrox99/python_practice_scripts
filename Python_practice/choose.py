#! /usr/bin/env python
#
# Calculate the Binomial coefficient (i.e n choose k)
#
# Uses the following recursive definition:
# choose(n,k) = choose(n-1,k-1)+choose(n-1,k)
# choose(n,0) = choose(n,n) = 1
#
import sys
def choose(n,k):
	#
	# Sanity check. 
	# Raise exception if k>n or if any arguments are negative
	#
	if k>n or k<0 or n<0:
		raise ValueError()
	#
	# Check for terminating case of k==0 or n==k
	#
	if k==0 or n==k:
		return 1
	#
	# Recurse if the terminating condition is not met
	#
	else:
		return choose(n-1,k-1)+choose(n-1,k)

# 
# We start the main body of the program by checking we have 3 arguments, exiting if not
#
if len(sys.argv) != 3:
	print "Usage choose n k"
	sys.exit(1)
#
# Next we attempt to parse the command line arguments into integers
#
x = int(sys.argv[1])
y = int(sys.argv[2])
#
# If we successfully parsed the args into ints, we pass them to choose(n,k) and print the result
#
print x,"choose",y,"=",choose(x,y)