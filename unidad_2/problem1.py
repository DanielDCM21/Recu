#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:47:59 2019

@author: danilo

"""       
def days(year):
    a=year%19
    b=year%4
    c=year%7
    d=(19*a+24)%30
    e=(2*b+4*c+6*d+5)%7
    day=81+d+e
    return day
    
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

def date(year):
    if(bisiesto(year)==True):
        day=days(year)
        if(day>31):
            day=day-31
            if(day>28):
                day=day-28
                if(day>31):
                    day=day-31
                    if(day>30):
                        day=day-30
                        if(day>31):
                            day=day-31
                            if(day>30):
                                day=day-30
                                if(day>31):
                                    day=day-31
                                    if(day>31):
                                        day=day-31
                                        if(day>30):
                                            day=day-30
                                            if(day>31):
                                                day=day-31
                                                if(day>30):
                                                    day=day-30
                                                    if(day>31):
                                                        day=day-31
                                                    else:
                                                        print("Diciembre",day)
                                                else:
                                                    print("Noviembre",day)
                                            else:
                                                print("Octubre",day)
                                        else:
                                            print("Septiembre",day)
                                    else:
                                        print("Agosto",day)
                                else:
                                    print("Julio",day)
                            else:
                                print("Junio",day)
                        else:
                            print("Mayo",day)
                    else:
                        print("Abril",day)
                else:
                    print("Marzo",day)
            else:
                print("Febrero",day)
        else:
            print("Enero",day)
    else:
        day=days(year)
        if(day>31):
            day=day-31
            if(day>28):
                day=day-28
                if(day>31):
                    day=day-31
                    if(day>30):
                        day=day-30
                        if(day>31):
                            day=day-31
                            if(day>30):
                                day=day-30
                                if(day>31):
                                    day=day-31
                                    if(day>31):
                                        day=day-31
                                        if(day>30):
                                            day=day-30
                                            if(day>31):
                                                day=day-31
                                                if(day>30):
                                                    day=day-30
                                                    if(day>31):
                                                        day=day-31
                                                    else:
                                                        print("Diciembre",day)
                                                else:
                                                    print("Noviembre",day)
                                            else:
                                                print("Octubre",day)
                                        else:
                                            print("Septiembre",day)
                                    else:
                                        print("Agosto",day)
                                else:
                                    print("Julio",day)
                            else:
                                print("Junio",day)
                        else:
                            print("Mayo",day)
                    else:
                        print("Abril",day)
                else:
                    print("Marzo",day)
            else:
                print("Febrero",day)
        else:
            print("Enero",day)
        


def main():
    flag=True
    while(flag==True):
        year=eval(input("Give me a year in a range (1982-2048): "))
        if(year>=1982 and year<=2048):
            date(year)
            flag=False
            
        else:
            print("Invalid date")
main()