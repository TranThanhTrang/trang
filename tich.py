# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:34:35 2024

@author: Administrator
"""

n=int(input("nhap so n:"))
tich=1
if n>0 and n%2==1:
    for i in range(1, n+1):
        tich=tich*i
    print("tich:",tich)
else:
    print("khong la so nguyen le lon hon 0")