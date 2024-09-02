# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:43:06 2024

@author: Administrator
"""

a=float(input("nhap so a:"))
b=float(input("nhap so b:"))
if a==0 and b==0 or a==b :
    print("khong co ket qua")
else:
    c=((a+b)/(a**1/3+b**1/3)-(a*b)**1/3)/(a**1/3-b**1/3)**2
    print("ket qua la:",c)
    