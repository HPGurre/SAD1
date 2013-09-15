import sys
import re
import math
import itertools
from operator import attrgetter
from decimal import *

class Point():   
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    def __str__(self):
        return "Point(%s: [x=%s, y=%s])"%(self.name, self.x, self.y) 
    
def distance(p1, p2):
        return Decimal(math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2))

def closestPair(points):
    px = points[:]
    py = points[:]
    points.sort(key=lambda point: point.x)
    points.sort(key=lambda point: point.y)
    
    return closestPairRec(px, py)
    
def closestPairRec(PX, PY):    
    #Base case
    if len(PX) <= 3:
        min_pair = None
        min_distance = Decimal('Infinity')
        for p1, p2 in itertools.combinations(PX, 2):
            d = distance(p1, p2)
            if d < min_distance:
                min_pair = (p1,p2)
                min_distance = d
        return min_pair
    
    #Recursion
    QX = PX[:len(PX)//2]
    QY = PX[:len(PX)//2]
    RX = PX[len(PX)//2:]
    RY = PX[len(PX)//2:]
    
    QY.sort(key=lambda point: point.y)
    RY.sort(key=lambda point: point.y)
    
    qStar = closestPairRec(QX, QY)
    rStar = closestPairRec(RX, RY)
    
    #Work
    q_r_minimum = qStar if distance(qStar[0], qStar[1]) < distance(rStar[0], rStar[1]) else rStar   
    xStar = max(QX, key=attrgetter("x"))
#     L = I do not thin this pseudo line is needed
    S = [point for point in PX if abs(point.x-xStar.x) < distance(q_r_minimum[0], q_r_minimum[1])]
    
    S.sort(key=lambda point: point.y)
     
    s_minimum = None
    s_minimum_distance = Decimal('Infinity')
    for index, p1 in enumerate(S):
        for p2 in S[index+1:index+16]:
            d = distance(p1, p2)
            if d < s_minimum_distance:
                s_minimum = (p1,p2)
                s_minimum_distance = d
        
    if s_minimum_distance < distance(q_r_minimum[0], q_r_minimum[1]):
        return s_minimum
    else:
        return q_r_minimum
    
#REGEX for matching the lines in the file
number = "[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?"
pointPattern = re.compile( '[\s]*(\w+)\s+({0})\s+({0})'.format(number))

points = []    
#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:
        if pointPattern.match(line):
            tokens = line.split() 
            name = tokens[0]
            x =  Decimal(tokens[1])
            y = Decimal(tokens[2])
            points.append(Point(name, x, y))

closestPair = closestPair(points)
print(closestPair[0])
print(closestPair[1])
print("distance: "+ str(distance(closestPair[0], closestPair[1])))

