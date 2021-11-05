import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(0,n):
        escalera=''
        for p in range(0,n-1-i):
            escalera=escalera + " "
        for s in range(0,i+1):
            escalera=escalera + "# "
        print(escalera)


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)