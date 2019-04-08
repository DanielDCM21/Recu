#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:26:24 2019

@author: danilo
"""

def main():
#    x=eval(input("Give me x: "))
    sum=2
    i=1
    while sum<=1800:
        print(sum)
        if(i%2!=0):
            sum=sum+3
        else:
            sum=sum+2
        i=i+1
main()