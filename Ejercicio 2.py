import math
import os
import random
import re
import sys

def __init__(self, a, b):
    self.a=a
    self.b=b

def compareTriplets(a, b):

    puntosLucía=0
    puntosCarlos=0

    for i in range (0,3):
        if(a[i]<b[i]):
            puntosCarlos+=1
        elif(a[i]>b[i]):
            puntosLucía+=1

    puntosFinales=[puntosLucía, puntosCarlos]
    return puntosFinales




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
