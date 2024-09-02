# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:53:38 2024

@author: Administrator
"""

a=float(input("nhap so a:"))
b=float(input("nhap so b:"))
c=float(input("nhap so c:"))
denta=float
denta=b**2-4*a*c
if a==0 and b!=0:
    print("nghiem cua phuong trinh la:",-c/b)
elif a!=0 and denta<0:
    print("phuong trinh vo nghiem")
elif a!=0 and denta==0:
    print("phuong trinh co nghiem kep x1=x2=:",-b/2*a)
elif a!=0 and denta>0:
    print("phuong trinh co 2 nghiem x1=",(-b+denta**(1/2))/2*a," x2=",(-b-denta**(1/2))/2*a)
elif a==0 and b==0 and c==0:
    print(" phuong trinh vo so nghiem")
else:
    print(" phuong trinh vo nghiem")
