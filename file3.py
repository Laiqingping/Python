# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:57:39 2017

@author: laiqingping
"""

x = open("C:\\laiqingping\\SoftDevelopment\\Code\\Python\\Python\\filetest.txt","r")
print(x.tell())
text = x.readline(5)
#for i in range(0,5):
#    text+=x.readline()
text = x.readlines()
print(text)
x.close()

y = open("C:\\laiqingping\\SoftDevelopment\\Code\\Python\\Python\\filetest.txt","r")
import pprint

pprint.pprint(y.readlines()) 