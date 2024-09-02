# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:33:38 2024

@author: Administrator
"""

a=int(input("nhap vao so nguyen thu nhat:"))
b=int(input("nhap vao so nguyen thu hai:"))
c=int(input("nhap vao so nguyen thu ba:"))
d=int(input("nhap vao so nguyen thu tu:"))
min= a
if b<min :
    min=b
elif c<min :
    min=c
elif d<min :
    min=d
else:
    min=a
print("so nho nhat la:",min)
 
    