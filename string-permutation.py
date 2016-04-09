#!/usr/bin/python

# recursive function
def permutation(prefix, current):
    if len(current) == 0:
        print prefix
    else:
        for i in range(len(current)):
            permutation(prefix + current[i], current[0:i] + current[i+1:])
   
# iterative function
def permute(string):
   print string
   
   for i in range(len(string)):
       for j in range(i+1,len(string)):
           prefix = string[:i] if i > 0 else '' 
           suffix = string[j+1:] if j < len(string) else ''
           middle = string[i+1:j] if j != i + 1 else ''
           print prefix + string[j] + middle + string[i] + suffix  

permute('abc')

print '***************'

permutation('', 'abc') 