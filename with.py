# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:06:15 2017

@author: laiqingping
"""


with open("C:\\laiqingping\\SoftDevelopment\\Code\\Python\\Python\\filetest.txt","r") as somefile:
    ts=somefile.readline()
    print(ts)
"""
管道：将前一个命令的标准输出作为下一个命令的标准输入
sys.stdin.read:标准输入
sys.stdin.write:标准输出
简单点理解就是，把标准输出流和标准输入流连接起来的管道
"""
import sys
#sys.stdin.write("My name")   not support writable 输入流