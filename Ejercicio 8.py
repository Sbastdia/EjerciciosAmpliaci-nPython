import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    manzanasCaídas=0
    naranjasCaídas=0
    for d in apples:
        if(a+d>s and a+d<t):
            manzanasCaídas+=1
    for o in oranges:
        if(b+o>s and b+o<t):
            naranjasCaídas+=1
    print('Han caído ' + manzanasCaídas + 'manzanas dentro de la casa.')
    print('Han caído ' + naranjasCaídas + 'naranjas dentro de la casa.')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)