# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:30:52 2017

@author: laiqingping
"""
import urllib
x = open("C:\\laiqingping\\SoftDevelopment\\Code\\Python\\Python\\filetest.txt","r")
line = x.readline()
print("line"+line)
#x.write("\nfsd")
text=x.read(20)
print(text)
print(x.tell())
#print(x)
#print(line)
x.close()
#print(x.read())
#htm = urllib.urlopen("http://www.baidu.com")

import sys

sys.stdout.writelines("Helloworld")

sys.stderr.write("i am a error")

