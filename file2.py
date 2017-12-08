# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:44:49 2017

@author: laiqingping
"""
x = open("C:\\laiqingping\\SoftDevelopment\\Code\\Python\\Python\\filetest.txt","r")
while True:
    line = x.readline()
    if not line:
        break
    #print(line)
x.close()

y = open("C:\\laiqingping\\SoftDevelopment\\Code\\Python\\Python\\filetest.txt","r")

for line in y:
    print(line)
    
z = file("C:\\laiqingping\\SoftDevelopment\\Code\\Python\\Python\\filetest.txt")
