# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:52:37 2024

@author: Administrator
"""

a=int(input("nhap vao so thu nhat:"))
b=int(input("nhap vao so thu hai:"))
c=int(input("nhap vao so thu ba:"))
max=a
if b>max:
    max=b
elif c>max:
    max=c
else:
    max=a
print("so lon nhat la:",max)