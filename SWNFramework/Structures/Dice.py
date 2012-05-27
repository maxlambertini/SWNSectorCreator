# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="massi"
__date__ ="$14-giu-2011 7.41.59$"

import random

def die(n):
    return random.randint(1,n)

def dN(num_faces = 6, num_die = 1, delta = 0):
    """
    Basic universal dice function.

    Arguments:
    - num_faces: the number of die's faces (default: 6)
    - num_die: the number of dice to roll (default: 1)
    - delta: an integer to be summed to the result (default : 0)
    """
    res  = 0
    for r in range(0,num_die):
        res += die(num_faces)
    return delta+res

    

def d6(num_die = 1, delta = 0):
    """
    Helper function that simulates rolling some six-sided dice:

    Arguments:
    - num_die: the number of dice to roll (default: 1)
    - delta: an integer to be summed to the result (default : 0)

    Examples:
    d6(3) = roll 3d6

    """
    return dN(6,num_die, delta)

def d10(num_die = 1, delta = 0):
    """
    Helper function that simulates rolling some ten-sided dice:

    Arguments:
    - num_die: the number of dice to roll (default: 1)
    - delta: an integer to be summed to the result (default : 0)

    Examples:
    d10(3) = roll 3d10

    """
    return dN(10,num_die, delta)


def dF(num_die = 1, delta = 0):
    """
    Helper function that simulates rolling some Fudge dice (-1,0,+1):

    Arguments:
    - num_die: the number of dice to roll (default: 1)
    - delta: an integer to be summed to the result (default : 0)

    Examples:
    dF(3) = roll 3dF

    """
    res  = 0
    for r in range(0,num_die):
        res += (die(3)-2)
    return delta+res



if __name__ == "__main__":
    print "D100: ", dN(100)
    print "D6: ", d6()
    print "DF: ", dF()
    print "3d6: ", d6(3)
    print "4dF: ", dF(4)

    print "2d6+6: ", d6(2,6)
    print "3dF+1: ", dF(3,1)
