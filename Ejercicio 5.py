import math
import os
import random
import re
import sys


def gameOfStones(n):
    ganador=""
    if(jugada(n)!=0):
        ganador="P1 is the winner"
    else:
        ganador ="P2 is the winner"
    return ganador

def jugada(n):
    jugadaOptima=0
    modulo=n%7
    if(modulo>=2 and modulo<=3):
        jugadaOptima=2
    elif(modulo==4):
        jugadaOptima=3
    elif(modulo>=5 and modulo<=6):
        jugadaOptima=5
    return jugadaOptima


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        fptr.write(result + '\n')
        fptr.close()
