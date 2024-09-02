# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:54:04 2024

@author: Administrator
"""

a= float(input("nhap so a:"))
b= float(input("nhap so b:"))
if a==0 and b==0:
    print("phuong trinh vo so nghiem")
elif a!=0: 
    print("nghiem cua phuong trinh la:",-b/a)
else:
    print("phuon trinh vo nghiem")
    