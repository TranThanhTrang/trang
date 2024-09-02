# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:57:52 2024

@author: Administrator
"""

x=float(input("nhap so x:"))
n=int(input("nhap so n:"))
tong=x
if n>0:
    for i in range(2, n+1):
        tongnho=0
        for j in range(1, i+1):
            tongnho=tongnho+j
        tong=tong+x**i/tongnho
    print("tong:",tong)
else:
    print("khong la so nguyen lon hon 0")