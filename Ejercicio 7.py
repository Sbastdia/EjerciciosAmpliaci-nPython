import math
import os
import random
import re
import sys


def gradingStudents(grades):
    listStudents=[]
    for grade in (grades):
        list.append(gradeStudents(grade))
    return listStudents

def gradeStudents(grade):
    finalGrade=0
    for grade in range(0, 100):
        if(grade<40):
            finalGrade= 'Suspenso'
        else:
            cociente=int(grade/5 + 1)
            multiple=cociente*5
            if(multiple-grade<3):
                finalGrade=multiple
    return finalGrade



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
        result = gradingStudents(grades)
        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')
        fptr.close()
