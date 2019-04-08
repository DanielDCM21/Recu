#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:18:24 2019

@author: danilo
"""
def main():
    x=eval(input("Give me x: "))
    sum=0
    for i in range(1,x+1):
        divisor=i
        if(i%2!=0):
            sum=sum+1/divisor
        else:
            sum=sum-1/divisor
    print("{0:.2f}".format(sum))
main()