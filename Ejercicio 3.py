import math
import os
import random
import re
import sys
import numpy as np


def aVeryBigSum(ar):
    suma=np.sum(ar)
    return suma


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()