# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:48:14 2024

@author: Administrator
"""

n=int(input("nhap so n:"))
tong=1
if n>0:
    for i in range(1,n+1):
        tong=tong+1/(i*2+1)
    print("tong:",tong)
else:
    print("khong la so nguyen lon hon 0")