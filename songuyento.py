# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:46:13 2024

@author: Administrator
"""

n=int(input("nhap vao so nguyen:"))
isNguyenTo = False
if n<2:
    isNguyenTo = False
    
else:    
    isNguyenTo = True
    for i in range(2, int(n/2)):
        if n%i==0:
           isNguyenTo = False
           break
              
if isNguyenTo:
    print("la so nguyen to")
else:
    print("khong la so nguyen to")
 