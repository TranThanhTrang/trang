# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:29:44 2024

@author: Administrator
"""

n=int(input("nhap so nguyen duong:"))
if n<0:
    print("khong la so nguyen duong, nhap lai")
else:
    print("cac uoc cua so:")
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
            
            