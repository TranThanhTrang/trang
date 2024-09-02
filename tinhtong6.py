# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:53:46 2024

@author: Administrator
"""

n=int(input("nhap so n:"))
tong=0
if n>=0:
    for i in range(0,n+1):
        tong=tong+(2*i+1)/(2*i+2)
    print("tong:",tong)
else:
    print("khong la so nguyen lon hon hoac bang 0")