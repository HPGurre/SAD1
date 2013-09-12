import sys
import re
import math

class Point():
    
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

def EuclidianDistance(p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def ClosestPair(points):
    px = points[:]
    py = points[:]
    px = points.sort(key=lambda point: point.x)
    py = points.sort(key=lambda point: point.y)
    
    ClosestPairRec(px, py)
    
def ClosestPairRec(pointsX, pointsY):
    if len(pointsX) :
        [print(EuclidianDistance(p1, p2)) for p1 in pointsX for p2 in pointsX]

    ClosestPairRec(points[:len(points)/2])
    ClosestPairRec(points[len(points)/2+1:]);
    
#REGEX for matching the lines in the file
pointPattern = re.compile('[\s]?[+-]?')  

points = []    
#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f: 
            theLine = line.split();
            name = str(theLine[0])
            x = int(theLine[1])
            y = int(theLine[2])
            points.append(Point(name, x, y))
                    
ClosestPair(points)
