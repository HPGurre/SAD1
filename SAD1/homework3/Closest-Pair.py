import sys
import re
import math
import itertools

class Point():   
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    def __str__(self):
        return "Point(%s: [x=%s,y=%s])"%(self.name, self.x, self.y) 
    
def euclidianDistance(p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def closestPair(points):
    px = points[:]
    py = points[:]
    points.sort(key=lambda point: point.x)
    points.sort(key=lambda point: point.y)
    
    return ClosestPairRec(px, py)
    
def ClosestPairRec(pointsX, pointsY):    
    #Base case
    if len(pointsX) <= 3:
        min_pair = (pointsX[0], pointsX[1] )
        min_distance = euclidianDistance(pointsX[0], pointsX[1])
        for p1, p2 in itertools.combinations(pointsX, 2):
            distance = euclidianDistance(p1, p2)
            if distance < min_distance:
                min_pair = (p1,p2)
                min_distance = distanc
        return min_pair
    
    #Recoursion
    QX = pointsX[:len(pointsX)//2]
    QY = pointsX[:len(pointsX)//2]
    RX = pointsX[len(pointsX)//2:]
    RY = pointsX[len(pointsX)//2:]
    
    QY.sort(key=lambda point: point.y)
    RY.sort(key=lambda point: point.y)
    
    #Work
    qStar = ClosestPairRec(QX, QY)
    rStar = ClosestPairRec(RX, RY)
   
    minimum = qStar if euclidianDistance(qStar[0], qStar[1]) < euclidianDistance(rStar[0], rStar[1]) else rStar   

    return minimum
    
#     if true:
#         return 
#     elif:
#         return
#     else: 
    
    #Work
    
#REGEX for matching the lines in the file
number = "[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?"
pointPattern = re.compile( '[\s]?(\d+)\s+({0})\s+({0})'.format(number))

points = []    
#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:
        tokens = line.split() 
        name = tokens[0]
        x =  float(tokens[1])
        y = float(tokens[2])
        points.append(Point(name, x, y))
        
#         if pointPattern.match(line):
#             name = str(pointPattern.match(line).group(0))
#             x =  float(pointPattern.match(line).group(1))
#             y = float(pointPattern.match(line).group(2))
#             points.append(Point(name, x, y))
                    
closestPair = closestPair(points)
print(closestPair[0])
print(closestPair[1])

