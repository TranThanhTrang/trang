# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:12:08 2024

@author: Administrator
"""

a=int(input("nhap so nguyen duong a:"))
b=int(input("nhap so nguyen duong b:"))
c=int(input("nhap so nguyen duong c:"))
if a==0 or b==0 or c==0 :
    print("3 canh tren khong tao thanh 1 tam giac")
if a+b>c and a+c>b and b+c>a :
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2== a**2 :
        print("tam giac tren la tam giac vuong")
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and a!=b):
        print("tam giac tren la tam giac can")
    elif a==b and a==c:
        print("tam giac tren la tam giac deu")
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print("tam giac tren la tam giac vuong")       
    else:
        print(" tam giac tren la tam giac thuong")
else:
    print(" 3 canh tren khong tao thanh 1 tam giac")