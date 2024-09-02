# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:01:31 2024

@author: Administrator
"""

h=int(input("nhap so gio: "))
p=int(input("nhap so phut: "))
g=int(input("nhap so giay: "))
if h>24 or p>60 or g>60 :
    print("khong hop le")
else:
    print("hop le")