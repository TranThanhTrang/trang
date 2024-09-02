# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:58:34 2024

@author: Administrator
"""

a=input("nhap 1 ki tu chu:")
if a.isupper():
    print("doi ki tu hoa thanh ki tu thuong :", a.lower())
else:
    hoa=a.upper()
    print("doi ki tu thuong thanh ki tu hoa :",hoa)