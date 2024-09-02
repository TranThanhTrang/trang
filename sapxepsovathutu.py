# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:04:22 2024

@author: Administrator
"""

a=float(input("nhap vao so thu nhat:"))
b=float(input("nhap vao so thu hai:"))
c=float(input("nhap vao so thu ba:"))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("thu tu tang dan la:", a, b, c)

N = input("Nhap so nguyen: ")

chusosapxep = ''.join(sorted(N))

print("So cac chu so thu tu tang dan la:", chusosapxep)

    