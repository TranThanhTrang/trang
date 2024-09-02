# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:11:51 2024

@author: Administrator
"""

a=input("nhap 1 ki tu chu thuong:")
if a.isupper():
    print("ki tu da la ki tu hoa")
elif a.islower():
    hoa=a.upper()
    print("doi ki tu thuong thanh ki tu hoa :",hoa)
else:
    print("ki tu khong hop le, hay nhap lai ki tu thuong")
    
    
    
    
   