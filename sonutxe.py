# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:31:57 2024

@author: Administrator
"""

a=input("ban nhap bien so xe co 4 chu so:")
if len(str(a)) != 4:
    print("bien so xe phai co 4 chu so")
else:
    tach=list(str(a))
    s1,s2,s3,s4=map(int,a)
    tong=s1+s2+s3+s4
    nut=tong%10
    print("so nut xe cua ban la:",nut)
    