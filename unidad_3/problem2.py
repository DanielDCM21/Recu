#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:12:05 2019

@author: danilo
"""
import random
def main():
    steps=eval(input("Give me the number of steps: "))
    cont=0
    for i in range(1,steps+1):
        a=random.randint(1,2)
        if(a%2==0):
            head=True
        else:
            head=False
            
        if(head==True):
            cont=cont+1
        else:
            cont=cont-1
            
    if(cont<0):
        cont=cont*-1
        
    print(cont/steps)
main()