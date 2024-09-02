# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:08:08 2024

@author: Administrator
"""

tg=input("nhap vao gio phut giay co dang hh:mm:ss:")
gio,ph,gi=map(int, tg.split(":"))
if gio>24 or ph>60 or gi>60 :
    print("khong the tinh ket qua, nhap lai gio phut giay")
else: 
    x=gio*3600+ph*60+gi;
    print("gio phut giay doi ra giay la: ",x)