# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:05:37 2024

@author: Administrator
"""

so=int(input("Nhap vao so nguyen duong co 2 chu so:"))
if so<10 or so>99:
    print("so khong hop le,nhap lai so co 2 chu so")
else:
    x=so//10+so%10
    print("tong cac chu so la:",x)
    