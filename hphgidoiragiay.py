# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:59:42 2024

@author: Administrator
"""

tinh=input("Nhap gio phut giay:")
h=int(tinh.split('h')[0])
ph= int(tinh.split('h')[1].split('p')[0])
gi= int(tinh.split('p')[1].split('s')[0])
c=h*3600+ph*60+gi
print("gio phut giay doi ra giay la:",c)
