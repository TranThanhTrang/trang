# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:45:37 2024

@author: Administrator
"""

a=int(input("nhap so a:"))
b=int(input("nhap so b:"))
print("tong la: ",a+b)
print("hieu la: ",a-b)
print("tich la: ",a*b)
if b==0 :
    print("khong the chia cho 0")
else:
    print("thuong la: ",round(a/b,3))
    