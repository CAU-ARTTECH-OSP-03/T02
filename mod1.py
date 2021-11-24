from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


mbti = [0,0,0,0]

def adding(type, value) :

    if (value) :
        mbti[type] += 1

    else :
        mbti[type] -= 1



def mbti_result() :

    result = 0

    for i in range(0,4) :
        if mbti[i] > 0 :
            mbti[i] = 1

        else :
            mbti[i] = 0

    for i in range (0, 4) :
        result += mbti[i] * (2 ** (3-i))
        #print(mbti[i] * (2 ** (3-i)))

    return result
