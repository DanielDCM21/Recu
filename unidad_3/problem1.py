#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:54:05 2019

@author: danilo
"""

def main():
    n=eval(input("Give me the number"))
    
    while(n!=1):
        
        print("{0:.0f}".format(n))
        
        if(n%2==0):
            n=n/2
        else:
            n=(n*3)+1
    print("{0:.0f}".format(n))
main()