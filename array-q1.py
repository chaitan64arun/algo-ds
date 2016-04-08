""" Given two sorted arrays A and B, generate all possible arrays such that first
element is taken from A then from B then from A and so on in increasing order
till the arrays exhausted. The generated arrays should end with an element from
B.
For Example
A = {10, 15, 25}
B = {1, 5, 20, 30}
The resulting arrays are:
    10 20
    10 20 25 30
    10 30
    15 20
    15 20 25 30
    15 30
    25 30
"""

#!/usr/bin/python

aList = [10, 15, 25];
bList = [1,5,20,30];

class Array_Q1:
    # Print the list recursively
    def solve(self, aList, bList, traversed, highest):
        for i in range(len(aList)):
            num_a = aList[i]
            if num_a > highest:
                for j in range(len(bList)):
                    temp_traversed = traversed
                    num_b = bList[j]
                    if num_b > num_a:
                        temp_traversed += ' ' + `num_a` + ' ' + `num_b`
                        print temp_traversed
                        self.solve(aList[i+1:], bList[j+1:], temp_traversed, num_b)
obj = Array_Q1()
obj.solve(aList, bList, '', aList[0]-1)
