# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:58:24 2024

@author: Administrator
"""

a=int(input("nhap vao so nguyen duong a: "))
b=int(input("nhap vao so nguyen duong b: "))
if b==0:
    print("khong the chia cho 0")
else:
    print("phan nguyen cua phep chia",a,"cho",b,"la:",a//b)
    print("phan du cua phep chia",a,"cho",b,"la:",a%b)
    
    