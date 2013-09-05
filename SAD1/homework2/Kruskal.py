import sys
import re


#Data structures
cities=[]

#REGEX for matching the lines in the file
cityPattern = re.compile('^["]?\D*["]?$')
cityDistancePattern = re.compile('^\d*[13579][\s]')

#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:  
        if cityPattern.match(line):
            cities.append(line)
        elif cityDistancePattern.match(line):
            pass


# Kruskal(G, c) 
# Sort edges weights so that c1 <= c2 =< ... <=cm
# T is initially empty
#for (u belonging V) make a set containing singleton u

#  for i = 1 to m
# (u, v) = ei
#     if (u and v are in different sets) 
#          T = T UNION ei
#          merge the sets containing u and v
