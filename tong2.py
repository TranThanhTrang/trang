# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:27:09 2024

@author: Administrator
"""

n=int(input("nhap so n:"))
tong=0
if n>0:
    for i in range(1, n+1):
        tong=tong+i**2
    print("tong:",tong)
else:
    print("khong la so nguyen lon hon 0")