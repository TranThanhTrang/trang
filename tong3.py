# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:28:20 2024

@author: Administrator
"""

n=int(input("nhap so n:"))
tong=0
if n>0 and n%2==0:
    for i in range(1, int(n/2) + 1):
        tong=tong+i*2
    print("tong:",tong)
else:
    print("khong la so nguyen chan lon hon 0")