#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:30:46 2019

@author: danilo
"""

def main():
    x=eval(input("Give me x: "))
    while(x!=1):
        print ("{0:.0f}".format(x))
        if(x%2==0):
            x=x/2
        else:
            x=x*3+1
    print ("{0:.0f}".format(x))
main()