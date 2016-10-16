# ProbabilityCalculator

Description:

A Python/Django application that calculates probability for an n-sided die labelled with integers from 1 to n, to roll all the numbers {1, ..., n}, in any order if the die is thrown n times.

To run the application, go to the folder that has the file 'manage.py' and run the following command:
>>python manage.py runserver

To run the application, 
Analysis:

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

Scalability:

For large values of n, say 1000, computing n^n causes overflow, and hence I have used the Decimal packge with precision 100.
Unlike hardware based binary floating point, the decimal module has a user alterable precision (defaulting to 28 places) which can be as large as needed for a given problem

Unit Tests:
Test for values 1, 1000, negative numbers, letters, non integers.

