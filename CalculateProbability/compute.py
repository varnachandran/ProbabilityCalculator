'''This file is used for the computation part
The problem is to find the probability of probability for an n-sided die labelled with integers from 1 to n, to roll
all the numbers {1, ..., n}, in any order if the die is thrown n times.
Consider a n=6 die.
probability of getting any number in the first throw = 6/6
probability of getting any other number in the second throw  = 5/6
probability of getting a third number(not first or the second number) = 4/6, etc

Therefore the probability for getting {1,2,3,4,5,6} in 6 throws is the product of all the above probabilities
6/6 * 5/6 * 4/6 * 3/6 * 2/6* 1/6 = (6* 5* 4* 3* 2* 1)/(6*6*6*6*6*6) = 6!/(6^6)

Similarly, for an n-sided die there are n^n total ways to
roll the die n times.
and the probability of getting all the numbers {1,2,3..n} in n throws is
n!/(n^n)
'''

#import math for FACTORIAL
import math

#import decimal for computing power of larger numbers
from decimal import *

def compute(numsides):

    #Set the precision of decimal
    try:

        getcontext().prec = 100

        sidescopy = Decimal(numsides)
        #Use the Decimal package to scale the program for larger numbers like 1000. Using the math POW function causes
        #overflow
        result=(math.factorial(numsides))/(sidescopy**sidescopy)
    except ValueError:
        print "Probability cannot be calculated for the given input"
    return result

if __name__ == '__main__':
    print compute(1)