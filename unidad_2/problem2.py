#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:23:02 2019

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

def date(year):
    day=days(year)
    day=day-7
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
        if(year>=1800 and year<=2099):
            
            if(year==1954 or year==1981 or year==2049 or year==2076):
                date(year)
            else:
                date(year)
            flag=False
            
        else:
            print("Invalid date")
main()