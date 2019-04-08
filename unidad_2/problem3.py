#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:33:06 2019

@author: danilo
"""
def bisiesto(year):
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    print("Give me a years range to find the leap years in format (x-y)")
    x=eval(input("Give me x: "))
    y=eval(input("Give me y: "))
    for i in range(x,y+1):
        if(bisiesto(i)==True):
            print(i)
        
main()