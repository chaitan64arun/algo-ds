#!/usr/bin/python

"""
https://www.careercup.com/question?id=5664477329489920

You have given an array of integers. The appearance of integers vary (ie some integers appears twice or once or more than once)

How would you determine which integers appeared odd number of times ?

a[] = { 1,1,1, 2,5,10000, 5,7,4,8}
as you can see 1 appeared 3 times, 2 appeared once etc

"""
def outputOdd(argArray):
    finalArray = []
    for i in argArray:
        if i not in finalArray:
            finalArray.append(i)
        else :
            finalArray.remove(i)
    print finalArray

array = [1,2,3,4,4,4,2,3,1]

outputOdd(array)
